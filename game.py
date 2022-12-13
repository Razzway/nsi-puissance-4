# PUISSANCE 4
from tkinter import *

e = 50

def replay():
    isGameStarting = False

def click_handler(event):
    coords_x = event.x
    coords_y = event.y
    print(f"x = {event.x} / y = {event.y}")

window = Tk()
window.title("Puissance 4")

board = Canvas(window, height = 500, width = 800)
board.pack()

button_quit = Button(window, text = "ALT F4", bg = "green", width = 20, command = window.destroy)
button_quit.pack()

button_replay = Button(window, text = "REPLAY", bg = "red", width = 20, command = replay)
button_replay.pack()

carreau = [[board.create_rectangle(i*e, j*e, (i+1)*e,(j+1)*e, fill = "#3140AF") for i in range(10)] for j in range(10)]

window.bind("<Button>", click_handler)

isGameStarting = False

Tour = 0
Player1 = 0
Player2 = 0
Winner = False

zone = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


# OUVERTURE DE LA FENETRE DE JEU
window.mainloop()