from socket import *
import time
start_time = time.time()

if __name__ == "__main__":
    target = input('enter target ip address: ')
    t_ip = gethostbyname(target) # hold the ip adress
    print("Start scanning for ports: ",t_ip)

    for port in range(50,500):
        s = socket(AF_INET, SOCK_STREAM)

        connected = s.connect_ex((t_ip,port))
        if connected == 0:
            print(f'Port :{port} is open')
            s.close()

print("Time taken to scan ports: ", time.time() - start_time)