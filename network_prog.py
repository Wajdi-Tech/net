from netmiko import ConnectHandler

router ={
    'device_type': 'cisco_ios',
    'host':'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password' :'C1sco12345',
    'port' : 22,
}
try:
    print("connexion au routeur...")
    net_connect = ConnectHandler(**router)
    print("affichage de l'heure coté routeur")
    clock_output = net_connect.send_command("show clock")
    print("Date et heure :", clock_output)
    print("Récupération des interfaces...")
    interfaces_output = net_connect.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as file:
        file.write(interfaces_output)
    print("les interfaces ont été enregistrés dans 'interfaces.txt'.")
    print("configuration de l'interface Loopback")
    config_commands = [
       "interface loopback 0",
       "ip address 10.8.8.8 255.255.255.240",
    ]
    config_output = net_connect.send_config_set(config_commands)
    print("configuration de l'interface Loopback terminée")
    print(config_output)
    net_connect.disconnect()
    print("Déconnexion du routeur")
except Exception as e:
    print(f"Erreur lors de l'exécution : {e}")
