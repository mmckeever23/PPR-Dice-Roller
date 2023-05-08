from tkinter import *
import random
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.geometry("190x330")
root.title("PPR")
root.configure(background='black') 
root.attributes("-topmost", True)

def roll_dice():
    d1 = random.SystemRandom().randint(1,12)
    d2 = random.SystemRandom().randint(1,12)
    d3 = random.SystemRandom().randint(1,12)
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
red = ImageTk.PhotoImage(Image.open('red.png').resize((72, 72)))
yellow = ImageTk.PhotoImage(Image.open('yellow.png').resize((72, 72)))
blue = ImageTk.PhotoImage(Image.open('blue.png').resize((72, 72)))

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