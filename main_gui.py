import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
project_name = "MusicDuplicateFinder"
win = tk.Tk()
win.title(project_name)
win.resizable(0, 0)
win.minsize(320, 200)


def select_folder():
    #win.withdraw()
    folder_selected = filedialog.askdirectory()
    print(folder_selected)
    

def start():
    print("started")


title = tk.Label(win, text=project_name, font=30, fg="blue")
title.pack()

selected_folder_bt = ttk.Button(win, text="select folder", command=select_folder)
start_bt = ttk.Button(win, text="start", command=start)
selected_folder_bt.pack()
start_bt.pack()


win.mainloop()
