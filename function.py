
import tkinter as tk

class item:

    # class atributes

    def __init__(self, gui, std_font):   
        self.price = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                              justify="right")
        self.size = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                             justify="right")
        self.discount = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                                 justify="right")
        self.percentage = tk.Label(gui, text='%', font=std_font)
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
        self.percentage.grid(row=row+2, column=col+2)
        self.row = row
        self.col = col

    def calculate(self):
    # this function calculate the unit_price of an item using data
    # stored in it, and display the result to the label in the item
        try: 
            price = float(self.price.get())
            size = float(self.size.get())
            discount = float(self.discount.get())
        except ValueError:
            # happens when some fields are empty
            self.resultlabel['text'] = 'Field(s) are empty!'
        else:
            unit_price = price/size * (1-discount*0.01)
            self.resultlabel['text'] = str(round(unit_price, 4))
        finally:
            self.resultlabel.grid(row=self.row+3, column=self.col+1)    


