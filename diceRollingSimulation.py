from tkinter import *
from random import randint


dice_unicode = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

root = Tk()
root.title("Dice Rolling Simulation")

dice_label = Label(root, text=dice_unicode[0], font=('Times', 100), foreground='#DC143C', background="#EEEEEE")
dice_label.grid(row=0, column=0, padx=25, pady=5)

def rollDice():
    i = randint(1, 6)
    new_dice_label = Label(root, text=dice_unicode[i], font=('Times', 100), foreground='#DC143C', background="#EEEEEE", width=2)
    new_dice_label.grid(row=0, column=0, padx=25, pady=5)

roll_btn = Button(root, text="Roll the Dice", command=rollDice, foreground='#DC143C', background="#EEEEEE")
roll_btn.grid(row=1, column=0)

if __name__ == "__main__":
    root.mainloop()