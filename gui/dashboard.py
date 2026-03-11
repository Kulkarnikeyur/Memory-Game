from tkinter import *
from gui.start_screen import open_start_screen
from gui.history_screen import open_history_screen


def open_dashboard():

    root = Tk()
    root.title("Memory Game")
    root.geometry("1000x560+150+90")
    root.minsize("1000", "560")
    root.maxsize("1000", "560")

    root.bg = PhotoImage(file="photos/main_background.png")

    Label(root, image=root.bg).place(x=0, y=0)

    Label(
        root, text="Planetary Pairs", font="times 25 italic ", background="white"
    ).pack(side="top", ipadx=50, ipady=20, pady=100)

    def start():
        root.destroy()
        open_start_screen()

    def history():
        root.destroy() 
        open_history_screen()

    
    Button(
        root, text="New Game", font="times 15 bold", background="white", command=start
    ).pack(side="left", expand=True, fill=X, padx=100, ipadx=20, ipady=10)

    Button(
        root, text="View History", font="times 15 bold", background="white", command=history
    ).pack(side="right", expand=TRUE, fill=X, padx=80, ipadx=20, ipady=10)

    Button(
        root, text="exit", font="times 15 bold", background="white", command=root.destroy
    ).pack(side="bottom", expand=True, fill=X, padx=100, ipadx=20, ipady=10)


    root.mainloop()