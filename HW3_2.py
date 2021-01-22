from socket import *
from threading import Thread
from HttpRequest import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 7777
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

whiteList = []

f = open("WhiteList", "r")
while True:
    line = f.readline()

    if not line:
        break

    else:
        whiteList.append(line.strip('\n'))  # 개행문자 제거
f.close()

print('White Lists')
print('===============')
for allowed in whiteList:
    print(allowed)
print('===============')
print()

print('The server is ready to receive')
print()

n = 1
while True:
    connectionSocket, addr = serverSocket.accept()

    ip = addr[0]
    ipDivide = ip.split('.')
    print('IP Address : ', ip)
    print('Sub Network : ', end='')
    for i in range(2):
        print(ipDivide[i], end='')
        print('.', end='')
    print(ipDivide[2])
    print('Host :', ipDivide[-1])

    flag = 0
    for allowed in whiteList:
        temp = allowed.split('.')

        if temp[0] == ipDivide[0] and temp[1] == ipDivide[1] and temp[2] == ipDivide[2]:
            flag = 1
            break

    if flag:
        print("Allowed!")
        thrd = Thread(target=HttpRequestFunction, args=(connectionSocket, n))
        print()
        thrd.start()
        n += 1

    else:
        print('Not Allowed!')

    print()

serverSocket.close()
sys.exit()
