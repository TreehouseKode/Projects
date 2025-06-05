import math
import turtle

def draw_KochSF(x1, y1, x2, y2, t):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    r = d / 3.0
    h = r * (math.sqrt(3) / 2.0)  # height of equilateral triangle
    p3 = ((x1 + 2 * x2) / 3.0, (y1 + 2 * y2) / 3.0)  # 2nd shoulder
    p1 = ((2 * x1 + x2) / 3.0, (2 * y1 + y2) / 3.0)  # 1st shoulder
    c = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)  # midpoint
    n = ((y1 - y2) / d, (x2 - x1) / d)  # normal vector
    p2 = (c[0] + h * n[0], c[1] + h * n[1])  # peak point

    if d > 10:
        # Recursive calls to draw smaller Koch segments
        draw_KochSF(x1, y1, p1[0], p1[1], t)
        draw_KochSF(p1[0], p1[1], p2[0], p2[1], t)
        draw_KochSF(p2[0], p2[1], p3[0], p3[1], t)
        draw_KochSF(p3[0], p3[1], x2, y2, t)
    else:
        # Drawing the actual snowflake when recursion stops
        t.up()
        t.setpos(x1, y1)
        t.down()
        t.setpos(p1[0], p1[1])
        t.setpos(p2[0], p2[1])
        t.setpos(p3[0], p3[1])
        t.setpos(x2, y2)

def main():
    print('Drawing the Koch Snowflake...')
    t = turtle.Turtle()
    t.hideturtle()
    
    # Set up the window size and turtle speed (optional)
    turtle.speed(0)
    
    # Draw the Koch Snowflake
    try:
        draw_KochSF(-100, 0, 100, 0, t)
        draw_KochSF(0, -173.2, -100, 0, t)
        draw_KochSF(100, 0, 0, -173.2, t)
    except Exception as e:
        print(f"Exception: {e}")
    
    # Ensure the window doesn't close immediately
    turtle.Screen().exitonclick()

if __name__ == "__main__":
    main()
