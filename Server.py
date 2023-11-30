import socket

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(hostname)
        self.port = 8000

        self.server.bind((self.ip, self.port))
        self.listen()


    def listen(self):
        self.allowed_messages = ["Hi", "Hey"]
        self.allowed_address = [self.ip]
    
        self.server.listen(0)

        print(f"Listening on {self.ip}:{self.port}")

        self.client_socket, self.client_address = self.server.accept()
        print(f"Accepted connection from {self.client_address[0]}:{self.client_address[1]}")

        if self.client_address[0] in self.allowed_address:
            while True:
                request = self.client_socket.recv(1024)
                request = request.decode("utf-8") # convert bytes to string
                
                if request.lower() == "close":
                    
                    self.client_socket.send("closed".encode("utf-8"))
                    break

                elif request in self.allowed_messages:

                    print(f"Received: {request}")
                    response = "accepted".encode("utf-8")
            
                else:
                    print('Message rejected')
                    response = "rejected".encode("utf-8")

                self.client_socket.send(response)
        
        else:
            print(f'Connection from {self.client_address[0]} rejected.')

        self.client_socket.close()
        print("Connection to client closed")
        self.server.close()


server = Server()