from tkinter import *
from Card import *

class Board():
	def __init__(self,app,name):
		self.view = app
		self.serch(name)

	def serch(self,name):
		hp = globals()[name].hp
		dmg = globals()[name].dmg
		self.view.hp = self.view.hp + hp
		self.view.dmg = self.view.dmg + dmg
		self.view.all_hp.config(text='All Hp = ' + str(self.view.hp))
		self.view.all_dmg.config(text='All Dmg = ' + str(self.view.dmg))
		self.view.combinatio = self.view.combinatio + str(name) +';'