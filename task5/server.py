import socket, threading, time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',8080))
server.listen()
clients = []
choices = {}
usernames = []
game_over=False
def handle(client, addr):
    global  game_over
    print(addr, 'is connected')
    username = None
    try:
        username = client.recv(1024).decode()
        if not username:
            raise ConnectionError
        usernames.append(username)
        while not game_over:
            if len(clients) >= 2:
                break
            client.send('Waiting for other players to join...'.encode())
            time.sleep(5)
        while True:
            message = client.recv(1024).decode()
            if not message:
                raise ConnectionError
            if not message.upper() in ('R', 'P', 'S'):
                client.send('Wrong format'.encode())
            else:
                choices[username]=message.upper()
                break
        while not game_over:
            if len(clients)==len(choices) and len(clients) >= 2:
                break
            client.send('Waiting for other players to choose...'.encode())
            time.sleep(5)
    except:
        if client in clients:
            clients.remove(client)
        if username in usernames:
            usernames.remove(username)
        if username in choices:
            choices.pop(username)
        client.close()
        return

    if game_over:
        return
    game_over = True
    x = 0
    while x < len(usernames)-1:
        i = x+1
        while i < len(usernames):
            if choices[usernames[x]] == choices[usernames[i]]:
                both_in_one = usernames[x] + ' and ' + usernames[i]
                choices[both_in_one] = choices[usernames[x]]
                choices.pop(usernames[x])
                choices.pop(usernames[i])
                usernames.pop(i)
                usernames[x] = both_in_one
            else:
                i+=1
        x+=1
    if len(choices) == 1:
        for i in clients:
            i.send(f'draw'.encode())
            i.close()
        server.close()
        return
    for x in range(len(choices)-1):
        if len(usernames) == 3:
            for i in clients:
                i.send(f'draw'.encode())
                i.close()
            server.close()
            break

        elif choices[usernames[x]]=='R' and choices[usernames[x+1]]=='S':
            for i in clients:
                i.send(f'{usernames[x]} is winner'.encode())
                i.close()
            server.close()
            break


        elif choices[usernames[x]]=='R' and choices[usernames[x+1]]=='P':
            for i in clients:
                i.send(f'{usernames[x+1]} is winner'.encode())
                i.close()
            server.close()
            break
        elif choices[usernames[x]]=='P' and choices[usernames[x+1]]=='S':
            for i in clients:
                i.send(f'{usernames[x+1]} is winner'.encode())
                i.close()
            server.close()
            break
        elif choices[usernames[x]]=='S' and choices[usernames[x+1]]=='P':
            for i in clients:
                i.send(f'{usernames[x]} is winner'.encode())
                i.close()
            server.close()
            break
        break
def main():
    while True:
        try:
            client, addr = server.accept()
            clients.append(client)
            thread = threading.Thread(target=handle, args=(client, addr))
            thread.start()
        except:
            break
main()
server.close()