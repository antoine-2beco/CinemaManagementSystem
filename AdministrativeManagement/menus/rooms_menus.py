# coding: utf-8

import tkinter
import lang
import sqlite3


def new_room_menu(origin_app):
    new_room_app = tkinter.Toplevel(origin_app)
    new_room_app.grab_set()
    new_room_app.title("Cinema Management System - New Room Menu")
    new_room_app.geometry(f"600x600+{(int(new_room_app.winfo_screenwidth()) // 2) - (600 //2)}+{(int(new_room_app.winfo_screenheight()) // 2) - (600 //2)}")
    new_room_app.resizable(width=False, height=False)

    name_entry_title = tkinter.Label(new_room_app, font=("Helvetica", 11, "bold"), text=lang.new_room_name).pack(pady=20)

    room_name = tkinter.Entry(new_room_app, justify='center', width=30).pack()

    new_room_app.mainloop()
