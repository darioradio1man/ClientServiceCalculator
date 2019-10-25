import socket
from datetime import datetime
import calc

address = ('localhost', 26709)
max_size = 1000
print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
client, addr = s.accept()
calc = calc.Stack()

mydata = client.recv(1024).decode()
print(mydata)
while True:
    try:
        mydata = client.recv(1024).decode()
        print('Query: {}'.format(mydata))
        if mydata.lower() == "exit":
            break
        a = calc.infixToPostfix(mydata)
        print(a)
        value = calc.postfixEval(a)
        print("The final result is:  " + str(value))
        client.sendall(str(value).encode())
    except EOFError:
        break

client.close()
s.close()
