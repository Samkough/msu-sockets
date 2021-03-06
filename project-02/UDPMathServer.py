from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive.")
count = 0
result = 0

while True:
    num1, clientAddress = serverSocket.recvfrom(2048)
    num2, clientAddress = serverSocket.recvfrom(2048)  
    expression, clientAddress = serverSocket.recvfrom(2048)

    # pre-processing
    expression = expression.decode()
    expression = str(expression)
    expression = expression.lstrip()
    expression = expression.rstrip()
    
    if expression in ("+", "add", "addition"):
        result = int(num1) + int(num2)
        count = 1
    elif expression in ("-", "subtract", "subtraction"):
        result = int(num1) - int(num2)
        count = 2
    elif expression in ("*", "multiply", "multiplication"):
        result = int(num1) * int(num2)
        count = 3
    elif expression in ("/", "divide", "division"):
        result = int(num1) / int(num2)
        count = 4
    else:
        print("Didn't understand your expression...please try again.")
        resultString = "Try again!"
        serverSocket.sendto(resultString.encode(), clientAddress)
        continue

    print("Expression #" + str(count) + " Message to be sent back: " + str(result))
    serverSocket.sendto(str(result).encode(), clientAddress)

print("Server is closed. Bye!")
serverSocket.close()
