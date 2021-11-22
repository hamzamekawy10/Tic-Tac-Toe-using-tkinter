from tkinter import *
from tkinter import messagebox

win = Tk()
player1 = "string"
player2 = "string"
turn = player1
win.resizable(False, False)
win.geometry("600x400")

score1 = 0
score2 = 0


def game():
    if a00["text"] == "X" and a01["text"] == "X" and a02["text"] == "X":
        return True
    elif a00["text"] == "O" and a01["text"] == "O" and a02["text"] == "O":
        return True
    elif a10["text"] == "X" and a11["text"] == "X" and a12["text"] == "X":
        return True
    elif a10["text"] == "O" and a11["text"] == "O" and a12["text"] == "O":
        return True
    elif a20["text"] == "X" and a21["text"] == "X" and a22["text"] == "X":
        return True
    elif a20["text"] == "O" and a21["text"] == "O" and a22["text"] == "O":
        return True
    elif a00["text"] == "X" and a11["text"] == "X" and a22["text"] == "X":
        return True
    elif a00["text"] == "O" and a11["text"] == "O" and a22["text"] == "O":
        return True
    elif a02["text"] == "X" and a11["text"] == "X" and a20["text"] == "X":
        return True
    elif a02["text"] == "O" and a11["text"] == "O" and a20["text"] == "O":
        return True
    elif a00["text"] == "X" and a10["text"] == "X" and a20["text"] == "X":
        return True
    elif a00["text"] == "O" and a10["text"] == "O" and a20["text"] == "O":
        return True
    elif a01["text"] == "X" and a11["text"] == "X" and a21["text"] == "X":
        return True
    elif a01["text"] == "O" and a11["text"] == "O" and a21["text"] == "O":
        return True
    elif a02["text"] == "X" and a12["text"] == "X" and a22["text"] == "X":
        return True
    elif a02["text"] == "O" and a12["text"] == "O" and a22["text"] == "O":
        return True
    else:
        return False


def score3():
    if score1 > score2:
        file = open("score", "w")
        file.write(str(score1))
    elif score2 > score1:
        file = open("score", "w")
        file.write(str(score2))
    win.destroy()


win.protocol("WM_DELETE_WINDOW", score3)


def check():
    if a00["text"] != "" and a01["text"] != "" and a02["text"] != "" and a11["text"] != "" and a12["text"] != "" and \
            a20["text"] != "" and a21["text"] != "" and a22["text"] != "":
        messagebox.showinfo(title="draw", message="draw")
        return True
    else:
        return False


def dark_mode():
    if darkvar.get() == 1:
        win['background'] = "black"


darkvar = IntVar()

dark = Checkbutton(win, text="dark mode", command=dark_mode, variable=darkvar)


def clear():
    a00.config(text="")
    a01.config(text="")
    a02.config(text="")
    a10.config(text="")
    a11.config(text="")
    a12.config(text="")
    a20.config(text="")
    a21.config(text="")
    a22.config(text="")
    x.config(text=player1 + " " + str(score1))
    y.config(text=player2 + " " + str(score2))


def e():
    global player1
    global player2
    global turn
    player1 = c.get()
    player2 = g.get()
    turn = player1
    Vline1.place(relx=0.35, rely=0.10)
    Vline2.place(relx=0.65, rely=0.10)
    Hline1.place(relx=0.15, rely=0.30)
    Hline2.place(relx=0.15, rely=0.60)
    a00.place(relx=0.15, rely=0.10, width=115, height=75)
    a01.place(relx=0.37, rely=0.10, width=160, height=75)
    a02.place(relx=0.67, rely=0.10, width=115, height=75)
    a10.place(relx=0.15, rely=0.33, width=115, height=100)
    a11.place(relx=0.37, rely=0.33, width=160, height=95)
    a12.place(relx=0.67, rely=0.33, width=115, height=95)
    a20.place(relx=0.15, rely=0.63, width=115, height=80)
    a21.place(relx=0.37, rely=0.63, width=160, height=80)
    a22.place(relx=0.67, rely=.63, width=115, height=80)
    k.place(relx=0.1, rely=0.85)
    x.pack()
    y.pack()
    d.destroy()


k = Frame(win)
x = Label(k, text=player1 + " " + str(score1))
y = Label(k, text=player2 + " " + str(score2))

a00 = Label(win)
a01 = Label(win)
a02 = Label(win)
a10 = Label(win)
a11 = Label(win)
a12 = Label(win)
a20 = Label(win)
a21 = Label(win)
a22 = Label(win)


def a00play(event):
    global turn
    global score1
    global score2
    if a00["text"] == "":
        if turn == player1:
            a00.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a00.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a00.bind("<Button-1>", a00play)


def a01play(event):
    global turn
    global score1
    global score2
    if a01["text"] == "":
        if turn == player1:
            a01.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a01.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a01.bind("<Button-1>", a01play)


def a02play(event):
    global turn
    global score1
    global score2
    if a02["text"] == "":
        if turn == player1:
            a02.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a02.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a02.bind("<Button-1>", a02play)


def a10play(event):
    global turn
    global score1
    global score2
    if a10["text"] == "":
        if turn == player1:
            a10.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a10.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a10.bind("<Button-1>", a10play)


def a11play(event):
    global turn
    global score1
    global score2
    if a11["text"] == "":
        if turn == player1:
            a11.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a11.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a11.bind("<Button-1>", a11play)


def a12play(event):
    global turn
    global score1
    global score2
    if a12["text"] == "":
        if turn == player1:
            a12.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a12.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()


a12.bind("<Button-1>", a12play)


def a20play(event):
    global turn
    global score1
    global score2
    if a20["text"] == "":
        if turn == player1:
            a20.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a20.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a20.bind("<Button-1>", a20play)


def a21play(event):
    global turn
    global score1
    global score2
    if a21["text"] == "":
        if turn == player1:
            a21.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a21.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a21.bind("<Button-1>", a21play)


def a22play(event):
    global turn
    global score1
    global score2
    if a22["text"] == "":
        if turn == player1:
            a22.config(text="X")
            turn = player2
            if game() == True:
                messagebox.showinfo(title="X won", message=player1 + " won")
                score1 += 1
                clear()
        elif turn == player2:
            a22.config(text="O")
            turn = player1
            if game() == True:
                messagebox.showinfo(title="O won", message=player2 + " won")
                score2 += 1
                clear()
    if check() == True:
        clear()


a22.bind("<Button-1>", a22play)

Vline1 = Frame(win, width=5, height=290, bg="black")
Vline2 = Frame(win, width=5, height=290, bg="black")

Hline1 = Frame(win, width=430, height=5, bg="black")
Hline2 = Frame(win, width=430, height=5, bg="black")

a = Label(win, text="Tic Tac Toe", font=50)
d = Frame(win, bg="yellow")
b = Label(d, text="player 1 name")
c = Entry(d)
f = Label(d, text="player 2 name")
g = Entry(d)
h = Button(d, text="start", command=e)
file = open("score", "r")
z = Label(win, text=file.read())
a.pack()
d.place(relx=0.1, rely=0.05)
b.grid(row=0, column=0)
c.grid(row=0, column=1)
f.grid(row=1, column=0)
g.grid(row=1, column=1)
h.grid(row=2, column=1)
z.place(relx=0.85, rely=0.15)
win.mainloop()
