from tkinter import *
import random
import tkinter as tk
from PIL import Image, ImageTk
import winsound

# Application Properties
root = Tk()
root.geometry("192x360")
root.title("PPR")
root.iconbitmap('media/logo.ico')
root.configure(background='black') 
root.attributes("-topmost", True)

# Functions
def key_pressed(event):
    if event.keysym == 'space':
        roll_dice()

def sound_toggle():
        sound_choice.set(not sound_choice.get())
        if sound_choice.get() == True:
            button.configure(text="Sound On")
        else:
            button.configure(text="Sound Off")

def play_roll_sound():
    if sound_choice.get() == True:
        winsound.PlaySound("media/roll.wav", winsound.SND_ASYNC)

def play_rare_sound():
    if sound_choice.get() == True:
        winsound.PlaySound("media/rare.wav", winsound.SND_ASYNC)

def roll_dice(): 
    d1 = random.SystemRandom().randint(1,12)
    d2 = random.SystemRandom().randint(1,12)
    d3 = random.SystemRandom().randint(1,12)
    dice_label1.config(text=d1)
    dice_label2.config(text=d2)
    dice_label3.config(text=d3)
    
    if d1 == d2 and d2 == d3:
        red_die.configure(image=green, bd=0)
        yellow_die.configure(image=green, bd=0)
        blue_die.configure(image=green, bd=0)
        dice_label1.configure(background="#398845")
        dice_label2.configure(fg="white", background="#398845")
        dice_label3.configure(background="#398845")
        play_rare_sound()
    else:
        red_die.configure(image=red, bd=0)
        yellow_die.configure(image=yellow, bd=0)
        blue_die.configure(image=blue, bd=0)
        dice_label1.configure(background="#FF5757")
        dice_label2.configure(fg="black", background="#FFDE59")
        dice_label3.configure(background="#5271FF")
        play_roll_sound()

    if d1 > 9:
        dice_label1.place(x=81, y=86)
    else:
        dice_label1.place(x=87, y=86)
    if d2 > 9:
        dice_label2.place(x=81, y=159)
    else:
        dice_label2.place(x=87, y=159)
    if d3 > 9:
        dice_label3.place(x=81, y=231)
    else:
        dice_label3.place(x=87, y=231)

# Frame Properties
my_frame = Frame(root, bg='black') 
my_frame.pack()
my_frame.focus_set()
my_frame.bind('<Key>', key_pressed)

# Global Variables
sound_choice = tk.BooleanVar(value="False")
my_dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
red = ImageTk.PhotoImage(Image.open('media/red.png').resize((72, 72)))
yellow = ImageTk.PhotoImage(Image.open('media/yellow.png').resize((72, 72)))
blue = ImageTk.PhotoImage(Image.open('media/blue.png').resize((72, 72)))
green = ImageTk.PhotoImage(Image.open('media/green.png').resize((72, 72)))

# Page Title
title = Label(my_frame, text='Pocket Pennant Run\nQuick Dice Roller', font=('', 13), fg='white', background="black")
title.grid(row=0, column=0, pady=10)

# Dice and Dice Labels
red_die = tk.Label(root, image=red, bd=0)
red_die.pack()
yellow_die = tk.Label(root, image=yellow, bd=0)
yellow_die.pack()
blue_die = tk.Label(root, image=blue, bd=0)
blue_die.pack()
dice_label1 = Label(root, text=my_dice[0], font=('', 15, 'bold'), fg = "white", background="#FF5757", justify="center") 
dice_label2 = Label(root, text=my_dice[1], font=('', 15, 'bold'), fg = "black", background="#FFDE59", justify="center") 
dice_label3 = Label(root, text=my_dice[2], font=('', 15, 'bold'), fg = "white", background="#5271FF", justify="center") 

title = Label(root, text='Press space bar to roll', font=('', 10), fg='white', background="black", justify="center", anchor='center', pady=10).pack()

button = Button(root, text="Sound Off", bg="black", fg="white", command=sound_toggle)
button.place(x=64, y=320)

root.resizable(width=False, height=False)
root.mainloop()