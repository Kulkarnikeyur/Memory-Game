from tkinter import *
from game.game_state import GameState
from game.card import MemoryGameCard
from game.game_over import check_game_over
import random
import time

def start_game(player_name):

    root = Tk()

    root.title("Memory Game")

    backbutton = PhotoImage(file="photos/background.png")
    mercury = PhotoImage(file="photos/mercury.png")
    venus = PhotoImage(file="photos/venus.png")
    earth = PhotoImage(file="photos/earth.png")
    mars = PhotoImage(file="photos/mars.png")
    jupiter = PhotoImage(file="photos/jupiter.png")
    saturn = PhotoImage(file="photos/saturn.png")
    uranus = PhotoImage(file="photos/uranus.png")
    neptune = PhotoImage(file="photos/neptune.png")

    state = GameState(backbutton)
    state.player_name = player_name

    state.start_time = time.time()

    # Example buttons (you will replace with your board)

    b1 = Button(root, image=backbutton)
    b2 = Button(root, image=backbutton)
    b3 = Button(root, image=backbutton)
    b4 = Button(root, image=backbutton)
    b5 = Button(root, image=backbutton)
    b6 = Button(root, image=backbutton)
    b7 = Button(root, image=backbutton)
    b8 = Button(root, image=backbutton)
    b9 = Button(root, image=backbutton)
    b10 = Button(root, image=backbutton)
    b11 = Button(root, image=backbutton)
    b12 = Button(root, image=backbutton)
    b13 = Button(root, image=backbutton)
    b14 = Button(root, image=backbutton)
    b15 = Button(root, image=backbutton)
    b16 = Button(root, image=backbutton)
    
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)

    b1.grid(row=0, column=0, sticky=NSEW)
    b2.grid(row=0, column=1, sticky=NSEW)
    b3.grid(row=0, column=2, sticky=NSEW)
    b4.grid(row=0, column=3, sticky=NSEW)
    b5.grid(row=1, column=0, sticky=NSEW)
    b6.grid(row=1, column=1, sticky=NSEW)
    b7.grid(row=1, column=2, sticky=NSEW)
    b8.grid(row=1, column=3, sticky=NSEW)
    b9.grid(row=2, column=0, sticky=NSEW)
    b10.grid(row=2, column=1, sticky=NSEW)
    b11.grid(row=2, column=2, sticky=NSEW)
    b12.grid(row=2, column=3, sticky=NSEW)
    b13.grid(row=3, column=0, sticky=NSEW)
    b14.grid(row=3, column=1, sticky=NSEW)
    b15.grid(row=3, column=2, sticky=NSEW)
    b16.grid(row=3, column=3, sticky=NSEW)

    l = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune] * 2
    random.shuffle(l)

    a = MemoryGameCard(b1, l[0],state, lambda s: check_game_over(s, root))
    b = MemoryGameCard(b2, l[1],state, lambda s: check_game_over(s, root))
    c = MemoryGameCard(b3, l[2],state, lambda s: check_game_over(s, root))
    d = MemoryGameCard(b4, l[3],state, lambda s: check_game_over(s, root))
    e = MemoryGameCard(b5, l[4],state, lambda s: check_game_over(s, root))
    f = MemoryGameCard(b6, l[5],state, lambda s: check_game_over(s, root))
    g = MemoryGameCard(b7, l[6],state, lambda s: check_game_over(s, root))
    h = MemoryGameCard(b8, l[7],state, lambda s: check_game_over(s, root))
    i = MemoryGameCard(b9, l[8],state, lambda s: check_game_over(s, root))
    j = MemoryGameCard(b10, l[9],state, lambda s: check_game_over(s, root))
    k = MemoryGameCard(b11, l[10],state, lambda s: check_game_over(s, root))
    Q = MemoryGameCard(b12, l[11],state, lambda s: check_game_over(s, root))
    m = MemoryGameCard(b13, l[12],state, lambda s: check_game_over(s, root))
    N = MemoryGameCard(b14, l[13],state, lambda s: check_game_over(s, root))
    o = MemoryGameCard(b15, l[14],state, lambda s: check_game_over(s, root))
    p = MemoryGameCard(b16, l[15],state, lambda s: check_game_over(s, root))

    b1.configure(command=a.click)
    b2.configure(command=b.click)
    b3.configure(command=c.click)
    b4.configure(command=d.click)
    b5.configure(command=e.click)
    b6.configure(command=f.click)
    b7.configure(command=g.click)
    b8.configure(command=h.click)
    b9.configure(command=i.click)
    b10.configure(command=j.click)
    b11.configure(command=k.click)
    b12.configure(command=Q.click)
    b13.configure(command=m.click)
    b14.configure(command=N.click)
    b15.configure(command=o.click)
    b16.configure(command=p.click)

    root.mainloop()