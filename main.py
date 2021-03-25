# coding: utf-8
import tkinter
import lang
import AdministrativeManagement.main_menu


def open_am_app():
    main_app.destroy()
    AdministrativeManagement.main_menu.am_app_f()


main_app = tkinter.Tk()
main_app.title("Cinema Management System")
main_app.geometry(f"500x400+{(int(main_app.winfo_screenwidth()) // 2) - (500 //2)}+{(int(main_app.winfo_screenheight()) // 2) - (400 //2)}")
main_app.minsize(300, 250)

tkinter.Button(main_app, padx=40, pady=15, bg='#A12B2D', fg='#fff', text="Administrative Management", font=("Helvetica", 15, "bold"), command=open_am_app).pack(expand=1, padx=10, pady=30)


main_app.mainloop()
