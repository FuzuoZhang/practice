from turtle import *

def draw_sun():
    print(pos())
    ht()
    color('red','yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break

    end_fill()
    done()


if __name__ == '__main__':
    draw_sun()