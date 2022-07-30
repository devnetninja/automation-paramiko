import paramiko
import time

def connect(hostname, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {hostname}")
    ssh_client.connect(hostname=hostname, port=port, username=username, password=password, 
                look_for_keys=False, allow_agent=False)
    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f"Sending command: {command}")
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    return output.decode('utf-8')

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print()
        print('Closing connection..')
        ssh_client.close()
        print()

if __name__ == '__main__':
    from routers import r1, r2, r3

    for r in [r1, r2, r3]:
        # client = connect('10.141.50.196', '22', 'cisco', 'cisco')
        client = connect(**r)

        shell = get_shell(client)

        send_command(shell, 'enable')
        send_command(shell, 'cisco')
        send_command(shell, 'term len 0')
        # send_command(shell, 'sh version')
        # send_command(shell, 'sh ip int brief')
        send_command(shell, 'show run', 3)

        output = show(shell)
        print(output)

        close(shell)
        print('-'* 70)
