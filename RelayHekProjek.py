import sqlite3
import getmac
import nmap

nm = nmap.PortScanner()
prevAmount = 0

while True:
    nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = nm.all_hosts()
    hosts_list.remove('192.168.1.1')
    print(hosts_list)

    if len(hosts_list) > prevAmount:
        for host in hosts_list:
            mac = getmac.get_mac_address(ip=host)
            connection = sqlite3.connect('OpenSesame.db')
            cursor = connection.cursor()
            try:    
                cursor.execute("SELECT EXISTS(SELECT 1 FROM tblDevices WHERE DeviceMAC ='" + mac + "');")
            except:
                bExists = 0
            bExists = cursor.fetchone()
            if bExists[0] == 1:
                cursor.execute("SELECT DeviceName FROM tblDevices WHERE DeviceMAC ='" + mac + "';")
                persoon = cursor.fetchone()
                print(persoon[0])
        prevAmount = len(hosts_list)
    elif len(hosts_list) < prevAmount:
        prevAmount = 0
