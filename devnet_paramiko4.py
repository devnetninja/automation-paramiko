from myparamiko import connect, get_shell, send_command, show, close
from routers2 import r1, r2, r3

client_connection = connect(**r1)
shell = get_shell(client_connection)

send_command(shell, 'enable')
send_command(shell, 'cisco')
send_command(shell, 'terminal length 0')
# send_command(shell, 'show version')
# show(shell)
send_command(shell, 'show running-config')

output = show(shell)
output_list = output.splitlines()[9:-2]
output = '\n'.join(output_list)

with open('backup-config.txt', 'w') as backup:
    backup.writelines(output)


close(shell)