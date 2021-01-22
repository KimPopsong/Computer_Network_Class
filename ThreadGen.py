from socket import *
from threading import Thread
from HttpRequest import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 7777
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

n = 1
while True:
    connectionSocket, addr = serverSocket.accept()
    thrd = Thread(target=HttpRequestFunction, args=(connectionSocket, n))
    print()
    thrd.start()
    n += 1

server_socket.close()
sys.exit()