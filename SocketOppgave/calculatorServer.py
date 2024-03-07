from socket import*
import threading
import re


def handle_client(conn):
    while True:
        operation = conn.recv(1024).decode()
        if operation == "exit":
            break
        try:
            match = re.fullmatch("^\d+([ ]?[+\-*\/][ ]?\d+)+$", operation)
            if match:
                result = eval(operation)
                conn.send(str(result).encode())
            else:
                conn.send(b"Not a valid input")
        except Exception as e:
            conn.send(f"Error performing operation: {e}".encode())
    conn.close()


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen()
print("Server listening on 127.0.0.1:8000")
print("Waiting for connections...")
while True:
    conn, addr = server.accept()
    print(f"New connection from {addr}")
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()
    

