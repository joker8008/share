import time
import multiprocessing

def read_time_data(q):
    while True:
        with open("time.txt", "r", encoding="utf-8") as f:
            data = f.read().strip()
            if data:
                try:
                    num, B = data.split(',')
                    if int(B) == 0:
                        q.put(num)
                        print("已发送数据给 time.py:", num)
                    else:
                        print("B 已修改为 1，忽略数据:", num)
                except ValueError:
                    print("数据格式错误，忽略数据:", data)
        time.sleep(5)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    process = multiprocessing.Process(target=read_time_data, args=(q,))
    process.start()

    try:
        process.join()
    except KeyboardInterrupt:
        process.terminate()
