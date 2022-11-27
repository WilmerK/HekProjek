import nmap
nm = nmap.PortScanner()
nm.scan(hosts='192.168.4.4', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = nm.all_hosts()
hosts_list.remove('192.168.4.1')
print(hosts_list)
