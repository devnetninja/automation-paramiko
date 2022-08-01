from myparamiko import connect, get_shell, send_command, show, close
from routers2 import r1, r2, r3
import threading


def backup(router):
    client_connection = connect(**router)
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

    from datetime import datetime

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    filename = f"{router['hostname']}-backup_{year}{month}{day}_{hour}{minute}{second}.txt"
    # print(filename)
    with open(filename, 'w') as backup:
        backup.writelines(output)

    close(shell)

routers = [r1, r2, r3]
threads = list()
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()
    