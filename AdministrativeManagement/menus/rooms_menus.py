# coding: utf-8
import tkinter
from tkinter import messagebox
import lang
import sqlite3

import main_menu


def new_room_menu(origin_app):

    def new_room_validation():
        if '' in (room_name_rec.get(), room_places_rec.get(), room_vip_places_rec.get()):
            new_room_error_text.set(lang.new_room_error_empty_entry)
            return

        new_room_confirmation_askquestion_rec = tkinter.messagebox.askquestion(title=lang.new_room_confirmation_frame_title, message=lang.new_room_confirmation_frame_message.format(room_name_rec.get()), icon='warning')
        if new_room_confirmation_askquestion_rec == 'yes':
            try:
                db_con = sqlite3.connect('database.db')
                db_cur = db_con.cursor()

                db_elements = (db_cur.lastrowid, room_name_rec.get(), room_places_rec.get(), room_vip_places_rec.get(),)
                db_cur.execute("INSERT INTO cms_rooms VALUES(?, ?, ?, ?)", db_elements)
                db_con.commit()

            except Exception as e:
                db_con.rollback()
                tkinter.messagebox.showwarning(title=lang.db_error_frame_title, message=lang.db_error_frame_message.format(e))
                return

            finally:
                db_con.close()
                new_room_app.destroy()
                return


    new_room_app = tkinter.Toplevel(origin_app)
    new_room_app.grab_set()
    new_room_app.title("Cinema Management System - New Room Menu")
    new_room_app.geometry(f"600x450+{(int(new_room_app.winfo_screenwidth()) // 2) - (600 //2)}+{(int(new_room_app.winfo_screenheight()) // 2) - (450 //2)}")
    new_room_app.resizable(width=False, height=False)

    #  New Room Menu Title
    tkinter.Label(new_room_app, font=("Helvetica", 14, "bold"), text=lang.new_room_menu).pack(pady=20)

    #  New Room Error Message
    new_room_error_text = tkinter.StringVar()
    tkinter.Label(new_room_app, font=("Helvetica", 9, "bold"), fg='#ff0000', textvariable=new_room_error_text).pack()

    #  Name Entry Title
    tkinter.Label(new_room_app, font=("Helvetica", 10, "bold"), text=lang.new_room_name).pack()
    room_name_rec = tkinter.StringVar()
    tkinter.Entry(new_room_app, justify='center', textvariable=room_name_rec, width=30).pack(pady=10)

    #  Places Entry Title
    tkinter.Label(new_room_app, font=("Helvetica", 10, "bold"), text=f"\n {lang.new_room_places}").pack()
    room_places_rec = tkinter.StringVar()
    tkinter.Spinbox(new_room_app, from_=1, to=1000, textvariable=room_places_rec).pack(pady=10)

    #  Vip Places Entry Title
    tkinter.Label(new_room_app, font=("Helvetica", 10, "bold"), text=f"\n {lang.new_room_places}").pack()
    room_vip_places_rec = tkinter.StringVar()
    tkinter.Spinbox(new_room_app, from_=1, to=1000, textvariable=room_vip_places_rec).pack(pady=10)

    #  Frame Buttons -Validation Button - Annulation Button
    new_room_buttons_frame = tkinter.Frame(new_room_app, width=200, height=100, borderwidth=1)
    tkinter.Button(new_room_buttons_frame, text=lang.new_room_annulation, width=10, height=1, command=new_room_app.destroy).grid(row=0, column=0, padx=10)
    tkinter.Button(new_room_buttons_frame, text=lang.new_room_validation, width=10, height=1, command=new_room_validation).grid(row=0, column=1, padx=10)
    new_room_buttons_frame.pack(pady=40)

    new_room_app.mainloop()


def remove_room_menu(origin_app):

    def remove_room_validation():
        new_room_confirmation_askquestion_rec = tkinter.messagebox.askquestion(title=lang.new_room_confirmation_frame_title, message=lang.new_room_confirmation_frame_message.format(room_name_rec.get()), icon='warning')
        if new_room_confirmation_askquestion_rec == 'yes':
            try:
                db_con = sqlite3.connect('database.db')
                db_cur = db_con.cursor()

                db_elements = (room_selection_rec.get(),)
                db_cur.execute("DELETE FROM cms_rooms WHERE (?)", db_elements)
                db_con.commit()

            except Exception as e:
                db_con.rollback()
                tkinter.messagebox.showwarning(title=lang.db_error_frame_title, message=lang.db_error_frame_message.format(e))
                return

            finally:
                db_con.close()
                new_room_app.destroy()
                return

    remove_room_app = tkinter.Toplevel(origin_app)
    remove_room_app.grab_set()
    remove_room_app.title("Cinema Management System - Remove Room Menu")
    remove_room_app.geometry(f"600x450+{(int(remove_room_app.winfo_screenwidth()) // 2) - (600 // 2)}+{(int(remove_room_app.winfo_screenheight()) // 2) - (450 // 2)}")
    remove_room_app.resizable(width=False, height=False)

    #  Remove Room Menu Title
    tkinter.Label(remove_room_app, font=("Helvetica", 14, "bold"), text=lang.remove_room_menu).pack(pady=20)

    #  New Room Error Message
    new_room_error_text = tkinter.StringVar()
    tkinter.Label(remove_room_app, font=("Helvetica", 9, "bold"), fg='#ff0000', textvariable=new_room_error_text).pack()

    #  Room Selection Entry Title
    tkinter.Label(remove_room_app, font=("Helvetica", 10, "bold"), text=lang.remove_room_room_selection).pack()
    room_selection_rec = tkinter.StringVar()
    tkinter.Combobox(remove_room_app, justify='left', values=main_menu.get_all_rooms(), textvariable=room_selection_rec, width=30).pack(pady=10)

    #  Frame Buttons -Validation Button - Annulation Button
    remove_room_buttons_frame = tkinter.Frame(remove_room_app, width=200, height=100, borderwidth=1)
    tkinter.Button(remove_room_buttons_frame, text=lang.remove_room_validation, width=10, height=1, command=remove_room_app.destroy).grid(row=0, column=0, padx=10)
    tkinter.Button(remove_room_buttons_frame, text=lang.remove_room_annulation, width=10, height=1, command=remove_room_validation).grid(row=0, column=1, padx=10)
    new_room_buttons_frame.pack(pady=40)
