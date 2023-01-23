from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Puissance 4")

e = 80

# https://www.colorhexa.com/
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

def getPlayer(args):
    if args == 1:
        ply = "rouge"
    else:
        ply = "jaune"
    return ply


def replay():
    board.delete("all")
    carreau = [[board.create_rectangle(i*e, j*e, (i+1)*e,(j+1)*e, fill = "#3140AF") for i in range(7)] for j in range(6)]
    global tab
    tab = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
    round = 0


round = 0
def click_handler(pos):
    global round
    x = pos.x//e
    y = 5 # nb de colonnes
    Find = False
    if x < 7 and y < 6: # On vérif si la pos est bien dans notre tableau
        while (not Find):
            if y < 0:
                print("La colonne est remplie !")
                Find = True
            else:
                if tab[y][x] == 0:
                    Find = True
                    if round % 2 == 0: # joueur 1 ou 2 (en fonction du round)
                        board.create_oval(x*e,y*e,(x+1)*e,(y+1)*e,fill=Player[0][1],width=3)
                        tab[y][x] = 1
                    else:
                        board.create_oval(x*e,y*e,(x+1)*e,(y+1)*e,fill=Player[1][1],width=3)
                        tab[y][x] = 2
                    round += 1
                else:
                    y -= 1

    if check_win():
        return
    print(f"x = {x} / y = {y}")
    print(tab)


def check_win():
    # check rows
    for row in tab:
        for i in range(4):
            if row[i] != 0 and row[i] == row[i+1] == row[i+2] == row[i+3]:
                action = messagebox.askyesno("Partie terminée !", f"Le joueur {getPlayer(row[i])} a gagné ! Rejouer ?")
                if (action):
                    replay()
                else:
                    window.destroy()
                return True

    # check columns
    for col in range(7):
        for row in range(3):
            if tab[row][col] != 0 and tab[row][col] == tab[row+1][col] == tab[row+2][col] == tab[row+3][col]:
                action = messagebox.askyesno("Partie terminée !", f"Le joueur {getPlayer(tab[row][col])} a gagné ! Rejouer ?")
                if (action):
                    replay()
                else:
                    window.destroy()
                return True

    # check diagonal (top-left to bottom-right)
    for row in range(3):
        for col in range(4):
            if tab[row][col] != 0 and tab[row][col] == tab[row+1][col+1] == tab[row+2][col+2] == tab[row+3][col+3]:
                action = messagebox.askyesno("Partie terminée !", f"Le joueur {getPlayer(tab[row][col])} a gagné ! Rejouer ?")
                if (action):
                    replay()
                else:
                    window.destroy()
                return True

    # check diagonal (bottom-left to top-right)
    for row in range(3):
        for col in range(4):
            if tab[row+3][col] != 0 and tab[row+3][col] == tab[row+2][col+1] == tab[row+1][col+2] == tab[row][col+3]:
                action = messagebox.askyesno("Partie terminée !", f"Le joueur {getPlayer(tab[row+3][col])} a gagné ! Rejouer ?")
                if (action):
                    replay()
                else:
                    window.destroy()
                return True
    return False



board = Canvas(window, height = 500, width = 800)
board.pack()

carreau = [[board.create_rectangle(i*e, j*e, (i+1)*e,(j+1)*e, fill = "#3140AF") for i in range(7)] for j in range(6)]

button_quit = Button(window, text = "ALT F4", bg = "#ff6e8d", width = 30, command = window.destroy)
button_quit.pack()

button_replay = Button(window, text = "REPLAY", bg = "#6ee2ff", width = 30, command = replay)
button_replay.pack()

window.bind("<Button>", click_handler)

window.mainloop()   
