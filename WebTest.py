from socket import *
import time

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 7777
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('The server is ready to receive')

    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(2048).decode()
        print(message)

        filename = message.split()[1]
        print(filename)

        myfile = open(filename[1:], 'rb')

        response = myfile.read()
        myfile.close()

        header = 'HTTP/1.1 200 OK\n'

        if filename.endswith(".jpg"):
            filetype = 'image/jpg'

        elif filename.endswith(".mp4"):
            filetype = 'video/mp4'

        elif filename.endswith(".gif"):
            filetype = 'image/gif'

        elif filename.endswith(".wmv"):
            filetype = 'video/wmv'

        else:
            filetype = 'text/html'

        header += 'Content-Type: ' + str(filetype) + '\n\n'
        print(header)

        connectionSocket.send(header.encode())
        connectionSocket.send(response)
        connectionSocket.close()

    except IOError:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode()

        print(header)
        connectionSocket.send(header.encode())
        connectionSocket.send(response)
        connectionSocket.close()

serverSocket.close()
sys.exit()
