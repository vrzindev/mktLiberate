# mktLiberate

Este projeto também está disponível em [inglês](/README.md).

## Descrição do Projeto

O **mktLiberate** é um sistema automatizado desenvolvido para gerenciar e liberar filas (queues) em dispositivos MikroTik. O sistema foi criado com o objetivo de facilitar a gestão de redes, permitindo que usuários realizem ajustes de forma intuitiva através de uma interface web.

O projeto consiste em um backend em Python que se conecta aos dispositivos MikroTik via SSH para executar comandos específicos, e um frontend web que permite aos usuários interagir com o sistema de forma simples e eficiente.

## Funcionalidades

- **Liberação de IPs**: O sistema permite liberar IPs específicos na rede, desabilitando filas (queues) e criando uma lista de endereços com um timeout definido.
- **Interface Web Intuitiva**: Uma interface web simples e fácil de usar para inserir o IP do roteador e realizar a liberação.
- **Automatização de Comandos**: Execução automática de comandos MikroTik via SSH para desabilitar filas e criar listas de endereços.

## Tecnologias Utilizadas

- **Python**: Para a lógica de backend e conexão SSH com os dispositivos MikroTik.
- **Paramiko**: Biblioteca Python para conexão SSH.
- **HTML/CSS**: Para a criação da interface web.
- **WSGI**: Interface para servir a aplicação web.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.