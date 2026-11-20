import socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',5000))
while True:
    server_message=client.recv(1024).decode('utf-8')
    print('[SERVER]',server_message)
    user_input=input("[CLIENT] Enter the day> ")
    client.send(user_input.encode('utf-8'))
    if user_input.lower()=='/exit':
        break
client.close()
