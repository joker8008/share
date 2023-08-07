import time
import multiprocessing

def read_time_data(q):
    while True:
        with open("time.txt", "r") as f:
            data = f.read().strip()
            if data:
                num, B = data.split(',')
                print(f"Readtime.py Sending: {num}")
                q.put(num)
                if B == '0':
                    print("Setting B to 1")
                    with open("time.txt", "w") as f:
                        f.write(f"{num},1")
        time.sleep(5)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=read_time_data, args=(queue,))
    process.start()
    process.join()
