import tkinter as tk
import os
from tkinter import *
from tkinter import filedialog, Tk, Label, Button
from tkinter import ttk
from pathlib import Path
from unittest import result
from search_dir import *
from create_list import *
from threading import Thread
win = tk.Tk()
# global variables my_table, selected_folder_to_compare,pb


def gui_start():
    global list_files

    def threading():
        # Call work function
        t1 = Thread(target=start)
        t1.start()

    def insert_values_to_table(save_data):
        #my_table.insert(parent='', index='end', iid=0, text='', values=('1', 'title1', 'Band', 'Bitrate', 'size,', 'Path'))
        counter = 1
        for data in save_data:
            path = data[0]
            artist = data[1]
            title = data[2]
            bitrate = data[3]
            size = data[4]
            my_table.insert(parent='', index='end', iid=counter, text='', values=(
                counter, title, artist, bitrate,  size, path))
            counter += 1

    def start():

        for i in my_table.get_children():
            my_table.delete(i)

        search_folder = search_dir()
        if selected_folder_to_compare != None and selected_folder_to_compare != "":
            list_files = search_folder.search_files(
                str(selected_folder_to_compare))
            duplicate = create_list()
            chceck_duplicate = duplicate.create_dictionary_music(list_files)
            result = duplicate.print_duplicates(chceck_duplicate)
            save_data = duplicate.compare_music(result, progress)
            insert_values_to_table(save_data)

    def select_folder():
        # win.withdraw()
        #global variable
        global selected_folder_to_compare
        selected_folder_to_compare = filedialog.askdirectory()
        selected_folder_bt['text'] = "selected folder:" + \
            str(selected_folder_to_compare)

    def OnDoubleClick(event):
        item = my_table.identify('item', event.x, event.y)

        path = os.path.realpath(my_table.item(item, "value")[5])
        os.startfile(path)
        
    def create_table():
        global my_table

        # creating table
        table_scroll = Scrollbar(result_frame, orient='horizontal')
        table_scroll.pack(side=BOTTOM, fill=X)
        table_scroll = Scrollbar(result_frame, orient='vertical')
        table_scroll.pack(side=RIGHT, fill=Y)

        my_table = ttk.Treeview(
            result_frame, xscrollcommand=table_scroll.set, yscrollcommand=table_scroll.set)
        my_table.pack()
        table_scroll.config(command=my_table.xview)
        table_scroll.config(command=my_table.yview)

        my_table['columns'] = ('number', 'Title', 'Band',
                               'Bitrate', 'size(in KB)', 'Path')
        my_table.column('#0', width=0, stretch=tk.NO)
        my_table.column("number", anchor=tk.CENTER, width=80)
        my_table.column("Title", anchor=tk.CENTER, width=80)
        my_table.column("Band", anchor=tk.CENTER, width=80)
        my_table.column("Bitrate", anchor=tk.CENTER, width=80)
        my_table.column("size(in KB)", anchor=tk.CENTER, width=80)
        my_table.column("Path", anchor=tk.CENTER, width=400)

        # headings
        my_table.heading("#0", text="")
        my_table.heading("number", text="Number", anchor=tk.CENTER)
        my_table.heading("Title", text="Title", anchor=tk.CENTER)
        my_table.heading("Band", text="Band", anchor=tk.CENTER)
        my_table.heading("Bitrate", text="Bitrate", anchor=tk.CENTER)
        my_table.heading("size(in KB)", text="size(in KB)", anchor=tk.CENTER)
        my_table.heading("Path", text="Path", anchor=tk.CENTER)
        my_table.bind("<Double-1>", OnDoubleClick)
        #my_table.insert(parent='', index='end', iid=0, text='', values=('1', 'title1', 'Band', 'Bitrate', 'size,', 'Path'))
    # end

    global progress

    project_name = "MusicDuplicateFinder"

    win.title(project_name)
    win.resizable(0, 0)
    win.minsize(300, 300)
    #win.maxsize(400, 300)

    title = tk.Label(win, text=project_name, font=30, fg="blue")
    title.pack()

    selected_folder_bt = ttk.Button(
        win, text="select folder", command=select_folder)
    # start_thread=Thread(target=start).start()
    start_bt = ttk.Button(win, text="start", command=threading)
    selected_folder_bt.pack()
    start_bt.pack()

    result_frame = tk.Frame(master=win)
    label = tk.Label(master=result_frame, text="Result:")
    progress = ttk.Label(master=result_frame, text="Status:Not started.")
    label.pack()
    progress.pack()
    result_frame.pack()

    create_table()

    win.mainloop()


# start
gui_start()
