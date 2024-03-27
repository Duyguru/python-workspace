from turtle import*
import time
s=Screen()
s.setup(400,600)

penup()
goto(0,180)
pendown()
pensize(4)

for i in range (2):
    fd(80)
    rt(90)
    fd(220)
    rt(90)

def kirmizi():
    penup()
    goto(40,140)
    fillcolor("red")
    shape("circle")
    shapesize(3)

def sari():
    penup()
    goto(40,70)
    fillcolor("yellow")
    shape("circle")
    shapesize(3)

def yesil():
    penup()
    goto(40,0)
    fillcolor("green")
    shape("circle")
    shapesize(3)
sayac=0
while sayac<5:
    yesil()
    time.sleep(2)
    sari()
    time.sleep(2)
    kirmizi()
    time.sleep(2)
    sayac+=1

s.mainloop()
