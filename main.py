from tkinter import *
import random

root = Tk()
root.geometry("200x275")
root.configure(background='black') 

def roll_dice():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)
    d3 = random.choice(my_dice)
    
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)
    dice_label3.config(text=d3)

def key_pressed(event):
    roll_dice()

my_dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

my_frame = Frame(root, bg='black')
my_frame.pack()
my_frame.focus_set()

my_frame.bind('<Key>', key_pressed)

title = Label(my_frame, text='Pocket Pennant Run\nQuick Dice Roller', font=('Helvetica', 15), fg='white', background="black")
title.grid(row=0, column=0, pady=10)

dice_label1 = Label(my_frame, text=my_dice[0], font=('Helvetica', 25), fg = "red", background="black") 
dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, text=my_dice[1], font=('Helvetica', 25), fg = "yellow", background="black") 
dice_label2.grid(row=2, column=0)

dice_label3 = Label(my_frame, text=my_dice[2], font=('Helvetica', 25), fg = "blue", background="black") 
dice_label3.grid(row=3, column=0)

title = Label(my_frame, text='Press any key to roll', font=('Helvetica', 10), fg='white', background="black")
title.grid(row=4, column=0, pady=10)

roll_dice()

root.mainloop()


