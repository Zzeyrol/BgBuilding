from tkinter import *
list_name = []
class Card():
	def __init__(self,name,hp,dmg,tier,fractia,image,gold = False):
		super().__init__()
		self.name = name
		self.hp = hp
		self.dmg = dmg
		self.image = image
		self.tier = tier
		self.fractia = fractia
		list_name.append(self.image)

pir = Card ('pir',4,4,4,'Пират','pir')
kap = Card ('kap',2,2,1,'Элемнталь','kap')
crab = Card('crab',4,4,5,'None','crab')