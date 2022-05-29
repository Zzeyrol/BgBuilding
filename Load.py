from tkinter import *
from Card import *
from Board import *

class Load():
	def __init__(self,root,app,canvas):
		self.view = app
		self.canvas = canvas
		self.loading()

	def loading(self):
		x = 180
		o = x * self.view.card
		self.sss = []
		f = open("combination.txt")
		test = f.read()
		for test in test:
			if test != ';':
				self.sss.append(test)
			if test ==';':
				self.d = ''.join(self.sss)
				self.imgload()
				self.sss = []
				print(self.d)
			else:
				f.close()

	def imgload(self):
		img = PhotoImage(file ='pics/' + globals()[self.d].image + '.png').subsample(2)
		self.canvas.create_image(10,50,anchor='nw',image= img)
		print(img)


