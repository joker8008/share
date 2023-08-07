import time
import multiprocessing
import queue

def countdown_process(q):
    time_left = 20

    while time_left > 0:
        try:
            data = q.get(timeout=1)
            num = int(data)
            print("接收到队列信息:", num)
            if num >= 0:
                time_left = num
                print("重新设置倒计时时间为:", time_left, "秒")
            else:
                print("无效的倒计时时间，忽略:", num)
        except queue.Empty:  # 使用正确的异常类型
            print("No data received from readtime.py in the last 5 seconds.")

        time.sleep(1)
        time_left -= 1

if __name__ == "__main__":
    q = multiprocessing.Queue()
    process = multiprocessing.Process(target=countdown_process, args=(q,))
    process.start()

    try:
        process.join()
    except KeyboardInterrupt:
        process.terminate()
