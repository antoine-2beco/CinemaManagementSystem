# coding: utf-8

import tkinter
from tkinter import messagebox
import lang
import sqlite3


def new_room_menu(origin_app):

    def new_room_validation():
        print(room_places_rec.get())
        print(room_vip_places_rec.get())
        if room_name_rec.get() == '' or room_places_rec.get() == '' or room_vip_places_rec.get() == '':
            new_room_error_text.set(lang.new_room_error_empty_entry)
            print(0)
            return

        tkinter.messagebox.askquestion(title=lang.new_room_confirmation_frame_title, message=lang.new_room_confirmation_frame_message)

    new_room_app = tkinter.Toplevel(origin_app)
    new_room_app.grab_set()
    new_room_app.title("Cinema Management System - New Room Menu")
    new_room_app.geometry(f"600x600+{(int(new_room_app.winfo_screenwidth()) // 2) - (600 //2)}+{(int(new_room_app.winfo_screenheight()) // 2) - (600 //2)}")
    new_room_app.resizable(width=False, height=False)

    #  New Room Menu Title
    tkinter.Label(new_room_app, font=("Helvetica", 13, "bold"), text=lang.new_room_menu).pack(pady=20)

    #  New Room Error Message
    new_room_error_text = tkinter.StringVar()
    tkinter.Label(new_room_app, font=("Helvetica", 10, "bold"), fg='#ff0000', textvariable=new_room_error_text).pack(pady=20)

    #  Name Entry Title
    tkinter.Label(new_room_app, font=("Helvetica", 10, "bold"), text=lang.new_room_name).pack()
    room_name_rec = tkinter.StringVar()
    tkinter.Entry(new_room_app, justify='center', textvariable=room_name_rec, width=30).pack(pady=10)

    #  Places Entry Title
    tkinter.Label(new_room_app, font=("Helvetica", 10, "bold"), text=f"\n {lang.new_room_places}").pack()
    room_places_rec = tkinter.IntVar()
    tkinter.Spinbox(new_room_app, from_=1, to=1000, textvariable=room_places_rec).pack(pady=10)

    #  Vip Places Entry Title
    tkinter.Label(new_room_app, font=("Helvetica", 10, "bold"), text=f"\n {lang.new_room_places}").pack()
    room_vip_places_rec = tkinter.IntVar()
    tkinter.Spinbox(new_room_app, from_=1, to=1000, textvariable=room_vip_places_rec).pack(pady=10)

    # Frame Buttons -Validation Button - Annulation Button
    new_room_buttons_frame = tkinter.Frame(new_room_app, width=200, height=100, borderwidth=1)
    tkinter.Button(new_room_buttons_frame, text=lang.new_room_annulation, width=10, height=1, command=new_room_app.destroy).grid(row=0, column=0, padx=10)
    tkinter.Button(new_room_buttons_frame, text=lang.new_room_validation, width=10, height=1, command=new_room_validation).grid(row=0, column=1, padx=10)
    new_room_buttons_frame.pack(pady=40)

    new_room_app.mainloop()
