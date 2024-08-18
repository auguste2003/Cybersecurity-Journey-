import socket

if __name__ == "__main__":

    # Defining the socket parameters
    host = "127.0.0.1"
    port = 8081

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP socket
    sock.connect((host, port))  # Connect to the server

    # File transfer loop
    while True:
        filename = input("Enter the name of the file you want to send/transfer: ")
        try:
            with open(filename, "r") as fi:
                data = fi.read()
                if data:
                    sock.sendall(data.encode()) # encode and send the data
            print(f"File '{filename}' sent successfully.")
            break  # Exit after sending the file
        except IOError:
            print("You input an invalid filename! Please try again.")

    sock.close()  # Close the client socket
