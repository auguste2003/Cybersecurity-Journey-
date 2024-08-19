import socket
import time
import subprocess


def get_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        return banner
    except Exception as e:
        return str(e)
    finally:
        s.close()


def stop_service(ip, port):
    # Diese Funktion kann implementiert werden, um einen Dienst zu stoppen, wenn du administrativen Zugriff hast.
    # In einem echten Szenario, könntest du SSH verwenden, um dich mit dem Gerät zu verbinden und den Dienst zu stoppen.
    pass


if __name__ == "__main__":
    start_time = time.time()
    target = input('Enter target IP address: ')
    t_ip = socket.gethostbyname(target)

    print("Start scanning for ports: ", t_ip)

    for port in range(50, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        connected = s.connect_ex((t_ip, port))
        if connected == 0:
            print(f'Port {port} is open')
            banner = get_banner(t_ip, port)
            if banner:
                print(f'Service Info: {banner}')
                # Weitere Aktionen können hier eingefügt werden, um den Dienst zu analysieren oder zu stoppen
        s.close()

    print("Time taken to scan ports: ", time.time() - start_time)
