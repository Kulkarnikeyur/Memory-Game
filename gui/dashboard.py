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
        root,
        text="Planetary Pairs",
        font=("Times", 36, "italic"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.2, anchor="center")

    def start():
        root.destroy()
        open_start_screen()

    def history():
        root.destroy() 
        open_history_screen()

    
    # ---------------- BUTTON STYLE ----------------
    btn_style = {
        "font": ("Times", 16, "bold"),
        "width": 15,
        "height": 2,
        "bg": "#1f2a44",
        "fg": "white",
        "bd": 0,
        "activebackground": "#2e3f66",
        "activeforeground": "white",
        "cursor": "hand2"
    }

    def on_enter(e):
        e.widget["bg"] = "#3b5998"

    def on_leave(e):
        e.widget["bg"] = "#1f2a44"


    new_game = Button(root, text="New Game", command=start, **btn_style)
    new_game.place(relx=0.3, rely=0.65, anchor="center")

    history_btn = Button(root, text="View History", command=history, **btn_style)
    history_btn.place(relx=0.7, rely=0.65, anchor="center")

    exit_btn = Button(root, text="Exit", command=root.destroy, **btn_style)
    exit_btn.place(relx=0.5, rely=0.8, anchor="center")


    for btn in [new_game, history_btn, exit_btn]:
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    root.mainloop()