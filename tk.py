#!usr/bin/python
import tkinter as tk
from tkinter import *
class ui:
	def __init__(self):
		self.root=tk.Tk()
		self.l,self.b = 400,400
		self.root.title('Calc')
		self.res1 = Label(self.root)
		self.root.geometry("{}x{}".format(self.l,self.b))
		self.createwidgets()
		self.root.mainloop()

	def add1(self):
		self.res1.destroy()
		data1=int(self.num1.get())
		data2=int(self.num2.get())
		res=data1+data2
		self.res1 = Label(self.root, text=res)
		self.res1.place(x=self.l/2, y=(2*self.l)/3)

	def sub1(self):
		self.res1.destroy()
		data1=int(self.num1.get())
		data2=int(self.num2.get())
		res=data1-data2
		self.res1 = Label(self.root, text=res)
		self.res1.place(x=self.l/2, y=(2*self.l)/3)

	def mul1(self):
		self.res1.destroy()
		data1=int(self.num1.get())
		data2=int(self.num2.get())
		res=data2*data1
		self.res1 = Label(self.root, text=res)
		self.res1.place(x=self.l/2, y=(2*self.l)/3)

	def div1(self):
		self.res1.destroy()
		data1=int(self.num1.get())
		data2=int(self.num2.get())
		res=data1/data2
		self.res1 = Label(self.root, text=res)
		self.res1.place(x=self.l/2, y=(2*self.l)/3)
		
	def createwidgets(self):
		self.num1=Entry(self.root)
		self.num2 = Entry(self.root)
		self.num1.place(x=self.l/5, y=self.b/3)
		self.num2.place(x=self.l/2, y=self.b/3)


		'''self.text1.place(x=self.l/5, y=self.b/4)
		self.text2.place(x=self.l/2, y=self.b/4)'''

		self.add = Button(self.root, text="Add", command=self.add1)
		self.sub = Button(self.root, text="Subtract", command=self.sub1)
		self.mul = Button(self.root, text="Multiply", command=self.mul1)
		self.div = Button(self.root, text="Divide", command=self.div1)

		self.add.place(x=self.l/5,y=200)
		self.sub.place(x=self.l/5,y=230)
		self.mul.place(x=self.l/5,y=260)
		self.div.place(x=self.l/5,y=290)

if __name__ == '__main__':
	x = ui()