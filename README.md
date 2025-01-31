# mktLiberate

This project is also available in [Portuguese](/mktLiberate/README-pt.md).

## Project Description

**mktLiberate** is an automated system designed to manage and release queues on MikroTik devices. The system was developed to simplify network management, allowing users to make adjustments intuitively through a web interface.

The project consists of a Python backend that connects to MikroTik devices via SSH to execute specific commands, and a web frontend that enables users to interact with the system in a simple and efficient way.

## Key Features

- **IP Release**: The system allows the release of specific IPs on the network by disabling queues and creating an address list with a defined timeout.
- **Intuitive Web Interface**: A simple and user-friendly web interface for entering the router's IP and performing the release.
- **Command Automation**: Automatic execution of MikroTik commands via SSH to disable queues and create address lists.

## Technologies Used

- **Python**: For backend logic and SSH connection to MikroTik devices.
- **Paramiko**: Python library for SSH connections.
- **HTML/CSS**: For creating the web interface.
- **WSGI**: Interface for serving the web application.

## Licença

This project is licensed under MIT License. See the [LICENSE](LICENSE) file for more details.
