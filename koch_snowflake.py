import math
import turtle
import tkinter
t = turtle.Turtle()
def draw_KochSF(x1, y1, x2, y2, t):
    d = math.sqrt((x1 -x2) * (x1 - x2) + (y1 - y2) *(y1 - y2))
    r = d / 3.0
    h = r*(math.sqrt(3)/2.0)#h=(sqrt3)/2 times scale units r
    p3 = ((x1 + 2 * x2)/3.0, (y1 + 2 *  y2)/3.0)#2nd shoulder of the flake
    p1 = ((2 * x1 + x2)/3.0, (2 * y1 + y2))# first shoulder
    c = (0.5*(x1 + x2), 0.5*(y1 + y2)) #centre
    n = ((y1 - y2)/d, (x2 - x1)/d) #vector for p2 = c + h * n
    p2 = (c[0] + h * n[0], c[1] + h * n[1]) #centre of flake
    if d > 10:
        #flake1
        draw_KochSF(x1, y1, p1[0], p1[1], t)
        #flake2
        draw_KochSF(p1[0], p1[1], p2[0], p2[1], t)
        #flake3
        draw_KochSF(p2[0], p2[1], p3[0], p3[1]. t)
        #flake4
        draw_KochSF(p3[0], p3[1], x2, y2, t)
    else:
        #draw cone
        t.up()
        t.setpos(p1[0], p1[1])
        t.down()
        t.setpos(p2[0], p2[1])
        t.setpos(p3[0], p3[1])
        #draw sides
        t.up()
        t.setpos(x1, y1)
        t.down()
        t.setpos(p1[0], p1[1])
        t.up()
        t.setpos(p3[0], p3[1])
        t.down()
        t.setpos(x2, y2)
       

def main():
    print('Drawing the Koch Snowflake...')
    t = turtle.Turtle()
    t.hideturtle()
    #draw!
    try:
        draw_KochSF(-100, 0, 100, 0, t)
        draw_KochSF(0, -173.2, -100, 0, t)
        draw_KochSF(100, 0, 0, -173.2, t)
        
       
    except Exception as e:
       
        print(f'Execption: {e}, exiting.')
        
    turtle.Screen().exitonclick()
if __name__=="__main__":
    main()