
from tkinter import*  # noqa: F403
import tkinter
from tkinter import ttk
from turtle import color  # noqa: F401

width = 800
heigh = 600
grid_size = 20


class square:

	"""docstring for square"""
	def __init__(self):
		self.x = x
		self.y = y
		self.color = color
		self.velx = 0
		self.vely = 0
		self.dim = [0, 0, 0,grid_size, grid_size, grid_size, 0]


	def setVel(self, newx, newy):
		self.velx = newx
		self.vely = newy

	def pos(self):
		return [self.dim[0] + self.x, self.dim[1] + self.y,self.dim[2] + self.x, self.dim[3] + self.y, self.dim[4] + self.x, self.dim[5] + self.y, self.dim[6] + self.x, self.dim[7] + self.y]


	def update(self):
		if (self.x>0 and self.x<width-grid_size):
			self.x += self.velx
		if (self.y>0 and self.y<heigh-grid_size):
			self.y += self.vely
		if (self.x==0 and self.x>0):
			self.x += self.velx
		if (self.x==width-grid_size and self.velx<0):
			self.x += self.velx
		if (self.x==0 and self.x>0):
			self.y += self.vely
		if (self.y==width-grid_size and self.y<0):
			self.y += self.vely


class Game:
		
	def __init__(self):
		self.window = ttk()
		self.canvas = Canvas(self.window, bg='black', width=width, heigh=heigh)  # noqa: F405
		self.canvas.pack()

		self.s = square(20, 20, 'white')
		self.s.velx = 20
		self.s.vely = 0

	
	def run(self):
		while(true):
			self.canvas.delete('all')
			self.canvas.create_polygon(self.s.pos(), fill=self.s.color)
			self.s.update()

			self.canvas.after(70)
			self.window.update_idletasks()
			self.window.update()



g = Game()
g.run()
