# coding: utf-8
import tkinter
import lang
import sqlite3

import AdministrativeManagement.menus.rooms_menus

def get_all_rooms():
    try:
        db_room_con = sqlite3.connect('database.db')
        db_room_cur = db_room_con.cursor()
        db_room_cur.execute("SELECT * FROM cms_rooms")
        cms_rooms = db_room_cur.fetchall()

    except Exception as e:
        print(e)
        db_room_con.rollback()

    finally:
        db_room_con.close()
    return cms_rooms

def apps_opening(origin_app, destination_app):
    def open_app():
        if destination_app == 'new_room_menu':
            origin_app.wait_window(AdministrativeManagement.menus.rooms_menus.new_room_menu(origin_app))

    return open_app


def am_app_f():
    am_app = tkinter.Tk()
    am_app.title("Cinema Management System - Administrative Management")
    am_app.geometry('800x600')
    am_app.minsize(600, 500)

    am_mm = tkinter.Menu(am_app)

    # Room Management
    room_menu = tkinter.Menu(am_mm, tearoff=0)
    am_mm.add_cascade(label=lang.room_menu, menu=room_menu)
    room_menu.add_command(label=lang.new_room, command=apps_opening(am_app, 'new_room_menu'))
    room_menu.add_command(label=lang.remove_room)
    room_menu.add_separator()

    for room in get_all_rooms():
        room_menu.add_command(label=f"[{room[0]}] {room[1]}")

    am_app.config(menu=am_mm)
    am_app.mainloop()
