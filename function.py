
import tkinter as tk

class item:

    def __init__(self, gui, std_font):   
        self.price = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                              justify="right")
        self.size = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                             justify="right")
        self.discount = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                                 justify="right")
        self.pricelabel = tk.Label(gui, text='Price:', font=std_font)
        self.sizelabel = tk.Label(gui, text='Size(g/lb/etc.):', font=std_font)
        self.discountlabel = tk.Label(gui, text='Discount:', font=std_font)
        self.row = -1
        self.col = -1
        self.resultlabel = tk.Label(gui, text='', font=std_font)

    def create(self, row, col):
        self.price.grid(row=row, column=col + 1)
        self.size.grid(row=row + 1, column=col + 1)
        self.discount.grid(row=row + 2, column=col + 1)
        self.pricelabel.grid(row=row, column=col)
        self.sizelabel.grid(row=row + 1, column=col)
        self.discountlabel.grid(row=row + 2, column=col)
        self.row = row
        self.col = col


