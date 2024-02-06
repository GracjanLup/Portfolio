import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
from PIL import ImageTk, Image

# pip install Pillow

def Czekaj1():
    info2.place_forget()
    ImageL1.place_forget()
    StartButton.after(2000, start1)

def start1():
    global start, stop, roznica, WhichOne
    start=time.time()
    LeftButton.place(x=270, y=440)
    RightButton.place(x=400, y=440)
    LeftButton.config(text="<--")
    RightButton.config(text="-->")
    ImageL1.config(image=zdjDoTabeli[WhichOne])
    ImageL1.place(relx=0.2, rely=0.15)
    WhichOne += 1

def GameCheck(zmienna):
    # Prawa strzałka
    if zmienna == 1:
        if WhichOne == 1 or WhichOne == 3 or WhichOne == 4 or WhichOne == 6 or WhichOne == 7 or WhichOne == 10 or WhichOne == 12 or WhichOne == 14 or WhichOne == 19 or WhichOne == 20 or WhichOne == 21 or WhichOne == 24 or WhichOne == 26 or WhichOne == 27 or WhichOne == 28:
            return True
        else:
            return False
    # Lewa strzałka
    else:
        if WhichOne == 2 or WhichOne == 5 or WhichOne == 8 or WhichOne == 9 or WhichOne == 3 or WhichOne == 4 or WhichOne == 6 or WhichOne == 11 or WhichOne == 13 or WhichOne == 15 or WhichOne == 16 or WhichOne == 17 or WhichOne == 18 or WhichOne == 22 or WhichOne == 23 or WhichOne == 25 or WhichOne == 29 or WhichOne == 30:
            return True
        else:
            return False

def Czekaj():
    global WhichOne
    LeftButton.place_forget()
    RightButton.place_forget()
    ImageL1.place_forget()
    if WhichOne == 5:
        LeftButton.after(10000, NextRound)
    else:
        LeftButton.after(2000, NextRound)

def NextRound():
    global start
    start=time.time()
    LeftButton.place(x=270, y=440)
    RightButton.place(x=400, y=440)
    ImageL1.place(relx=0.2,rely=0.15)
    global WhichOne
    if WhichOne == 5:
        info2.place_forget()
    ImageL1.config(image=zdjDoTabeli[WhichOne])
    WhichOne += 1

def Next(zmienna):
    global WhichOne, Points
    global stop, roznica
    stop = time.time()
    roznica = stop - start
    zaokraglona = round(roznica,4)
    if WhichOne > 5:
        czasy.append(zaokraglona)

    userwin = GameCheck(zmienna)
    if userwin:
        Points += 1
        print(Points)
    if WhichOne == 30:
        GameFin()
    else:
        if WhichOne == 5:
            info2.config(text=f"Od tego momentu zaczyna się właściewe badanie. Które włączy się po 10s, proszę zachować czujność i kursor na znaku \"+\"\nPoprawne odpowiedzi w części próbnej: {Points}/5.")
            info2.place(x=35, y=40)
            Points = 0
        Czekaj()

def GameFin():
    global Points
    ImageL1.place_forget()
    LeftButton.place_forget()
    RightButton.place_forget()
    PunktStart.place_forget()
    InfoResults.pack()
    InfoResults.insert(INSERT, f"Uzyskane czasy to: {czasy}\nUzyskałeś {Points}/25 punktów!")

timeleft = 5
WhichOne = 0
Points = 0

czasy = []
start = 0
stop = 0
roznica = 0
czas = 0

zdj = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
zdjRozmiar = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
zdjDoTabeli = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
ImageLabel = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

ImgA = ["Stroop/28.png", "Stroop/15.png", "Stroop/16.png", "Stroop/4.png", "Stroop/23.png", "Stroop/6.png", "Stroop/7.png", "Stroop/20.png", "Stroop/18.png", "Stroop/10.png", "Stroop/19.png", "Stroop/12.png", "Stroop/13.png", "Stroop/26.png", "Stroop/2.png", "Stroop/3.png", "Stroop/17.png", "Stroop/9.png", "Stroop/30.png", "Stroop/8.png", "Stroop/21.png", "Stroop/22.png", "Stroop/5.png", "Stroop/24.png", "Stroop/25.png", "Stroop/14.png", "Stroop/27.png", "Stroop/1.png", "Stroop/29.png", "Stroop/11.png"]

ImgAa = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

root = tk.Tk()
root.title('Badanie skuienia')
root.geometry("1920x1080")
# Pełne okno:
root.state("zoomed")

InfoFont = font.Font(family='Tahoma', size=14)
ArrowFont = font.Font(family='Tahoma', size=26)
ButtonFont = font.Font(family='Tahoma', size=16)

canvas = tk.Canvas(root, bg="#d9d1e0")
canvas.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.6, relheight=0.8, relx=0.2, rely=0.1)

info1 = Label(canvas, text="Badanie pierwsze: Skupienie", font=("Tohoma", 20), bg="#d9d1e0")
info1.place(x=470, y=15)

for i in range (len(ImgA)):
    zdj[i] = (Image.open(ImgA[i]))
    zdjRozmiar[i]= zdj[i].resize((450,300), Image.LANCZOS)
    zdjDoTabeli[i] = ImageTk.PhotoImage(zdjRozmiar[i])

img1 = (Image.open("Stroop/25.png"))
resized_image1= img1.resize((450,300), Image.LANCZOS)
Image1 = ImageTk.PhotoImage(resized_image1)
ImageL1 = Label(frame, image=Image1)
ImageL1.place(relx=0.2,rely=0.4)

info2 = Label(frame, text="Po kliknięciu przycisku \"Zaczniej badanie\", masz 2s na ustawienie kursora na znaku \"+\". Po tym czasie zostaną wyświetlone trzy napisy, (tak jak w przykładzie poniżej) górny napis decyduje w jakim kolorze CZCIONKI napis należy wybrać. Wyboru dokonujemy poprzez kliknięcie odpowiedniego przycisku strzałka w lewo \"<--\" jeżeli napis w odpowiednim kolorze czcionki jest po lewej, a strzałka w prawo \"-->\" jeżeli po prawej. Po każdym kliknięciu masz 2s na ponowne ustawienie kursora na znaku \"+\". Pierwsze 5 przykładów ma na celu zapoznaie Ciebie z zadaniem, ich wyniki nie będą brane pod uwagę. Proszę się przygotować i wciskać przyciski jak najszybciej i jak najpoprawniej.", pady=20, font=InfoFont, bg="white", wraplength=700, justify="center")
info2.place(x=35, y=40)

PunktStart = Label(frame, font=ArrowFont, text="+", bg="white")
PunktStart.place(x=360, y=450)

RightButton = Button(frame, font=ArrowFont, command=lambda:Next(1))
LeftButton = Button(frame, font=ArrowFont, command=lambda:Next(0))

StartButton = Button(frame, text="Zacznij badanie", padx=10, pady=5, font=ButtonFont, command=lambda:[StartButton.place_forget(), Czekaj1()])
StartButton.place(relx=0.39,rely=0.01)

InfoResults = Text(frame, font=InfoFont)

root.mainloop()
