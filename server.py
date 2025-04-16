import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost',9999))

s.listen(2)
print('waiting for a connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", addr, name)
    c.send(bytes( 'Welcome Home', 'utf-8'))

#Added to GitHub
    c.close()
