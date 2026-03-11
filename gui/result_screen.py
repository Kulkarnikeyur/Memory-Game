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

    Label(
            window,
            text=f"Congratulations {state.player_name}!!\n You cracked it",font="times 25 italic",
        ).pack(side="top")

    Label(
            window,
            text=f"score\n Number of moves taken : {state.moves}\n Time taken : {tottime}",font="times 20",
        ).pack(side="top", fill="x")
    
    def go_home():
        window.destroy()
        from gui.dashboard import open_dashboard
        open_dashboard()

    Button(window, text="Home", font="times 20", command=go_home).pack(side="right", expand=TRUE, fill=X, padx=40, ipadx=10, ipady=5)

    def replay():
        window.destroy()
        from gui.game_screen import start_game
        start_game(state.player_name)

    Button(window, text="Replay", font="times 20", command=replay).pack(side="left", expand=True, fill=X, padx=60, ipadx=10, ipady=5)

    window.mainloop()