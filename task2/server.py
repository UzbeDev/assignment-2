import socket
questions={
    'Q1) What is a thread in python?\n':['A) a thin strand of fiber or material used in sewing\nB) Social media platform\nC) Library allows you to run multiple functions simultaneously\nD) CPU scheduling algorithm','C'],
    'Q2) What is a kernel in OS?\n':['A) Sunflower oil\nB) The heart of operating system\nC) One of the Coffman\'s condition\nD) RAG(Request allocator graph)','B'],
    'Q3) What is a OSI?\n': ['A) Open Systems Interconnection\nB) Open System interchange\nC) Operating System in Inha\nD) Ordered System Intentions','A'],
    'Q4) What is a TCP?\n': ['A) Transmission control protocol\nB) Transforming computer plugins\nC) Threading in Cpp(c++)\nD) Theoretical command prompt', 'A'],
    'Q5) What is a UDP?\n': ['A) United developers program\nB) Undoing developed program\nC) Utilized data place\nD) User datagram protocol', 'D'],
}
correct=0
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost',8080))
server.listen()
client, addr = server.accept()
result=''
disconnect=False
print(addr,'is Connected!')
for _ in questions.keys():
    while True:
        sendible=result+'\n'+_+questions.get(_)[0]
        try:
            client.send(sendible.encode())
            ans = client.recv(1024).decode()
        except:
            print('Connection is closed')
            disconnect=True
            break
        if ans.lower() == '/exit':
                disconnect = True
                client.close()
                server.close()
        if ans.lower() not in ('a','b','c','d'):
            result='Wrong format'
            continue
        else:
            if ans.upper()==str(questions.get(_)[1]):
                    result='Correct!'
                    correct+=1
            else:
                    result='Incorrect!'
            break
    if disconnect:
        break
if not disconnect:
    client.send(f"Your score: {correct}/5.".encode())
client.close()
server.close()
