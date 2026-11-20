import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(('localhost', 5000))
print('Welcome to the termigram')
username = input("Enter your username> ")
server.send(username.encode())
def listener():
    try:
        while True:
            server_message = server.recv(1024).decode()
            if not server_message:
                break
            print(f"\r\033[K{server_message}\n[{username}]> ", end="", flush=True)
    except:
        print('\nConnection closed')

def sender():
    while True:
        m = input()
        if m.lower() == '/exit':
            server.send('is left.'.encode())
            server.close()
            break
        server.send(m.encode())
    print(f"\r\033[K[{username}]>", end="", flush=True)
thread1 = threading.Thread(target=listener, daemon=True)
thread2 = threading.Thread(target=sender)
thread1.start()
thread2.start()
thread2.join()