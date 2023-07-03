from tkinter import*
from tkinter import messagebox


def login():
    username = entry1.get()
    password = entry2.get()

    if (username == "" and password==""):
        messagebox.showinfo("", "Blank not allowed")

    elif (username == "Jude" and password=="123"):
        messagebox.showinfo("", "Login Success")

    else:
        messagebox.showinfo("", "Username & password not valid")


root = Tk()
root.title("Login")
root.geometry("450x300")

global entry1
global entry2

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

entry1 = Entry(root, bd=3)
entry1.place(x=140, y=20)

entry2 = Entry(root, bd=3)
entry2.place(x=140, y=70)

Button(root, text="Login", command=login, height=3, width=13, bd=5).place(x=100, y=120)

root.mainloop()

