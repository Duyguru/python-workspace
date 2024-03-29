'''
from turtle import*
import time,random
Liste=[]
score=0
maxscore=0
s=Screen()
s.title("Yılan Oyunu")
s.setup(600,600)
s.bgcolor("pink")
s.tracer(0)

yilan=Turtle()
yilan.speed(0)
yilan.shape("circle")
yilan.color("darkgreen")
yilan.penup()
yilan.goto(0,0)
yilan.yon="dur"


def hareket():
    if yilan.yon=="yukari":
        y=yilan.ycor()
        yilan.sety(y+20)

    if yilan.yon=="asagi":
        y=yilan.ycor()
        yilan.sety(y-20)

    if yilan.yon=="sag":
        x=yilan.xcor()
        yilan.setx(x+20)

    if yilan.yon=="sol":
        x=yilan.xcor()
        yilan.setx(x-20)

def yukariGit():
    if yilan.yon!="asagi":
       yilan.yon="yukari"

def asagiGit():
    if yilan.yon!="yukari":
       yilan.yon="asagi"

def sagaGit():
    if yilan.yon!="sol":
       yilan.yon="sag"

def solaGit():
    if yilan.yon!="sag":
       yilan.yon="sol"

s.listen()
s.onkeypress(yukariGit,"Up")
s.onkeypress(asagiGit,"Down")
s.onkeypress(sagaGit,"Right")
s.onkeypress(solaGit,"Left")

while True:
    s.update()
    hareket()
    time.sleep(0.1)


yem=Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("purple")
yem.penup()
yem.goto(0,100)


def ye():
    if yilan.distance(yem)<20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        yem.goto(x,y)

        kuyruk=Turtle()
        kuyruk.speed(0)
        kuyruk.shape("rectangular")
        kuyruk.shape("green")
        kuyruk.penup()
        Liste.append(kuyruk)
        global score
        global maxscore
        score+=5
        if score>maxscore:
         maxscore=score
         s.title("Skor:{} En yüksek skor: {}".format(score,maxscore))

    uzunluk=len(Liste)
    for indis in range (uzunluk-1,0,-1):
        x=Liste[indis-1].xcor()
        y=Liste[indis-1].ycor()
        Liste[indis].goto(x,y)


    if len(Liste)>0:
          x=yilan.xcor()
          y=yilan.ycor()
          Liste[0].goto(x,y)

def baslangic():
   
    time.sleep(0.1)
    yilan.goto(0,0)
    yilan.yon="dur"
    
    for eklem in Liste:
        eklem.goto(1000,1000)

    Liste.clear()
    score=0
    s.title("Skor: {} En yüksek puan: {}".format(score,maxscore))

while True:
    s.update()
    ye()
    hareket()
    if yilan.xcor()>290 or yilan.xcor()<-290 or yilan.ycor>290 or yilan.ycor<-290:
        baslangic()
    for eklem in Liste:
        if eklem.distance(yilan)<20:
            baslangic()

    time.speed(0.1)

s.mainloop()

'''

from turtle import *
import time
import random

Liste = []
score = 0
maxscore = 0

s = Screen()
s.title("Yılan Oyunu")
s.setup(600, 600)
s.bgcolor("pink")
s.tracer(0)

yilan = Turtle()
yilan.speed(0)
yilan.shape("circle")
yilan.color("darkgreen")
yilan.penup()
yilan.goto(0, 0)
yilan.yon = "dur"


def hareket():
    if yilan.yon == "yukari":
        y = yilan.ycor()
        yilan.sety(y + 20)

    if yilan.yon == "asagi":
        y = yilan.ycor()
        yilan.sety(y - 20)

    if yilan.yon == "sag":
        x = yilan.xcor()
        yilan.setx(x + 20)

    if yilan.yon == "sol":
        x = yilan.xcor()
        yilan.setx(x - 20)


def yukariGit():
    if yilan.yon != "asagi":
        yilan.yon = "yukari"


def asagiGit():
    if yilan.yon != "yukari":
        yilan.yon = "asagi"


def sagaGit():
    if yilan.yon != "sol":
        yilan.yon = "sag"


def solaGit():
    if yilan.yon != "sag":
        yilan.yon = "sol"


s.listen()
s.onkeypress(yukariGit, "Up")
s.onkeypress(asagiGit, "Down")
s.onkeypress(sagaGit, "Right")
s.onkeypress(solaGit, "Left")

yem = Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("purple")
yem.penup()
yem.goto(0, 100)


def ye():
    global score,maxscore
    if yilan.distance(yem) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

        kuyruk = Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("green")
        kuyruk.penup()
        Liste.append(kuyruk)
        score += 5
        if score > maxscore:
            maxscore = score
        s.title("Skor:{} En yüksek skor: {}".format(score, maxscore))

    uzunluk = len(Liste)
    for indis in range(uzunluk - 1, 0, -1):
        x = Liste[indis - 1].xcor()
        y = Liste[indis - 1].ycor()
        Liste[indis].goto(x, y)

    if len(Liste) > 0:
        x = yilan.xcor()
        y = yilan.ycor()
        Liste[0].goto(x, y)


def baslangic():
    global score,maxscore
    score = 0
    s.title("Skor: {} En yüksek puan: {}".format(score, maxscore))
    time.sleep(0.1)
    yilan.goto(0, 0)
    yilan.yon = "dur"

    for eklem in Liste:
        eklem.goto(1000, 1000)

    Liste.clear()


while True:
    s.update()
    ye()
    hareket()
    if (
        yilan.xcor() > 290
        or yilan.xcor() < -290
        or yilan.ycor() > 290
        or yilan.ycor() < -290
    ):
        baslangic()
    for eklem in Liste:
        if eklem.distance(yilan) < 20:
            baslangic()

    time.sleep(0.1)















        

























































































