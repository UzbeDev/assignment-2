import socket
addr = ('localhost',7070)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    message = input("Enter temperature> ")
    client.sendto(message.encode(), addr)
    if message.lower()=='/exit':
        break
    server_message = client.recvfrom(1024)[0]
    print(server_message.decode())
client.close()
