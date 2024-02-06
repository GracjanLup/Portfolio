import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
import random
import os

def start0():
    timeLabel.place(x=540, y=80)
    if timeleft0 == 60:
        TimerDown0()
    EyeGame()

def GameStart():
    global wygrane, przegrane, suma
    StartButton.pack_forget()
    ZostajeButton.place_forget()
    DobieramButton.place_forget()
    WartoscKarty.config(text="")
    DobraneKarty.config(text="")
    GameInfo3.config(text="")
    info2.config(text="Czas na zapoznanie się skończył!")
    GameInfo.config(text=f"Końcowy bilans to badany = {wygrane}, komputer = {przegrane}")
    wygrane, przegrane = reducefract(wygrane, przegrane)
    ZaoWygrane = int(wygrane)
    ZaoPrzegrane = int(przegrane)
    GameInfo2.config(text=f"Stosunek wygranych do przegranych to {ZaoWygrane}:{ZaoPrzegrane}")
    wygrane = 0
    przegrane = 0
    suma = 0
    karty.clear()
    StartButton.config(text="Zacznij część właściwą", command=lambda:[StartButton.pack_forget(), start1()])
    StartButton.pack()

def start1():
    global wygrane, przegrane
    timeLabel.place(x=540, y=80)
    if timeleft == 120:
        TimerDown()
    EyeGame()

def GameFin():
    global wygrane, przegrane
    StartButton.pack_forget()
    ZostajeButton.place_forget()
    DobieramButton.place_forget()
    WartoscKarty.config(text="")
    DobraneKarty.config(text="")
    GameInfo3.config(text="")
    info2.config(text="Czas się skończył!")
    GameInfo.config(text=f"Końcowy bilans to badany = {wygrane}, komputer = {przegrane}")
    wygrane, przegrane = reducefract(wygrane, przegrane)
    ZaoWygrane = int(wygrane)
    ZaoPrzegrane = int(przegrane)
    GameInfo2.config(text=f"Stosunek wygranych do przegranych to {ZaoWygrane}:{ZaoPrzegrane}")

def TimerDown0():
    global timeleft0
    if timeleft0 > 0:
        timeleft0 -= 1
        timeLabel.config(text = "Pozostały czas " + str(timeleft0))
        timeLabel.after(1000, TimerDown0)
    else:
        GameStart()

def TimerDown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Pozostały czas " + str(timeleft))
        timeLabel.after(1000, TimerDown)
    else:
        GameFin()

def reducefract(n, d):
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0
    assert isinstance(d, int)
    assert isinstance(n, int)
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return n, d

def Dobor():
    global suma, przegrane, wygrane, karty
    wylosowana = random.randint(2,10)
    suma = suma + wylosowana
    karty.append(wylosowana)
    DobraneKarty.config(text=f"Dobrane karty: {karty}")
    WartoscKarty.config(text=f"Dobrana karta ma wartość {wylosowana}")
    if suma>21:
        GameInfo.config(text=f"Przegrałeś! Wartość Twoich kart wynosi {suma}, więc jest większa od 21")
        przegrane+=1
        suma=0
        info2.config(text=f"Wygrane Ty={wygrane}, komputer={przegrane}")
        StartButton.config(text="Gram dalej!")
        StartButton.pack()
        ZostajeButton.place_forget()
        DobieramButton.place_forget()
        karty = []

def Zostaje():
    global suma, komputer, przegrane, wygrane, karty
    komputer = random.randint(12,21)
    GameInfo.config(text=f"Zakończyłeś z {suma}pkt")
    GameInfo2.config(text=f"Wartość jaką zebrał komputer to {komputer}")
    if suma>=komputer and suma<22:
        GameInfo3.config(text="Gratulacje wygrałeś! Zdobywasz punkt!")
        wygrane+=1
        suma=0
        info2.config(text=f"Wygrane Ty={wygrane}, komputer={przegrane}")
        StartButton.config(text="Gram dalej!")
        StartButton.pack()
        ZostajeButton.place_forget()
        DobieramButton.place_forget()
        karty = []
    elif suma<komputer:
        GameInfo3.config(text="Wartość Twoich kart jest mniejsza lub równa wartości komputera, więc przegrywasz :c")
        przegrane+=1
        suma=0
        info2.config(text=f"Wygrane Ty={wygrane}, komputer={przegrane}")
        StartButton.config(text="Gram dalej!")
        StartButton.pack()
        ZostajeButton.place_forget()
        DobieramButton.place_forget()
        karty = []


