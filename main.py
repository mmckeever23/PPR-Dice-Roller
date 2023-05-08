from tkinter import *
import random
import tkinter as tk
from PIL import Image, ImageTk
import winsound

root = Tk()
root.geometry("190x370")
root.title("PPR")
root.configure(background='black') 
root.attributes("-topmost", True)

sound_choice = tk.BooleanVar(value="False")

def key_pressed(event):
    roll_dice()
    play_sound()

def sound_toggle():
        sound_choice.set(not sound_choice.get())
        if sound_choice.get() == True:
            button.configure(text="Sound On")
        else:
            button.configure(text="Sound Off")

def play_sound():
    if sound_choice.get() == True:
        winsound.PlaySound("media/roll.wav", winsound.SND_ASYNC)

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
    
    if d1 == d2 and d2 == d3:
        red_die.configure(image=gold, bd=0)
        yellow_die.configure(image=gold, bd=0)
        blue_die.configure(image=gold, bd=0)
        dice_label1.configure(background="#726000")
        dice_label2.configure(fg="white", background="#726000")
        dice_label3.configure(background="#726000")
    else:
        red_die.configure(image=red, bd=0)
        yellow_die.configure(image=yellow, bd=0)
        blue_die.configure(image=blue, bd=0)
        dice_label1.configure(background="#FF5757")
        dice_label2.configure(fg="black", background="#FFDE59")
        dice_label3.configure(background="#5271FF")

my_dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
red = ImageTk.PhotoImage(Image.open('media/red.png').resize((72, 72)))
yellow = ImageTk.PhotoImage(Image.open('media/yellow.png').resize((72, 72)))
blue = ImageTk.PhotoImage(Image.open('media/blue.png').resize((72, 72)))
gold = ImageTk.PhotoImage(Image.open('media/gold.png').resize((72, 72)))

my_frame = Frame(root, bg='black') 
my_frame.pack()
my_frame.focus_set()
my_frame.bind('<Key>', key_pressed)

title = Label(my_frame, text='Pocket Pennant Run\nQuick Dice Roller', font=('Helvetica', 13), fg='white', background="black")
title.grid(row=0, column=0, pady=10)

red_die = tk.Label(root, image=red, bd=0)
red_die.pack()
yellow_die = tk.Label(root, image=yellow, bd=0)
yellow_die.pack()
blue_die = tk.Label(root, image=blue, bd=0)
blue_die.pack()

dice_label1 = Label(root, text=my_dice[0], font=('Helvetica', 15, 'bold'), fg = "white", background="#FF5757", justify="center") 
dice_label2 = Label(root, text=my_dice[1], font=('Helvetica', 15, 'bold'), fg = "black", background="#FFDE59", justify="center") 
dice_label3 = Label(root, text=my_dice[2], font=('Helvetica', 15, 'bold'), fg = "white", background="#5271FF", justify="center") 

title = Label(root, text='Press any key to roll', font=('Helvetica', 10), fg='white', background="black")
title.place(x=33, y=295)
 
button = Button(root, text="Sound Off", bg="black", fg="white", command=sound_toggle)
button.place(x=64, y=330)

root.mainloop()