import socket

ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]

with open('address.txt', 'r') as f:
    list.hosts = f.read()

print("Ожидайте, идет сканирование портов!")

# hosts = list.append(hosts)


for port in ports:
    for host in hosts:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((host, port))
        except socket.error:
            pass
        else:
            with open('result_scan.txt', 'a') as f:
                f.write(f"{host}: {port} порт активен")
            s.close()
print("Сканирование завершено!")
