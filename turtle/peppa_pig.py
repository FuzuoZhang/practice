from turtle import *

#默认为standard模式

FACE_COLOR = (251, 207, 237)
FACE_PEN_COLOR = (233, 154, 207)
NOSE_COLOR = (179, 98, 151)
MOUTH_COLOR = (215, 43, 125)
CHEEK_COLOR = (237, 164, 207)
BODAY_COLOR = (214, 74, 65)

def nose(x, y, init_angle):
	penup()
	goto(x, y)
	seth(init_angle)
	color(FACE_PEN_COLOR, FACE_COLOR)
	pendown()
	begin_fill()
	for i in range(120):
		if (i >= 30 and i <= 120) or (i >= 210 and i <= 300):
			circle(35,3)
		else:
			circle(50,3)
	end_fill()
	done() 
	
def head(x, y):
	pass 

def body(x, y):
	pass

if __name__ == "__main__":
	home()
	nose(50, 50, 15)

	#NOSE_COLOR = 

