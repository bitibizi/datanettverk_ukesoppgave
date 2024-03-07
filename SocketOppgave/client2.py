from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8000))

while True:
    operation = input("Enter a mathematical operation (e.g., '7 + 10'), or 'exit' to quit: ")
    client.send(operation.encode())
    if operation.lower() == 'exit':
        break
    result = client.recv(1024).decode()
    print(f"Result from server: {result}")

client.close()