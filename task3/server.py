import socket

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost',7070))
while True:
    message, addr = server.recvfrom(1024)
    print(addr, ' is connected')
    if not message.decode() or message.decode().lower()=='/exit':
        break
    try:
        number=float(message.decode())
        if number<10:
            server.sendto(b'Very cold', addr)
        elif 10 <= number <= 24.9:
            server.sendto(b'Normal', addr)
        elif 25 <= number <=34.9:
            server.sendto(b'Warm', addr)
        elif 35<= number <= 44.9:
            server.sendto(b'High temperature', addr)
        elif number>=45:
            server.sendto(b'Critical', addr)
    except:
        server.sendto(b'Wrong format', addr)

server.close()