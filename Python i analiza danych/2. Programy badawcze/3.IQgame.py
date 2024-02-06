import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import time
from PIL import ImageTk, Image

# pip install Pillow

def start1():
    # TimerDown()
    global start, stop, roznica
    start=time.time()
    info2.config(text="\n\n\n")
    OdpA.place(relx=0.3, rely=0.6)
    OdpB.place(relx=0.4, rely=0.6)
    OdpC.place(relx=0.5, rely=0.6)
    OdpD.place(relx=0.6, rely=0.6)
    Answer()

def Answer():
    global WhichOne
    info2.place_forget()
    ImageL1.place(x=180, y=170)
    OdpA.place(relx=0.3, rely=0.6)
    OdpB.place(relx=0.4, rely=0.6)
    OdpC.place(relx=0.5, rely=0.6)
    OdpD.place(relx=0.6, rely=0.6)
    ImageL2.place_forget()
    ImageL1.place(x=140, y=80)
    ImageL1.config(image=zdjDoTabeli[WhichOne])
    OdpA.config(image=ImgAb[WhichOne])
    OdpB.config(image=ImgBb[WhichOne])
    OdpC.config(image=ImgCb[WhichOne])
    OdpD.config(image=ImgDb[WhichOne])


def GameCheck(zmienna):
    global WhichOne
    Pom1 = ImgTable[WhichOne]
    Zmienna2 = SlownikOdp[Pom1]
    if zmienna == Zmienna2:
        return True
    else:
        return False

def Next(zmienna):
    global WhichOne, Points
    global start, stop, roznica
    # global timeleft
    # timeleft = 5
    stop = time.time()
    roznica = stop - start
    zaokraglona = round(roznica,4)
    if WhichOne > 3:
        czasy.append(zaokraglona)
    start=time.time()

    userwin = GameCheck(zmienna)
    if userwin:
        Points += 1
    WhichOne += 1
    if WhichOne == 15:
        GameFin()
    else:
        if WhichOne == 3:
            info2.config(text=f"Od tego momentu zaczyna się właściewe badanie. Które włączy się po 10s, proszę zachować czujność i postarać się jak najszybciej klikać odpowiedzi na następne zadania.\nPoprawne odpowiedzi w części próbnej: {Points}/3.")
            info2.place(x=35, y=40)
            Points = 0
        Czekaj()

def Czekaj():
    global WhichOne
    ImageL1.place_forget()
    OdpA.place_forget()
    OdpB.place_forget()
    OdpC.place_forget()
    OdpD.place_forget()
    if WhichOne == 3:
        OdpA.after(10000, Answer)
    else:
        OdpA.after(000, Answer)

# def TimerDown():
#     global timeleft
#     if timeleft > 0:
#         timeleft -= 1
#         timeLabel.config(text = "Pozostały czas " + str(timeleft))
#         timeLabel.after(1000, TimerDown)
#     else:
#         print("Aha")

def GameFin():
    global Points
    ImageL1.place_forget()
    OdpA.place_forget()
    OdpB.place_forget()
    OdpC.place_forget()
    OdpD.place_forget()
    InfoResults.pack()
    InfoResults.insert(INSERT, f"Uzyskane czasy to: {czasy}\nUzyskałeś {Points}/12 punktów!")

SlownikOdp = {"Problemy/zad1.png": "Problemy/odp1.png", "Problemy/zad2.png": "Problemy/odp2.png", "Problemy/zad3.png": "Problemy/odp3.png", "Problemy/zad4.png": "Problemy/odp4.png", "Problemy/zad5.png": "Problemy/odp5.png", "Problemy/zad6.png": "Problemy/odp6.png", "Problemy/zad7.png": "Problemy/odp7.png", "Problemy/zad8.png": "Problemy/odp8.png", "Problemy/zad9.png": "Problemy/odp9.png", "Problemy/zad10.png": "Problemy/odp10.png", "Problemy/zad11.png": "Problemy/odp11.png", "Problemy/zad12.png": "Problemy/odp12.png", "Problemy/zad13.png": "Problemy/odp13.png", "Problemy/zad14.png": "Problemy/odp14.png", "Problemy/zad15.png": "Problemy/odp15.png"}

WhichOne = 0
Points = 0

czasy = []
start = 0
stop = 0
roznica = 0
czas = 0

AnsTable = ["Problemy/odp1.png", "Problemy/odp2.png", "Problemy/odp3.png", "Problemy/odp4.png", "Problemy/odp5.png", "Problemy/odp6.png", "Problemy/odp7.png", "Problemy/odp8.png", "Problemy/odp9.png", "Problemy/odp10.png", "Problemy/odp11.png", "Problemy/odp12.png", "Problemy/odp13.png", "Problemy/odp14.png", "Problemy/odp15.png"]
ImgTable = ["Problemy/zad1.png", "Problemy/zad2.png", "Problemy/zad3.png", "Problemy/zad4.png", "Problemy/zad5.png", "Problemy/zad6.png", "Problemy/zad7.png", "Problemy/zad8.png", "Problemy/zad9.png", "Problemy/zad10.png", "Problemy/zad11.png", "Problemy/zad12.png", "Problemy/zad13.png", "Problemy/zad14.png", "Problemy/zad15.png"]

zdj = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
zdjRozmiar = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
zdjDoTabeli = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
ImageLabel = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

