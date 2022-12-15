# PUISSANCE 4
from tkinter import *

e = 80

Player1 = [ # Rouge
    0, # Round
    "#ff0a0a", # Color
]
Player2 = [ # Jaune
    0, # Round
    "#fff70a", # Color
]

def replay():
    isGameStarting = False


round = 0
def click_handler(event):
    # indice du click dans la liste zone
    x = event.x//e
    y = event.y//e
    if x < 8 and y < 6: # On vérif si la pos est bien dans notre tableau
        board.create_oval(x*e,y*e,(x+1)*e,(y+1)*e,fill=Player1[1],width=3)
    print(f"x = {x} / y = {y}")

window = Tk()
window.title("Puissance 4")

board = Canvas(window, height = 500, width = 800)
board.pack()

carreau = [[board.create_rectangle(i*e, j*e, (i+1)*e,(j+1)*e, fill = "#3140AF") for i in range(8)] for j in range(6)]

button_quit = Button(window, text = "ALT F4", bg = "#ff6e8d", width = 20, command = window.destroy)
button_quit.pack()

button_replay = Button(window, text = "REPLAY", bg = "#6ee2ff", width = 20, command = replay)
button_replay.pack()

window.bind("<Button>", click_handler)

isGameStarting = False

Winner = False

zone = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

zonePos = [
    [0, 0, 0, 0, 0, 0, 0],
]


# OUVERTURE DE LA FENETRE DE JEU
window.mainloop()
