import tkinter as tk
from tkinter import *
import tkinter.font as font
import time
import random
from PIL import Image, ImageTk, ImageFilter
from functools import partial

# Grupy:
# 0 - 2
# 1 - 3

def ClickGroup(i):
    WrittenText.place_forget()

    # Zapominenie umieszczenia odpowiedniego przycisku grupy
    group_fields[0].grid_forget()
    group_fields[1].grid_forget()
    group_fields[2].grid_forget()
    group_fields[3].grid_forget()

    print(f"Grupa: {i}")
    global letter
    print(f"Litera: {letter}")
    letter+=1
    print(time.time())
    print(time.ctime())
    print("__________________")
    if timeleft0 == 0:
        TimerUp()

    # Funkcja dla przycisku z indeksem 0
    if i == 0:
        # stworzenie okna pierwszej tabeli (i=0)
        Letter0.place(relx=0.5, rely=0.4, anchor=CENTER)
        LetterLoop0()
    elif i == 1:
        Letter1.place(relx=0.5, rely=0.4, anchor=CENTER)
        LetterLoop1()
    elif i == 2:
        Letter2.place(relx=0.5, rely=0.4, anchor=CENTER)
        LetterLoop2()
    else:
        Letter3.place(relx=0.5, rely=0.4, anchor=CENTER)
        LetterLoop3()

def LetterLoop0():
    global i
    if i == 8:
        for i in range(2):
            for j in range(2):
                group_fields[i * 2 + j].grid(row = j, column = i, sticky=W+E)
        Letter0.place_forget()
        WrittenText.place(x=240, y=5)
        global timeleft0
        timeleft0 = 0
        timeLabel.config(text = str(timeleft0))
    else:
        Letter0.config(text=String0[i-1])
        i+=1
        Letter0.after(1000, LetterLoop0)

def LetterLoop1():
    global i
    if i == 7:
        for i in range(2):
            for j in range(2):
                group_fields[i * 2 + j].grid(row = j, column = i, sticky=W+E)
        Letter1.place_forget()
        WrittenText.place(x=240, y=5)
        global timeleft0
        timeleft0 = 0
        timeLabel.config(text = str(timeleft0))
    else:
        Letter1.config(text=String1[i-1])
        i+=1
        Letter1.after(1000, LetterLoop1)

def LetterLoop2():
    global i
    if i == 8:
        for i in range(2):
            for j in range(2):
                group_fields[i * 2 + j].grid(row = j, column = i, sticky=W+E)
        Letter2.place_forget()
        WrittenText.place(x=240, y=5)
        global timeleft0
        timeleft0 = 0
        timeLabel.config(text = str(timeleft0))
    else:
        Letter2.config(text=String2[i-1])
        i+=1
        Letter2.after(1000, LetterLoop2)

def LetterLoop3():
    global i
    if i == 7:
        for i in range(2):
            for j in range(2):
                group_fields[i * 2 + j].grid(row = j, column = i, sticky=W+E)
        Letter3.place_forget()
        WrittenText.place(x=240, y=5)
        global timeleft0
        timeleft0 = 0
        timeLabel.config(text = str(timeleft0))
    else:
        Letter3.config(text=String3[i-1])
        i+=1
        Letter3.after(1000, LetterLoop3)

def TimerUp():
    global timeleft0
    timeleft0 += 1
    timeLabel.config(text = str(timeleft0))
    if timeleft0 < 7:
        timeLabel.after(1000, TimerUp)

String0 = "abcdefg"
String1 = "opqrst"
String2 = "hijklmn"
String3 = "uvwxyz"
global i
i = 0
global letter
letter = 1
timeleft0 = 0

# utworzenie okna tkintera
root = tk.Tk()
root.title('Speller')
root.geometry('1200x800')

# Szablonów czcionek
HugeFont = font.Font(family='Tahoma', size=120)
BigFont = font.Font(family='Tahoma', size=40)
TextFont = font.Font(family='Tahoma', size=20)

# Głównego okna akcji
main_panel = tk.Frame(root, bg="#222222", highlightbackground="blue", highlightthickness=2)
main_panel.place(width=1000, height=700, relx=0.1, y=80)

# Okna grup i klawiatury
main_window = tk.Frame(root, bg="black")
main_window.place(width=840, height=340, relx=0.17, rely=0.2)

# Tytuł
title = Label(root, text="S p e l l e r", pady=0, font=BigFont)
title.place(x=500, y=10)

# Textbox
WrittenText = Text(main_panel, height = 1, width = 39, font=TextFont, bg="navy", fg="white")
WrittenText.insert(INSERT, "Teraz możesz swobodnie mrugać i wybrać grupę")
WrittenText.place(x=240, y=5)

# Grupy liter:
# partial pozwala wysłać zmienną w aktywacji przycisku.
group_fields = [tk.Button(main_window, text="a, b, c, d,\ne, f, g", font=BigFont, bg="white", command=partial(ClickGroup, 0), height=2, width=15), tk.Button(main_window, text="o, p, q,\nr, s, t", font=BigFont, bg="white", command=partial(ClickGroup, 1), height=2, width=15),
tk.Button(main_window, text="h, i, j, k,\nl, m, n", font=BigFont, bg="white", command=partial(ClickGroup, 2), height=2, width=14),
tk.Button(main_window, text="u, v, w,\nx, y, z", font=BigFont, bg="white", command=partial(ClickGroup, 3), height=2, width=14)]
# Ułożenie przycisków grup liter
for i in range(2):
    for j in range(2):
        group_fields[i * 2 + j].grid(row = j, column = i, sticky=W+E)

Letter0 = tk.Label(main_window, text=String0[0], font=HugeFont, fg="white", bg="black")
Letter1 = tk.Label(main_window, text=String1[0], font=HugeFont, fg="white", bg="black")
Letter2 = tk.Label(main_window, text=String2[0], font=HugeFont, fg="white", bg="black")
Letter3 = tk.Label(main_window, text=String3[0], font=HugeFont, fg="white", bg="black")

timeLabel = Label(main_panel, text = str(timeleft0), font = ('Tahoma', 60), bg="white", fg="navy")
timeLabel.place(relx=0.5, rely=0.85)

root.mainloop()
