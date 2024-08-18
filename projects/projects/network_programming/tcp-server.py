import socket

if __name__ == "__main__":

    # Defining the socket parameters
    host = "127.0.0.1"
    port = 8081
    totalClients = int(input("How many clients do you want to connect to? "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reusing the address
    sock.bind((host, port))
    sock.listen(totalClients)

    connexions = []

    print("Initiating clients")

    # Accept connections from clients
    for i in range(totalClients): # loop all client files
        conn, addr = sock.accept() # hold the adress and the connexion
        connexions.append(conn)  # add to the file
        print(f"Connected with client {i + 1}")

    fileno = 0
    for conn in connexions: # inter in the connexion
        fileno += 1
        data = conn.recv(1024).decode("utf-8") # decode the message  . WE recieve data<1024
        if not data:
            continue
        filename = f'output{fileno}.txt' # create a format file
        with open(filename, "w") as fo:
            while data:
                fo.write(data) # open the file and wirte the informations behind
                data = conn.recv(1024).decode("utf-8")
            print(f"Received file from client {fileno} successfully! New filename is: {filename}")
        conn.close()

    sock.close()
