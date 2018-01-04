#!usr/bin/python
from tkinter import *
import tkinter as tk

#ramachandra1

class ui:
	def __init__(self):
		self.root=tk.Tk()
		self.l, self.b = 500, 333
		self.root.title('Insurance Prediction')
		self.root.geometry("{}x{}".format(self.l,self.b))
		# self.coverimg = PhotoImage(file='cover.png')
		# self.cover = Label(self.root, image=self.coverimg)
		# self.cover.place(x=0, y=0)
		self.createwidgets()
		self.root.mainloop()

	def camact(self):
		pass

	def exploreract(self):
		pass

	def bookcab(self):
		pass

	def smshome(self):
		pass

	def smscolleage(self):
		pass

	def createwidgets(self):

		self.camimage = PhotoImage(file='camera.png')
		self.explorerimage = PhotoImage(file='explorer.png')
		
		self.cam = Button(self.root, compound=CENTER, image=self.camimage, command=self.camact, height=80, width=80)
		self.cam.place(x=150,y=40)

		self.explorer = Button(self.root, compound=CENTER, image=self.explorerimage, command=self.exploreract, height=80, width=80)
		self.explorer.place(x=250,y=40)

		self.cab = Button(self.root, text='Book a Cab', compound=CENTER, command=self.bookcab, width=25)
		self.cab.place(x=150, y=170)

		self.smshome = Button(self.root, text='Send SMS to Home', compound=CENTER, command=self.smshome, width=25)
		self.smshome.place(x=150, y=210)

		self.smscolleage = Button(self.root, text='Send SMS to colleague', compound=CENTER, command=self.smscolleage, width=25)
		self.smscolleage.place(x=150, y=250)

if __name__ == '__main__':
	x = ui()