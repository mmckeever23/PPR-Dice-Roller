from tkinter import *
import random
import tkinter as tk

root = Tk()
root.geometry("190x330")
root.title("PPR")
root.iconbitmap("C:/Users/mmcke/Desktop/Python Tests/PPR-Dice-Roller/baseball.ico")
root.configure(background='black') 
root.attributes("-topmost", True)

def roll_dice():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)
    d3 = random.choice(my_dice)
    if d1 > 9:
        dice_label1.place(x=81, y=86)
    else:
        dice_label1.place(x=86, y=86)
    if d2 > 9:
        dice_label2.place(x=81, y=159)
    else:
        dice_label2.place(x=86, y=159)
    if d3 > 9:
        dice_label3.place(x=81, y=231)
    else:
        dice_label3.place(x=86, y=231)
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)
    dice_label3.config(text=d3)

def key_pressed(event):
    roll_dice()

my_dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
red = tk.PhotoImage(file="C:/Users/mmcke/Desktop/Python Tests/PPR-Dice-Roller/Dice/red.png").subsample(3, 3)
yellow = tk.PhotoImage(file="C:/Users/mmcke/Desktop/Python Tests/PPR-Dice-Roller/Dice/yellow.png").subsample(3, 3)
blue = tk.PhotoImage(file="C:/Users/mmcke/Desktop/Python Tests/PPR-Dice-Roller/Dice/blue.png").subsample(3, 3)

my_frame = Frame(root, bg='black') 
my_frame.pack()
my_frame.focus_set()
my_frame.bind('<Key>', key_pressed)

title = Label(my_frame, text='Pocket Pennant Run\nQuick Dice Roller', font=('Helvetica', 13), fg='white', background="black")
title.grid(row=0, column=0, pady=10)

red_die = tk.Label(root, image=red, bd=0, highlightthickness=0)
red_die.pack()
yellow_die = tk.Label(root, image=yellow, bd=0, highlightthickness=0)
yellow_die.pack()
blue_die = tk.Label(root, image=blue, bd=0, highlightthickness=0)
blue_die.pack()

dice_label1 = Label(root, text=my_dice[0], font=('Helvetica', 15, 'bold'), fg = "white", background="#FF5757", justify="center") 
dice_label2 = Label(root, text=my_dice[1], font=('Helvetica', 15, 'bold'), fg = "black", background="#FFDE59", justify="center") 
dice_label3 = Label(root, text=my_dice[2], font=('Helvetica', 15, 'bold'), fg = "white", background="#5271FF", justify="center") 

title = Label(root, text='Press any key to roll', font=('Helvetica', 10), fg='white', background="black")
title.place(x=36, y=295)

root.mainloop()