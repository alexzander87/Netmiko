from getpass import getpass
from netmiko import ConnectHandler

cisco3 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'show_version.txt',
}

net_connect = ConnectHandler(**cisco3)
print(net_connect.send_command("show version"))

