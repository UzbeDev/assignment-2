import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',8080))
while True:
    try:
        server_message=client.recv(1024).decode()
        print(server_message)
        answer=input("> ")
        client.send(answer.encode())
        if not server_message or answer.lower() == '/exit':
            break
    except:
        print('Connection is closed')
        break
client.close()
