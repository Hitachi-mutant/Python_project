'''Home work for the lesson 34'''

'''Task 1 - A shared counter:
Make a class called Counter, and make it a subclass of the 
Thread class in the Threading module. Make the class have two global variables, 
one called counter set to 0, and another called rounds set to 100.000. 
Now implement the run() method, let it include a simple for-loop that 
iterates through rounds (e.i. 100.000 times) and for each time increments the 
value of the counter by 1. Create 2 instances of the thread and start them, 
then join them and check the result of the counter, it should be 200.000, right? 
Run it a couple of times and consider some different reasons why you get the answer that you get. '''
# import threading

# counter = 0
# rounds = 100000

# class Counter(threading.Thread):
#     def __init__(self, name, count):
#         super().__init__()
#         self.name = name
#         self.count = count

#     def run(self):
#         global counter
#         print(f"Thread {self.name} is starting.")
#         for i in range(1, self.count + 1):
#             with threading.Lock():
#                 counter += 1
#         print(f"Thread {self.name}: Counter {counter}")
#         print(f"Thread {self.name} is finished.")

# thread1 = Counter("Thread 1", rounds)
# thread2 = Counter("Thread 2", rounds)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# result = counter  # Access the global counter variable directly
# print(f"Final Counter Value: {result}")

# due to the GIL, you may not always get the exact result of 200,000. 
# The GIL can prevent true parallel execution of threads in CPU-bound tasks. 
# To escape race condition I've added a threading.Lock()

'''Task 2 - Echo server with threading
Create a socket echo server which handles each connection in a separate Thread.'''
import socket
import threading

host = 'localhost'
port = 8000

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.send(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            # continuously accept incoming client connections
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            # create a new thread and pass the client socket to the handle_client function as an argument
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()


'''Task 3 - Requests using multiprocessing:
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/

As a result, store all comments in chronological order in JSON and dump it to a file. 
For this task use Threads for making requests to reddit API.'''

# !!! This task should be skipped !!!