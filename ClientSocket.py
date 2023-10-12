from socket import *
import json


while True:
    serverName = "127.0.0.1"
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    operation = input('Please input Random, Subtract, Add or quit \n INPUT HERE: ')
    number1 = input("Please input your first number")
    number2 =input ("Please input your second number")

    Jsonformat = {"method": f"{operation}", "number1": f"{number1}", "number2": f"{number2}"}
    
    jsonfile = json.dumps(Jsonformat)

    clientSocket.sendall(bytes(jsonfile,encoding= "utf-8"))

    if (operation == "quit"):
        print("stopping")
        break
    #clientSocket.send(operation.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From server: ', modifiedSentence.decode())