# -*- coding: utf-8 -*-
# Auteur : Alexandreou

import random
from tkinter import *

def zero(a, b, f, g, t, v_tk_speed):
	x_d = a + (-50)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(180)
	t.penup()
	t.forward(10)
	t.right(90)
	t.forward(10)
	t.down()
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.hideturtle()

def un(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140)
	t.left(130)
	t.forward(100)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(80)
	t.left(-130)
	t.forward(120)
	t.left(90)
	t.forward(9)
	t.hideturtle()
	
def deux(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(60)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(70)
	t.left(90)
	t.forward(80)
	t.hideturtle()
		
def trois(a, b, f, g, t, v_tk_speed):
	x_d = a +(-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(40)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(40)
	t.right(90)
	t.forward(60)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(80)
	t.hideturtle()
	
def quatre(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140)
	t.left(140)
	t.forward(120)
	t.left(130)
	t.forward(90)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(130)
	t.forward(75)
	t.right(140)
	t.forward(116)
	t.left(90)
	t.forward(9)
	t.hideturtle()
	
def cinq(a, b, f, g, t, v_tk_speed):
	x_d = a + (-140)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(80)
	t.left(90)
	t.forward(70)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(60)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(10)
	t.hideturtle()

def six(a, b, f, g, t, v_tk_speed):
	x_d = a + (-130)
	y_d = b + 20
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.right(0)
	t.forward(70)
	t.right(90)
	t.forward(70)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(140)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.hideturtle()
	
def sept(a, b, f, g, t, v_tk_speed):
	x_d = a + (-140)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(50)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.right(-10)
	t.forward(70)
	t.right(60)
	t.forward(20)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(15)
	t.right(120)
	t.forward(80)
	t.left(120)
	t.forward(80)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(65)
	t.right(120)
	t.forward(68)
	t.right(60)
	t.forward(20)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(15)
	t.right(120)
	t.forward(70)
	t.left(120)
	t.forward(10)
	t.hideturtle()
	
def huit(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.penup()
	t.left(180)
	t.forward(10)
	t.right(90)
	t.forward(10)
	t.down()
	t.forward(60)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(60)
	t.penup()
	t.left(90)
	t.forward(70)
	t.down()
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.hideturtle()

def neuf(a, b, f, g, t, v_tk_speed):
	x_d = a + (-70)
	y_d = b + (20)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.right(0)
	t.forward(70)
	t.right(90)
	t.forward(70)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(140)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.hideturtle()
	
def pzero(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.penup()
	t.left(180)
	t.forward(10/3)
	t.right(90)
	t.forward(10/3)
	t.down()
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()

def pun(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140/3)
	t.left(130)
	t.forward(100/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(80/3)
	t.left(-130)
	t.forward(120/3)
	t.left(90)
	t.forward(9/3)
	t.hideturtle()
	
def pdeux(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(50/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(60/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(70/3)
	t.left(90)
	t.forward(80/3)
	t.hideturtle()
		
def ptrois(a, b, f, g, t, v_tk_speed):
	x_d = a + (-65)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(50/3)
	t.right(90)
	t.forward(40/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(40/3)
	t.right(90)
	t.forward(60/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(80/3)
	t.hideturtle()
	
def pquatre(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140/3)
	t.left(140)
	t.forward(120/3)
	t.left(130)
	t.forward(90/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(130)
	t.forward(75/3)
	t.right(140)
	t.forward(116/3)
	t.left(90)
	t.forward(9/3)
	t.hideturtle()
	
def pcinq(a, b, f, g, t, v_tk_speed):
	x_d = a + (-90)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(80/3)
	t.left(90)
	t.forward(70/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(60/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(50/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(10/3)
	t.hideturtle()

def psix(a, b, f, g, t, v_tk_speed):
	x_d = a + (-85)
	y_d = b + (-27)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.right(0)
	t.forward(70/3)
	t.right(90)
	t.forward(70/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(140/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(10/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()
	
def psept(a, b, f, g, t, v_tk_speed):
	x_d = a + (-85)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(50)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.right(-10)
	t.forward(70/3)
	t.right(60)
	t.forward(20/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(15/3)
	t.right(120)
	t.forward(80/3)
	t.left(120)
	t.forward(80/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(65/3)
	t.right(120)
	t.forward(68/3)
	t.right(60)
	t.forward(20/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(15/3)
	t.right(120)
	t.forward(70/3)
	t.left(120)
	t.forward(10/3)
	t.hideturtle()
	
def phuit(a, b, f, g, t, v_tk_speed):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.penup()
	t.left(180)
	t.forward(10/3)
	t.right(90)
	t.forward(10/3)
	t.down()
	t.forward(60/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(60/3)
	t.penup()
	t.left(90)
	t.forward(70/3)
	t.down()
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()
	
def pneuf(a, b, f, g, t, v_tk_speed):
	x_d = a + (-58)
	y_d = b + (-27)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.right(0)
	t.forward(70/3)
	t.right(90)
	t.forward(70/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(140/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(10/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()
	
def milieu(a, b, f, g, t, v_tk_speed):
	x_d = a + 20
	y_d = b
	
	# Pour changer aléatoirement la marque qui dessine, à chaque tour.
	alea = random.randint(0, 5)
	forme = ['arrow', 'turtle', 'circle', 'square', 'triangle',\
	'classic']
	logo = forme[alea]
	t.shape(logo)
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(50)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(50)
	t.hideturtle()
	t.reset()
	t.hideturtle()

def contour(a, b, f, g, t, v_tk_speed):
	x_d = a + 280
	y_d = b + (-90)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(190)
	t.left(90)
	t.forward(540)
	t.left(90)
	t.forward(190)
	t.left(90)
	t.forward(540)
	t.hideturtle()
	
def acontour(a, b, t, v_tk_speed, v_tk_chco_2):
	x_d = 0
	y_d = 200
	t.speed(v_tk_speed)
	if a == 1:
		t.speed(10)
	# Pour changer aléatoirement la marque qui dessine, à chaque tour.
	alea = random.randint(0, 5)
	forme = ['arrow', 'turtle', 'circle', 'square', 'triangle',\
	'classic']
	logo = forme[alea]
	t.shape(logo)
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	if a == 1 and v_tk_chco_2 == 1:
		t.penup()
	t.width(3)
	t.pencolor(b)
	t.circle(-200)
	t.hideturtle()
	if a == 1:
		t.reset()
		t.hideturtle()
		
def heurmin(b, t, v_tk_speed):
	x_d = 0
	y_d = 150
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.pencolor(b)
	t.down()
	t.width(1.2)
	t.speed(v_tk_speed)
	t.speed(20)
	for i in range(12):
		t.circle(-150, extent=30)
		t.left(-90)
		t.forward(8)
		t.right(-180)
		t.forward(8)
		t.left(-90)
	for i in range(60):
		t.penup()
		t.circle(-150, extent=6)
		t.down()
		t.left(-90)
		t.forward(5)
		t.right(-180)
		t.forward(5)
		t.left(-90)
	t.hideturtle()
	
def petitmil(a, b, t, v_tk_speed):
	x_d = 10
	y_d = 0
	if a == 1:
		t.speed(100)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.circle(10)
	t.hideturtle()
	t.end_fill()
	
def postrois(b, t, v_tk_speed):
	x_d = 185
	y_d = -20
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.forward(35)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(2.5)
	t.left(90)
	t.forward(17.5)
	t.right(90)
	t.forward(12.5)
	t.right(90)
	t.forward(10)
	t.left(90)
	t.forward(2.5)
	t.left(90)
	t.forward(10)
	t.right(90)
	t.forward(15)
	t.right(90)
	t.forward(17.5)
	t.left(90)
	t.forward(2.5)
	t.left(90)
	t.forward(20)
	t.end_fill()
	t.hideturtle()
	
def posdouze(b, t, v_tk_speed):
	x_d = -6
	y_d = 155
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.forward(35)
	t.left(130)
	t.forward(25)
	t.left(90)
	t.forward(2.5)
	t.left(90)
	t.forward(20)
	t.left(-130)
	t.forward(30)
	t.left(90)
	t.forward(2.25)
	t.end_fill()
	t.penup()
	t.forward(27.5)
	t.down()
	t.begin_fill()
	t.left(90)
	t.forward(2.5)
	t.left(90)
	t.forward(17.5)
	t.right(90)
	t.forward(12.5)
	t.right(90)
	t.forward(17.5)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(2.5)
	t.left(90)
	t.forward(17.5)
	t.right(90)
	t.forward(15)
	t.right(90)
	t.forward(17.5)
	t.left(90)
	t.forward(17.5)
	t.left(90)
	t.forward(20)
	t.end_fill()
	t.hideturtle()
	
def possix(b, t, v_tk_speed):
	x_d = -8
	y_d = -173
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.right(0)
	t.forward(17.5)
	t.right(90)
	t.forward(17.5)
	t.right(90)
	t.forward(20)
	t.right(90)
	t.forward(35)
	t.right(90)
	t.forward(20)
	t.right(90)
	t.forward(2.5)
	t.right(90)
	t.forward(17.5)
	t.left(90)
	t.forward(30)
	t.left(90)
	t.forward(15)
	t.left(90)
	t.forward(12.5)
	t.left(90)
	t.forward(15)
	t.end_fill()
	t.hideturtle()

def posneuf(b, t, v_tk_speed):
	x_d = -165
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.right(0)
	t.forward(17.5)
	t.right(90)
	t.forward(17.5)
	t.right(90)
	t.forward(20)
	t.right(90)
	t.forward(35)
	t.right(90)
	t.forward(20)
	t.right(90)
	t.forward(2.5)
	t.right(90)
	t.forward(17.5)
	t.left(90)
	t.forward(30)
	t.left(90)
	t.forward(15)
	t.left(90)
	t.forward(12.5)
	t.left(90)
	t.forward(15)
	t.end_fill()
	t.hideturtle()
		
def aiguillem(a, b, t, v_tk_speed):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*6)
	t.color(b)
	t.begin_fill()
	t.forward(2.5)
	t.left(90)
	t.forward(125)
	t.right(90)
	t.forward(12.5)
	t.left(135)
	t.forward(21)
	t.left(90)
	t.forward(21)
	t.left(135)
	t.forward(12.5)
	t.right(90)
	t.forward(125)
	t.left(90)
	t.forward(2.5)
	t.end_fill()
	t.hideturtle()
	
def aiguillem1(a, b, t, v_tk_speed):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*6)
	t.color(b)
	t.begin_fill()
	t.forward(2.5)
	t.left(90)
	t.forward(125)
	t.left(10)
	t.forward(15)
	t.left(160)
	t.forward(15)
	t.left(10)
	t.forward(125)
	t.left(90)
	t.forward(2.5)
	t.end_fill()
	t.hideturtle()
	
def aiguillem2(a, b, t, v_tk_speed):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*6)
	t.color(b)
	t.begin_fill()
	t.forward(2.5)
	t.left(91)
	t.forward(140)
	t.left(178)
	t.forward(140)
	t.left(91)
	t.forward(2.5)
	t.end_fill()
	t.hideturtle()
	
def aiguilleh(a, b, t, v_tk_speed):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*30)
	t.color(b)
	t.begin_fill()
	t.forward(5)
	t.left(90)
	t.forward(100)
	t.right(90)
	t.forward(10)
	t.left(135)
	t.forward(21)
	t.left(90)
	t.forward(21)
	t.left(135)
	t.forward(10)
	t.right(90)
	t.forward(100)
	t.left(90)
	t.forward(5)	
	t.end_fill()
	t.hideturtle()
	
def aiguilleh1(a, b, t, v_tk_speed):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*30)
	t.color(b)
	t.begin_fill()
	t.forward(5)
	t.left(90)
	t.forward(90)
	t.left(20)
	t.forward(15)
	t.left(140)
	t.forward(15)
	t.left(20)
	t.forward(90)
	t.left(90)
	t.forward(5)
	t.end_fill()
	t.hideturtle()
	
def aiguilleh2(a, b, t, v_tk_speed):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*30)
	t.color(b)
	t.begin_fill()
	t.forward(5)
	t.left(93)
	t.forward(90)
	t.left(174)
	t.forward(90)
	t.left(93)
	t.forward(5)
	t.end_fill()
	t.hideturtle()