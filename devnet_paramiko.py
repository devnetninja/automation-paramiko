import paramiko
import time
from routers import r1, r2, r3

routers = [r1, r2, r3]
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# print(ssh_client)
for router in routers:
    print(f'Connecting to {router["hostname"]}...')   
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    shell = ssh_client.invoke_shell()
    # shell.send('show version\n')
    shell.send('enable\n')
    shell.send('cisco\n')
    shell.send('terminal length 0\n')
    shell.send('show run\n')
    time.sleep(3)

    output = shell.recv(10000)
    output = output.decode('utf-8')
    print(output)


    if ssh_client.get_transport().is_active() == True:
        print()
        print('Closing connection..')
        ssh_client.close()
        print()
        print('-'*70)