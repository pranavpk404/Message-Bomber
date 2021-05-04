import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter import StringVar
from pyautogui import typewrite
from time import sleep

root = tk.Tk()
style = ThemedStyle(root)
style.set_theme("black")
root.geometry("500x120")
root.wm_iconbitmap("icon.ico")
root.resizable(False, False)
root.title("Message Bomber")
root.config(bg="black")

def brain():

    x = int(Times.get())

    sleep(2)
    while True:
        typewrite(message.get())
        sleep(.600)
        typewrite("\n")

        x = x - 1

        if x == 0:
            break


def Widgets():
    ttk.Label(root, text="message :").grid(row=1, column=0, pady=5, padx=5)
    ttk.Entry(root, width=55, textvariable=message).grid(row=1, column=1, pady=5, padx=5, columnspan=2)
    ttk.Label(root, text="times :").grid(row=2, column=0, pady=5, padx=5)
    ttk.Entry(root, width=40, textvariable=Times).grid(row=2, column=1, pady=5, padx=5)
    ttk.Button(root, text="Start", command=brain).grid(row=3, column=1, pady=3, padx=3)


message = StringVar()
Times = StringVar()
Widgets()
root.mainloop()
