import tkinter as tk
from tkinter import ttk

from Card_select import CardSelect
from Card import *
from Board import *
from Load import *

class Main(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.init_main()

	def init_main(self):

		self.bg = tk.PhotoImage(file = 'pics/bg2.png')
		self.canvas = tk.Canvas(root,width=1280,height=720)
		self.canvas.pack(fill='both',expand=True)
		self.canvas.create_image(0,0,anchor='nw',image=self.bg)

		add_card = tk.Button(self.canvas,borderwidth=0,text='Добавить карту',bg = '#AC9E7F',bd=1,compound=tk.TOP,command=self.card_select)
		add_card.place(relx=0.01,rely=0.01,relwidth=0.14,relheight=0.08)

		self.all_hp = Label(self.canvas,bg = '#AC9E7F',text = 'All Hp = 0')
		self.all_hp.place(x=200,y=15,width=70,height=40)

		delite_all = tk.Button(self.canvas,borderwidth=0,text='Очистить',bg = '#AC9E7F',bd=1,compound=tk.TOP,command=self.all_del)
		delite_all.place(x=12,y=80,relwidth=0.14,relheight=0.08)

		self.all_dmg = Label(self.canvas,bg = '#AC9E7F',text = 'All Dmg = 0')
		self.all_dmg.place(x=200,y=75,width=70,height=40)

		self.save = tk.Button(self.canvas,borderwidth=0,text='Сохранить комбинацию',bg='#AC9E7F',bd=1,compound=tk.TOP,command=self.save)
		self.save.place(x=1020,y=80,relwidth=0.14,relheight=0.08)

		self.lod = tk.Button(self.canvas,borderwidth=0,text='Загрузить комбинацию',bg='#AC9E7F',bd=1,compound=tk.TOP,command=self.load)
		self.lod.place(x=1020,y=10,relwidth=0.14,relheight=0.08)		

		self.card = 0
		self.hp = 0
		self.dmg = 0
		self.combinatio = ''

	def save(self):
		f = open("combination.txt","w")
		f.write(self.combinatio)

	def load(self):
		Load(root,app,self.canvas)

	def card_select(self):
		CardSelect(root,app,self.canvas)

	def all_del(self):
		self.hp = 0
		self.dmg = 0
		self.card = 0
		self.all_hp.config(text='All Hp = 0')
		self.all_dmg.config(text='All Dmg = 0')
		self.canvas.delete('all')
		self.canvas.create_image(0,0,anchor='nw',image=self.bg)

if __name__ == "__main__":
	root = tk.Tk()
	app = Main(root)
	app.pack()
	root.title('Программа')
	root.geometry('1200x720')
	root.resizable(False, False)
	root.mainloop()