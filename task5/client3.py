import socket,threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost',8080))
username = input("Enter username> ")
server.send(username.encode())
print(f"Choose Rock, Paper, scissors (R/P/S)")
def listen():
    while True:
        try:
            server_message = server.recv(1024).decode()
        except:
            print('Connection closed')
            server.close()
            break
        if not server_message:
            server.close()
            break
        print(server_message)

def sender():
    while True:
        message = input()
        if message.lower()=='/exit':
            server.close()
            break
        try:
            server.send(message.encode())
        except:
            server.close()
            print('Connection closed')
            break

thread1= threading.Thread(target=listen, args=())
thread2= threading.Thread(target=sender, args=())
thread1.start()
thread2.start()
thread1.join()
thread2.join()
