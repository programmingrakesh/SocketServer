import socket


IP = socket.gethostbyname(socket.gethostname())
PORT = 9090


class Server():


    def __init__(self, msg):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((IP, PORT))
        self.server.listen()
        while True:
            self.conn, self.addr = self.server.accept()
            msg = input(">>>")
            self.conn.send(msg.encode("utf-8"))




class client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((IP,PORT))
        while True:
            self.data2 = self.client.recv(1024).decode("utf-8")
            print(self.data2)
