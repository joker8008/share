import time
import queue
import multiprocessing


def countdown_process(q):
    countdown = 20
    while countdown > 0:
        try:
            data = q.get(timeout=1)
            print(f"Received data from readtime.py: {data}")
            num = int(data)
            countdown += num
            print(f"Remaining time: {countdown} seconds")
        except queue.Empty:
            print("No data received from readtime.py in the last 5 seconds.")
        except ValueError:
            print(f"Invalid data received: {data}")

        countdown -= 1
        time.sleep(1)

    # Countdown is completed, now handle the remaining data in the queue
    while not q.empty():
        data = q.get()
        print(f"Received data from readtime.py after countdown: {data}")
        num = int(data)
        countdown += num
        print(f"Remaining time: {countdown} seconds")

    print("Countdown completed.")


if __name__ == "__main__":
    q = multiprocessing.Queue()
    countdown_process(q)
