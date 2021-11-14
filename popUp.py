# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:20:42 2021
@author: Kaushal Vashisth
"""
import tkinter
from tkinter import *
import csv
import tkinter.ttk as ttk
#import time

window=tkinter.Tk()
# to rename title
window.title("Importing csv data")
#window size
width=500
height=500

window.geometry('%dx%d' % (width,height))
window.resizable(True,True)

#creating table
#def getTable(column_names)
TableMargin=Frame(window,width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("date", "symbol", "% change"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('date', text="Date", anchor=W)
tree.heading('symbol', text="Symbol", anchor=W)
tree.heading('% change', text="Change%", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

#pack is used to show the object in the window
#label=tkinter.Label(window,text="Hello World").pack()

#open csv file
with open('Indices stats.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        date=row['date']
        symbol=row['symbol']
        change=row['% change']
        tree.insert("",0, values=(date,symbol,change))
        
if __name__ == '__main__':
    window.after(30000, lambda: window.destroy())
    window.mainloop()
    

