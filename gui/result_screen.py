from tkinter import *
from game.score_manager import save_score
import datetime

def show_result_screen(state):

    tottime = str(datetime.timedelta(seconds=state.end_time-state.start_time))[2:7]

    save_score(state.player_name, state.moves, tottime)

    window = Tk()

    window.geometry("630x350+400+150")
    window.minsize("630", "350")
    window.maxsize("630", "350")

    # window.bg = PhotoImage(file="photos/main_background.png")
    # bg_label = Label(window, image=window.bg)
    # bg_label.place(relwidth=1, relheight=1)

    Label(
            window,
            text=f"🎉 Congratulations {state.player_name} 🎉\n You cracked it",font="times 25 italic",
        ).place(relx=0.5, rely=0.10, anchor="center")

    Label(
            window,
            text=f"Moves Taken : {state.moves}\n Time Taken : {tottime}",font="times 20",
        ).place(relx=0.5, rely=0.40, anchor="center")
    
    def go_home():
        window.destroy()
        from gui.dashboard import open_dashboard
        open_dashboard()

    def replay():
        window.destroy()
        from gui.game_screen import start_game
        start_game(state.player_name)


    # Button(window, text="Home", font="times 20", command=go_home).pack(side="right", expand=TRUE, fill=X, padx=40, ipadx=10, ipady=5)


    # Button(window, text="Replay", font="times 20", command=replay).pack(side="left", expand=True, fill=X, padx=60, ipadx=10, ipady=5)

    # Button Style
    btn_style = {
        "font": ("Arial", 16, "bold"),
        "width": 12,
        "height": 2,
        "bg": "#1f2a44",
        "fg": "white",
        "bd": 0,
        "activebackground": "#2e3f66",
        "cursor": "hand2"
    }

    def on_enter(e):
        e.widget["bg"] = "#3b5998"

    def on_leave(e):
        e.widget["bg"] = "#1f2a44"

    # Buttons
    replay_btn = Button(window, text="Replay", **btn_style, command=replay)
    replay_btn.place(relx=0.35, rely=0.75, anchor="center")

    home_btn = Button(window, text="Home", **btn_style, command=go_home)
    home_btn.place(relx=0.65, rely=0.75, anchor="center")

    # Hover effect
    for btn in [replay_btn, home_btn]:
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
    window.mainloop()