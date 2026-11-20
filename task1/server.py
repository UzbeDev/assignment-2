import socket
menu = {
    "monday": "Plov is the food on Monday",
    "tuesday": "Lagman is the food on Tuesday",
    "wednesday": "Mastava is the food on Wednesday",
    "thursday": "Manti is the food on Thursday",
    "friday": "Fish is the food on Friday",
    'saturday': 'IUT Canteen is closed on weekends, try another day',
    'sunday':'IUT Canteen is closed on weekends, try another day'
}
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',5000))
server.listen()
client, addr = server.accept()
print(f'[{addr}] Client is connected!')
client.send("Welcome to the UIT canteen.".encode('utf-8'))
while True:
    m=client.recv(1024).decode('utf-8')
    if not m or m.lower()=='/exit':
        break
    for i in menu.keys():
        if i==m.lower() or (len(m)==3 and i[:3]==m[:3].lower()):
            food=menu.get(i)
            client.send(food.encode('utf-8'))
            break
    else:
            client.send('There is no such day'.encode('utf-8'))

server.close()
