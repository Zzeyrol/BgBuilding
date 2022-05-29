from tkinter import *
from Card import *
from Board import *

class CardSelect(Toplevel):
	def __init__(self,root,app,canvas):
		super().__init__(root)
		self.view = app
		self.canvas = canvas
		self.window()

	def window(self):
		self.title('Card Select')
		self.geometry('400x300')
		self.resizable(False,False)

		self.bg = Canvas(self,width=350,height=300)
		self.bg.pack(fill='both',expand=True)
		self.bg.create_image(-200,-200,anchor='nw',image=self.view.bg)

		self.all_cards = Listbox(self,bg = '#D9C69B',bd=1,selectmode = SINGLE)
		self.all_cards.place(x=5,y=50, height=240,width=200)
		
		add_list = list_name
		for add_list in add_list:
			self.all_cards.insert(END,add_list)

		select = Button(self,bg = '#D9C69B',text = 'Добавить',command = self.select_card)
		select.place(x=250,y=260,height=30,width=100)

		entry = Entry(self,bd = 2)
		entry.place(x=5,y=10,height=30,width=200)

		def card_show(event):
			itm = self.all_cards.curselection()[0]
			self.name = self.all_cards.get(ANCHOR)
			self.img = PhotoImage(file ='pics/' + globals()[list_name[itm]].image + '.png').subsample(2)
			time_img = self.bg.create_image(210,0,anchor='nw',image= self.img)

		self.all_cards.bind('<<ListboxSelect>>',card_show)

		def scankey(event):
			add_list = list_name
			val = event.widget.get()
			if val == '':
				data = add_list
			else:
				data = []
				for item in add_list:
					if val.lower() in item.lower():
						data.append(item)
			update(data)

		def update(data):
			self.all_cards.delete(0, END)
			for item in data:
				self.all_cards.insert(END, item)

		entry.bind('<KeyRelease>', scankey)

	def bord(self,name):
		Board(self.view,self.name)

	def select_card(self):
		self.bord(self.name)
		x = 180
		o = x * self.view.card
		self.canvas.create_image(10 + o,450,anchor='nw',image= self.img)
		self.view.card += 1
		self.destroy()