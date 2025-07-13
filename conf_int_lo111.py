import netmiko
import json
import requests

from netmiko import ConnectHandler
conn = {

    'device_type' : 'cisco_ios',
    'host' : '192.168.100.76',
    'port' : '22',
    'username' : 'cisco',
    'password' : 'cisco123!'

}

conf_int = {
    'interface loopback 111',
    'ip address 111.111.111.111 255.255.255.255',
    'no shutdown'
}

show_int = 'show ip interface brief'

with ConnectHandler(**conn) as conexion:
    conexion.send_config_set(conf_int)
    out = conexion.send_command(show_int)
    print(out)