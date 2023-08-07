import os
import multiprocessing
import time

def read_time_data(q):
    while True:
        with open(os.path.join(os.path.dirname(__file__), "time.txt"), "r") as f:
            data = f.readline().strip()
            if data:
                num, B = data.split(',')
                print("队列发送数据:", num)
                q.put(num)
                with open(os.path.join(os.path.dirname(__file__), "time.txt"), "w") as f:
                    f.write(f"{num},1")
        time.sleep(5)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    process = multiprocessing.Process(target=read_time_data, args=(q,))
    process.start()
    process.join()
