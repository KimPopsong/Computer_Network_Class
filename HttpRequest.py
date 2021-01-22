import time

def HttpRequestFunction(conSocket, n):
    try:
        message = conSocket.recv(2048).decode()

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

        elif filename.endswith(".html"):
            filetype = 'text/html'

        else:
            raise IOError

        header += 'Content-Type: ' + str(filetype) + '\n\n'

        conSocket.send(header.encode())
        conSocket.send(response)
        conSocket.close()

        print(n, '번째 스레드 시작')
        for i in range(100):
            print(n, '번째 스레드', i, '번째 실행 중')
            time.sleep(1)

    except IOError:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode()

        print(header)
        conSocket.send(header.encode())
        conSocket.send(response)
        conSocket.close()