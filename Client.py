import socket

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(hostname)
        self.port = 8000  
        
        self.client.connect((self.ip, self.port))

        self.communicate()

    def communicate(self):
        while True:
            message = input("Enter message: ")
            self.client.send(message.encode("utf-8")[:1024])

            response = self.client.recv(1024)
            response = response.decode("utf-8")

            if response.lower() == "close":
                break

            print(f"Received: {response}")

        self.client.close()
        print("Connection has closed")


client = Client()