def EyeGame():
    global wygrane, przegrane, suma, karty
    GameInfo.config(text="")
    GameInfo2.config(text="")
    GameInfo3.config(text="")
    info2.config(text=f"Wygrane: Ty={wygrane}, komputer={przegrane}")
    if not DobieramButton.pack():
        DobieramButton.place(x=330, y=350)
        ZostajeButton.place(x=750, y=350)
    DobieramButton.config(text="Dobieram", padx=10, pady=5, font=ButtonFont)
    ZostajeButton.config(text="Zostaje z tym co mam", padx=10, pady=5, font=ButtonFont)
    DobraneKarty.config(text=f"Dobrane karty: {karty}")
    WartoscKarty.config(text=f"Dobrana karta ma wartość {wylosowana}")

timeleft0 = 60
timeleft = 120
wygrane = 0
przegrane = 0
suma = 0
komputer = 0
karty = []

root = tk.Tk()
root.title('Badanie podejmowania decyzji')
root.geometry("1920x1080")
root.state("zoomed")

canvas = tk.Canvas(root, bg="#d9d1e0")
canvas.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.6, relheight=0.6, relx=0.2, rely=0.2)

InfoFont = font.Font(family='Tahoma', size=14)
ButtonFont = font.Font(family='Tahoma', size=16)

info1 = Label(canvas, text="Badanie drugie: Podejmowanie decyzji", pady=30, font=("Tohoma", 20), bg="#d9d1e0")
info1.pack()

StartButton = Button(frame, text="Zacznij część próbną", padx=10, pady=5, font=ButtonFont, command=lambda:[StartButton.pack_forget(), start0()])
StartButton.pack()

info2 = Label(frame, text="Badanie przypomina grę w oczko. Polega ono na zbieraniu punktów i równoczesnym nie przekroczeniu wartości 21. Możesz dobrać kartę (o losowej wartości od 2 do 10) albo zakończyć dobieranie, wciskając odpowiedni przycisk. Twój wynik zostanie porównany z konkurującym z Tobą komputerem. Wygrasz jeśli będziesz mieć więcej punktów (do 21) lub tyle co komputer. Twoim celem jest wygranie jak najwięcej razy, przy jak najmniejszej ilości przegranych. Na początku gry masz 1 minutę, w której wyniki nie będą brane pod uwagę, gdyż jest to czas na Twoje zapoznanie się z programem. Następnie otrzymujesz 2 minuty na właściwe zadanie.", pady=20, font=InfoFont, bg="white", wraplength=700, justify="center")
info2.pack()

DobraneKarty = Label(frame, text="", pady=10, font=InfoFont, bg="white", justify="left")
DobraneKarty.pack()

WartoscKarty = Label(frame, text="", pady=10, font=InfoFont, bg="white", justify="left")
WartoscKarty.pack()

GameInfo = Label(frame, text="", pady=10, font=InfoFont, bg="white", justify="left")
GameInfo.pack()

GameInfo2 = Label(frame, text="", pady=10, font=InfoFont, bg="white", justify="left")
GameInfo2.pack()

GameInfo3 = Label(frame, text="", pady=10, font=InfoFont, bg="white", justify="left")
GameInfo3.pack()

timeLabel = Label(canvas, text = "Pozostały czas: " + str(timeleft0), font = ('Tahoma', 18), bg="#d9d1e0")

DobieramButton = Button(canvas, command=lambda:[Dobor()])
DobieramButton.pack(side=tk.LEFT)
ZostajeButton = Button(canvas, command=lambda:[Zostaje()])
ZostajeButton.pack(side=tk.RIGHT)

root.mainloop()
