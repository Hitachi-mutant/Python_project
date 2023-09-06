'''Home work for the lesson 35'''

'''Task 1 - Primes
We have the following input list of numbers, some of them are prime. 
You need to create a utility function that takes as input a number and returns 
a bool, whether it is prime or not. 
 '''

# !!! This task should be skipped !!!


'''Task 2 - Requests using concurrent and multiprocessing libraries
Download all comments from a subreddit of your choice,
store all comments in chronological order in JSON and dump it to a file.'''

# !!! This task should be skipped !!!

'''Task 3 - Echo server with threading:
Create a socket echo server that handles each connection using the multiprocessing library.'''

import socket
import multiprocessing

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        # Send this data back to the client
        client_socket.send(data)

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind it to host and port
    server_socket.bind(("127.0.0.1", 8000))

    server_socket.listen(5)
    print("Server is listening on port 8000")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Create a new process to handle the client
        client_handler = multiprocessing.Process(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
