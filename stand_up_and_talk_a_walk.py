# -*- coding: utf8 -*-
import time
from datetime import datetime
import click
import tkinter as tk
from tkinter import messagebox

# For the health of people who sit for long periods of time, this script will remind you to stand up and take a walk at regular intervals (default each 30 minutes).
# Github: https://github.com/Chiaki2333/stand_up_and_take_a_walk
# Version: 1.1

def remind(root, current_time):
    # 创建置顶的弹出框
    messagebox.showwarning("Stand up and take a walk!", "It is " + current_time + " now.\nIt's time to stand up and take a walk!")
    root.wm_attributes("-topmost", True)  # 将弹出框置顶显示
    root.wm_attributes("-disabled", True)  # 将弹出框置顶显示
    
@click.command()
@click.option("--each", default=30, help="How many minutes do I remind you to stand up and take a walk?(default=30)", type=int)
def main(each):
    # 创建主窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo("Info", "For the health of people who sit for long periods of time, this script will remind you to stand up and take a walk each " + str(each) + " minutes.")
    root.wm_attributes("-topmost", True)  # 将弹出框置顶显示
    root.wm_attributes("-disabled", True)  # 将弹出框置顶显示
    while True:
        tmp = time.time()
        dt_object = datetime.fromtimestamp(tmp)
        current_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
        print("[*]It is " + current_time + " now.")
        print("[*]To avoid you sitting for too long, I will remind you to stand up and take a walk every " + str(each) + " minutes.")
        print("[*]I will remind you at " + datetime.fromtimestamp(tmp+each*60).strftime('%Y-%m-%d %H:%M:%S') +".")
        while time.time()-tmp <= each*60:
            pass
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print("[!]It is " + current_time + " now.\n[!]It's time to stand up and take a walk!")
        remind(root, current_time)
        print("-"*50)

if __name__ == '__main__':
    main()
    
