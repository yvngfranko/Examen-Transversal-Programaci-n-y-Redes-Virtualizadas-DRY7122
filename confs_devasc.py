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

cambio_nomb = "hostname Gonzalez-Munoz-Valdebenito"

with ConnectHandler(**conn) as conexion:
    conexion.send_config_set(cambio_nomb)
    show_nomb = "show running-config"
    out = conexion.send_command(show_nomb)
    print(out)