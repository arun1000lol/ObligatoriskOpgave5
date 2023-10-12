from socket import *
import threading
import random
import json

def handle_client(connectionSocket, addr):

    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode("utf-8")
        sentence = json.loads(sentence)
        print(addr,sentence)
        operation1 = sentence["method"]
        operation2 = sentence["number1"]
        operation3 = sentence["number2"]

        number1 = float(operation2)
        number2 = float(operation3)

        response = "Didn't understand, please send a proper message"
        if sentence == "quit":
            keep_communicating = False
            response = "closing the connection"
        elif operation1 == "Random":
            response = random.randint(number1, number2)
        elif operation1 == "Add":
            response = number1 + number2
        elif operation1 == "Subtract":
            response = number1 - number2

        output = str(response)
        print(output)
        connectionSocket.send(output.encode())
    #connectionSocket.close()

serverPort = 12000
serverHost = '127.0.0.1'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()