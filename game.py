# PUISSANCE 4
from tkinter import *

e = 80

Player = [
    ["Joueur Rouge", "#ff0a0a"],
    ["Joueur Jaune", "#fff70a"]
]

tab = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

def replay():
    isGameStarting = False


round = 0
def click_handler(pos):
    global round
    global findPlayer1
    global findPlayer2
    # indice du click dans la liste zone
    x = pos.x//e
    column = 5
    y=column
    Find = False
    if x < 7 and y < 6: # On vérif si la pos est bien dans notre tableau
        if round % 2 == 0:
            while (not Find):
                if y < 0:
                    print("La colonne est remplie !")
                    Find = True
                else:
                    if tab[y][x] == 0:
                        Find = True
                        board.create_oval(x*e,y*e,(x+1)*e,(y+1)*e,fill=Player[0][1],width=3)
                        tab[y][x] = 1
                        round += 1
                    else:
                        y -= 1
        else:
            while (not Find):
                if y < 0:
                    print("La colonne est remplie !")
                    Find = True
                else:
                    if tab[y][x] == 0:
                        Find = True
                        board.create_oval(x*e,y*e,(x+1)*e,(y+1)*e,fill=Player[1][1],width=3)
                        tab[y][x] = 2
                        round += 1
                    else:
                        y -= 1
    print(f"x = {x} / y = {y}")
    print(tab)

window = Tk()
window.title("Puissance 4")

board = Canvas(window, height = 500, width = 800)
board.pack()

carreau = [[board.create_rectangle(i*e, j*e, (i+1)*e,(j+1)*e, fill = "#3140AF") for i in range(7)] for j in range(6)]

button_quit = Button(window, text = "ALT F4", bg = "#ff6e8d", width = 20, command = window.destroy)
button_quit.pack()

button_replay = Button(window, text = "REPLAY", bg = "#6ee2ff", width = 20, command = replay)
button_replay.pack()

window.bind("<Button>", click_handler)

isGameStarting = False

Winner = False

zonePosX = [
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 4, 5, 6],
]

zonePosY = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5],
]


# OUVERTURE DE LA FENETRE DE JEU
window.mainloop()
