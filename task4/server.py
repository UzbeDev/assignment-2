import socket,threading
clients = []
def handle(client,addr):
    print(addr, 'Connected')
    try:
        username = client.recv(1024).decode()
        for i in clients:
            if i!=client:
                try:
                    i.send(f'\n{username} joined!\n'.encode())
                except:
                    clients.remove(i)
        while True:
            message = client.recv(1024).decode()
            if not message:
                break
            format=f'[{username}] {message}'.encode()
            for i in clients:
                if i!=client:
                    try:
                        i.send(format)
                    except:
                        clients.remove(i)
    except:
        pass
    finally:
        if client in clients:
            clients.remove(client)
        client.close()
def main():
    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost',5000))
    server.listen()
    while True:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle,args=(client,addr))
        thread.start()
main()