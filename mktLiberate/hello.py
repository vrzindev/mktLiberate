import paramiko
import cgi

def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        router_ip = form.getvalue('routerIP')
        result = execute_script(router_ip)
        status = '200 OK'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return [result.encode('utf-8')]
    else:
        with open('index.html', 'r') as file:
            response = file.read()
        status = '200 OK'
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        return [response.encode('utf-8')]

def execute_script(router_ip):
    username = 'liberarbanda'
    password = 'liberar@123'

    # Comandos MikroTik
    get_address_list_command = '/ip firewall address-list print detail'
    check_address_list_command = '/ip firewall address-list print where comment="queue_controlada" detail'
    disable_queues_command = '/queue simple disable [find name="DVRs"] ; /queue simple disable [find name="Central"]' 
    create_address_list_command = '/ip firewall address-list add address=0.0.0.0 list=liberado timeout=01:00:00'

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conecte-se ao dispositivo MikroTik
        ssh_client.connect(router_ip, username=username, password=password, timeout=10)

        # Execute o comando para listar detalhes da address list
        stdin, stdout, stderr = ssh_client.exec_command(get_address_list_command)

        # Leia a saída para obter os detalhes da address list
        output = stdout.read().decode('utf-8')

        # Separe as linhas de saída em uma lista
        output_lines = output.split('\n')

        # Flag para indicar se o timeout foi encontrado
        timeout_found = False

        # Itere sobre as linhas para encontrar os timeouts
        for line in output_lines:
            if 'timeout' in line:
                # Extrai o timeout da linha
                timeout = line.split('=')[1].strip()
                response = f"O IP ENCONTRA-SE LIBERADO, TEMPO RESTANTE: {timeout}"
                timeout_found = True  # Define a flag como True quando o timeout é encontrado
                break  # Encerra o loop se o timeout for encontrado

        # Se o timeout não for encontrado, desabilite as queues e crie a address list
        if not timeout_found:
            ssh_client.exec_command(disable_queues_command)
            ssh_client.exec_command(create_address_list_command)
            response = 'IP LIBERADO COM SUCESSO!!!'

        return response

    except paramiko.SSHException:
        response = 'IP INVÁLIDO\nERRO: PODE SER QUE O IP NÃO EXISTA OU O MIKROTIK NÃO TENHA PERMISSÃO \n CASO OCORRA ALGUMA DÚVIDA, CONTATE O VITOR RAMOS'
        return response

    finally:
        # Feche a conexão SSH para evitar futuros problemas
        ssh_client.close()
