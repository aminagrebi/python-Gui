'''
Dec 25,  2017
Recipe:  B04829_01_01
@author: Amin Agrebi
'''
#======================
# imports
#======================
import tkinter as tk
from  tkinter import Menu

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")

# Creating a Menu Bar
menuBar = Menu(win)
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
menuBar.add_cascade(label="File", menu=fileMenu)

#======================
# Start GUI
#======================
win.mainloop()
