import tkinter as tk
from tkinter import messagebox
import threading
import time


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("倒计时窗口")

        self.timers = [
            {"name": "1号机器人", "remaining_time": 0, "running": False},
            {"name": "2号机器人", "remaining_time": 0, "running": False},
            {"name": "3号机器人", "remaining_time": 0, "running": False},
        ]

        self.create_widgets()

    def create_widgets(self):
        self.timer_labels = []
        for timer in self.timers:
            label = tk.Label(self.root, text=f"{timer['name']}剩余时间：正在倒计时间")
            label.pack(anchor="w")
            self.timer_labels.append(label)

        self.start_buttons = []
        self.pause_buttons = []
        self.add_time_entries = []
        self.add_time_buttons = []  # 添加此列表来保存“增加时间”按钮

        for timer in self.timers:
            frame = tk.Frame(self.root)
            frame.pack(anchor="w")

            start_button = tk.Button(frame, text="启动", command=lambda t=timer: self.start_timer(t))
            start_button.pack(side="left", padx=5)
            self.start_buttons.append(start_button)

            pause_button = tk.Button(frame, text="暂停", command=lambda t=timer: self.pause_timer(t))
            pause_button.pack(side="left", padx=5)
            self.pause_buttons.append(pause_button)

            add_time_entry = tk.Entry(frame)
            add_time_entry.pack(side="left", padx=5)
            self.add_time_entries.append(add_time_entry)

            add_time_button = tk.Button(frame, text="增加时间", command=lambda t=timer: self.add_time(t))
            add_time_button.pack(side="left", padx=5)
            self.add_time_buttons.append(add_time_button)  # 将“增加时间”按钮添加到列表中

    def start_timer(self, timer):
        if not timer['running']:
            timer['running'] = True
            remaining_time = timer['remaining_time']
            if remaining_time <= 0:
                remaining_time = 10  # 默认初始时间为10秒
            self.update_timer_label(timer, f"{timer['name']}剩余时间：{remaining_time}秒")
            self.start_buttons[self.timers.index(timer)].config(state=tk.DISABLED)
            self.pause_buttons[self.timers.index(timer)].config(state=tk.NORMAL)
            self.add_time_entries[self.timers.index(timer)].config(state=tk.DISABLED)
            self.countdown(timer, remaining_time)

    def countdown(self, timer, remaining_time):
        while timer['running'] and remaining_time > 0:
            self.update_timer_label(timer, f"{timer['name']}剩余时间：{remaining_time}秒")
            time.sleep(1)
            remaining_time -= 1
        if timer['running']:
            timer['remaining_time'] = remaining_time
            self.update_timer_label(timer, f"{timer['name']}剩余时间：正在倒计时间")
            self.start_buttons[self.timers.index(timer)].config(state=tk.NORMAL)
            self.pause_buttons[self.timers.index(timer)].config(state=tk.DISABLED)
            self.add_time_entries[self.timers.index(timer)].config(state=tk.NORMAL)

    def pause_timer(self, timer):
        timer['running'] = False
        self.start_buttons[self.timers.index(timer)].config(state=tk.NORMAL)
        self.pause_buttons[self.timers.index(timer)].config(state=tk.DISABLED)
        self.add_time_entries[self.timers.index(timer)].config(state=tk.NORMAL)

    def add_time(self, timer):
        if not timer['running']:
            try:
                added_time = int(self.add_time_entries[self.timers.index(timer)].get())
                timer['remaining_time'] += added_time
                self.update_timer_label(timer, f"{timer['name']}剩余时间：{timer['remaining_time']}秒")
                self.add_time_entries[self.timers.index(timer)].delete(0, tk.END)
            except ValueError:
                messagebox.showerror("错误", "请输入有效的时间。")

    def update_timer_label(self, timer, text):
        self.timer_labels[self.timers.index(timer)].config(text=text)


def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
