from turtle import *
import colorsys

speed(0)
bgcolor('white')
pensize(10)
h = 0
for i in range(60):
    for j in range(10):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.05
        rt(90)
        circle(150-j*10, 90)
        lt(90)
        circle(150-j*9, 90)
        rt(180)
    circle(40,24)
done()

    #     h += 0.05
    #     fd(100)
    #     rt(59)
    #     colormode(255)
    #     r = int(c[0] * 255)
    #     g = int(c[1] * 255)
    #     b = int(c[2] * 255)
    #     pencolor(r, g, b)
    # rt(90)
    
# for i in range(360):
#     color = colorsys.hsv_to_rgb(hue, 1, 1)
#     hue += 0.005
#     fd(100)
#     rt(59)
#     pencolor(color)
#     if i < 120:
#         width(i / 10 + 1)
#     elif i < 240:
#         width(12 - i / 20)
#     else:
#         width(i / 20 - 6)
#     if i == 359:
#         break
