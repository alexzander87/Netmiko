from getpass import getpass
from netmiko import ConnectHandler

cisco3 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
}

net_connect = ConnectHandler(**cisco3)
output = net_connect.send_command("show version")

with open("show_version.txt", "w") as f:
    f.write(output)