ImgA = ["Problemy/15.png", "Problemy/4.png", "Problemy/5.png", "Problemy/odp4.png", "Problemy/4.png", "Problemy/odp6.png", "Problemy/23.png", "Problemy/10.png", "Problemy/11.png", "Problemy/16.png", "Problemy/odp11.png", "Problemy/22.png", "Problemy/23.png", "Problemy/28.png", "Problemy/odp15.png", ""]
ImgB = ["Problemy/odp1.png", "Problemy/6.png", "Problemy/odp3.png", "Problemy/16.png", "Problemy/odp5.png", "Problemy/10.png", "Problemy/odp7.png", "Problemy/9.png", "Problemy/12.png", "Problemy/15.png", "Problemy/17.png", "Problemy/21.png", "Problemy/odp13.png", "Problemy/27.png", "Problemy/29.png", ""]
ImgC = ["Problemy/10.png", "Problemy/9.png", "Problemy/19.png", "Problemy/30.png", "Problemy/29.png", "Problemy/14.png", "Problemy/6.png", "Problemy/8.png", "Problemy/odp9.png", "Problemy/odp10.png", "Problemy/18.png", "Problemy/20.png", "Problemy/24.png", "Problemy/odp14.png", "Problemy/30.png", ""]
ImgD = ["Problemy/3.png", "Problemy/odp2.png", "Problemy/11.png", "Problemy/18.png", "Problemy/14.png", "Problemy/19.png", "Problemy/7.png", "Problemy/odp8.png", "Problemy/13.png", "Problemy/14.png", "Problemy/19.png", "Problemy/odp12.png", "Problemy/25.png", "Problemy/26.png", "Problemy/1.png", ""]

ImgAa = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
ImgAb = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

ImgBa = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
ImgBb = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

ImgCa = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
ImgCb = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

ImgDa = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
ImgDb = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

root = tk.Tk()
root.title('Badanie rozwiązywania problemów')
root.geometry("1920x1080")
root.state("zoomed")

InfoFont = font.Font(family='Tahoma', size=14)
ButtonFont = font.Font(family='Tahoma', size=16)

canvas = tk.Canvas(root, bg="#d9d1e0")
canvas.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.6, relheight=0.6, relx=0.2, rely=0.2)

info1 = Label(canvas, text="Badanie trzecie: Rozwiązywanie problemów", pady=15, font=("Tohoma", 20), bg="#d9d1e0")
info1.pack()

info2 = Label(frame, text="Badanie polega na dodawaniu i odejmowaniu fioletowych pól kwadratów z siatek 3x3. Masz za zadanie wybrać poprawną z 4 odpowiedzi, wyświetlających się na dole ekranu, naciskając na odpowiednią z nich. Twoim celem jest udzielenie jak najwiękczej ilości poprawych odpowiedzi, w jak najkrótszym czasie. Pierwsze trzy zadania mają na celu zapoznanie Cię z programem, ich wyniki nie będą branę pod uwagę. By rozpocząć badanie wciśnij przycisk \"Zacznij badanie\". \nPrzykłady:", pady=20, font=InfoFont, bg="white", wraplength=700, justify="center")
info2.pack()

info3 = Label(frame, text="", pady=20, font=InfoFont, bg="white", wraplength=700, justify="center")
info3.pack()

img1 = (Image.open("Problemy/Przykład1.png"))
resized_image1= img1.resize((400,100), Image.LANCZOS)
Image1 = ImageTk.PhotoImage(resized_image1)
ImageL1 = Label(frame, image=Image1)
ImageL1.place(x=180, y=170)

img2 = (Image.open("Problemy/Przykład2.png"))
resized_image2= img2.resize((400,100), Image.LANCZOS)
Image2 = ImageTk.PhotoImage(resized_image2)
ImageL2 = Label(frame, image=Image2)
ImageL2.place(x=180, y=280)

for i in range (len(ImgTable)):
    zdj[i] = (Image.open(ImgTable[i]))
    zdjRozmiar[i]= zdj[i].resize((480,100), Image.LANCZOS)
    zdjDoTabeli[i] = ImageTk.PhotoImage(zdjRozmiar[i])
    # ImageLabel[i] = Label(canvas, image=zdjDoTabeli[i])
    # ImageLabel[i].pack()

for i in range (0, 15):
    ImgAa[i] = PhotoImage(file=ImgA[i])
    ImgAb[i] = ImgAa[i].subsample(3, 3)

for i in range (0, 15):
    ImgBa[i] = PhotoImage(file=ImgB[i])
    ImgBb[i] = ImgBa[i].subsample(3, 3)

for i in range (0, 15):
    ImgCa[i] = PhotoImage(file=ImgC[i])
    ImgCb[i] = ImgCa[i].subsample(3, 3)

for i in range (0, 15):
    ImgDa[i] = PhotoImage(file=ImgD[i])
    ImgDb[i] = ImgDa[i].subsample(3, 3)

# timeLabel = Label(canvas, text="", font = ('Tahoma', 25), bg="#d9d1e0")
# timeLabel.pack()

OdpA = Button(canvas, command=lambda:Next(ImgA[WhichOne]))
OdpB = Button(canvas, command=lambda:Next(ImgB[WhichOne]))
OdpC = Button(canvas, command=lambda:Next(ImgC[WhichOne]))
OdpD = Button(canvas, command=lambda:Next(ImgD[WhichOne]))

InfoResults = Text(frame, font=InfoFont)

StartButton = Button(canvas, text="Zacznij badanie", padx=10, pady=5, font=ButtonFont, command=lambda:[StartButton.pack_forget(), start1()])
StartButton.pack()

root.mainloop()
