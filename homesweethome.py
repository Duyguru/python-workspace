from turtle import*
colormode(255)
color(200,50,90)
pensize(4)
def ucgen():
    for x in range(3):
        fd(200)
        lt(120)

def kare():
    for x in range(4):
        forward(200)
        right(90)

begin_fill()
fillcolor(199,78,79)
ucgen()
end_fill()

begin_fill()
fillcolor(100,25,75)
kare()
end_fill()
