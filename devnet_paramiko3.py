from myparamiko import connect, get_shell, send_command, show, close
from routers2 import r1, r2, r3

client_connection = connect(**r1)
shell = get_shell(client_connection)

send_command(shell, 'enable')
send_command(shell, 'cisco')
send_command(shell, 'terminal length 0')
send_command(shell, 'show cdp neighbor')

output = show(shell)
print(output)

close(shell)