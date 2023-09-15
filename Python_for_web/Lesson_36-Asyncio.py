'''Home work for the lesson 36'''

'''Task 1 - Practice asynchronous code
Create a separate asynchronous code to calculate Fibonacci, 
factorial, squares and cubic for an input number. 
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. 
You need to get four lists of results from corresponding functions.
'''

import asyncio

async def fibonacci_async(input_number):
    if input_number <= 0:
        return []
    elif input_number == 1:
        return [0]
    elif input_number == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < input_number:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
            await asyncio.sleep(0) 
        return fib_sequence

async def factorial_async(input_number):
    if input_number == 0:
        return 1
    else:
        result = 1
        for i in range(1, input_number + 1):
            result *= i
            await asyncio.sleep(0)  
        return result

async def squares_async(input_number):
    return input_number * input_number

async def cubic_async(input_number):
    return input_number * input_number * input_number

async def main():
    results = {
        "Fibonacci": [],
        "Factorial": [],
        "Squares": [],
        "Cubic": []
    }

    for input_number in range(1, 11):
        # Run all functions for each input number
        fib_task = asyncio.create_task(fibonacci_async(input_number))
        fact_task = asyncio.create_task(factorial_async(input_number))
        squar_task = asyncio.create_task(squares_async(input_number))
        cub_task = asyncio.create_task(cubic_async(input_number))

        await asyncio.gather(fib_task, fact_task, squar_task, cub_task)

        fib_result = fib_task.result()
        fact_result = fact_task.result()
        squar_result = squar_task.result()
        cub_result = cub_task.result()

        results["Fibonacci"].append(fib_result)
        results["Factorial"].append(fact_result)
        results["Squares"].append(squar_result)
        results["Cubic"].append(cub_result)

    for input_number, result_dict in results.items():
        print(f"{input_number} Results:", result_dict)

if __name__ == "__main__":
    asyncio.run(main())

# Same task using multiprocessing module

import multiprocessing

def fibonacci(input_number):
    if input_number <= 0:
        return []
    elif input_number == 1:
        return [0]
    elif input_number == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < input_number:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence

def factorial(input_number):
    if input_number == 0:
        return 1
    else:
        result = 1
        for i in range(1, input_number + 1):
            result *= i
        return result

def squares(input_number):
    return input_number * input_number

def cubic(input_number):
    return input_number * input_number * input_number

def calculate_functions(input_number):
    fib_result = fibonacci(input_number)
    fact_result = factorial(input_number)
    squar_result = squares(input_number)
    cub_result = cubic(input_number)
    
    return {
        "Fibonacci": fib_result,
        "Factorial": fact_result,
        "Squares": squar_result,
        "Cubic": cub_result
    }

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    input_numbers = range(1, 11)
    results = pool.map(calculate_functions, input_numbers)

    for i, input_number in enumerate(input_numbers):
        print(f"Results for {input_number}:")
        for func_name, result in results[i].items():
            print(f"{func_name}: {result}")


'''Task 2 - Requests using asyncio and aiohttp
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/
store all comments in chronological order in JSON and dump them to a file. 
For this task use asyncio and aiohttp libraries for making requests to Reddit API.
'''

# !!! This task should be skipped !!!


'''Task 3 - Echo server with asyncio:
Create a socket echo server which handles each connection using asyncio Tasks.'''

import asyncio

async def handle_client(reader, writer):
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break
            message = data.decode()
            addr = writer.get_extra_info('peername')
            print(f"Received {message} from {addr}")

            writer.write(data)
            await writer.drain()
    except asyncio.CancelledError:
        pass
    finally:
        print(f"Closing connection from {addr}")
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8000)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
