from tkinter import *
from tkinter import messagebox

def open_start_screen():

    root = Tk()
    root.title("Enter Name")
    root.geometry("150x130+550+250")
    root.minsize("150", "130")
    root.maxsize("150", "130")

    Label(root, text="Enter your name", font="times 15").pack(side="top")

    Name = StringVar(root)
    entry = Entry(root, textvariable=Name)
    entry.pack(side="top", pady=5)

    def start():
        if Name.get():
            name = Name.get()
            root.destroy()
            from gui.game_screen import start_game
            start_game(name)
        else:
            messagebox.showinfo(title="Error", message="Please enter your name")

    Button(root, text="submit", command=start).pack(side="top")

    root.mainloop()