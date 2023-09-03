
import tkinter as tk

class item:

    # class atributes

    def __init__(self, gui, std_font, number, colour):
        # setting up labels and entries   
        self.price = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                              justify="right", width = 7)
        self.size = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                             justify="right", width = 7)
        self.discount = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                                 justify="right", width = 7)
        self.num_items = tk.Entry(gui, bg='grey', fg='white', font=std_font, 
                                 justify="right", width = 7)
        self.title = tk.Label(gui, text='Item ' + str(number), font=std_font,
                              bg = colour)
        self.percentage = tk.Label(gui, text='%', font=std_font, width = 1)
        self.pricelabel = tk.Label(gui, text='Price:', font=std_font,
                              bg = colour)
        self.sizelabel = tk.Label(gui, text='Size(g/lb/etc.):', font=std_font,
                              bg = colour)
        self.numlabel = tk.Label(gui, text='Number of items:', font=std_font,
                              bg = colour)
        self.discountlabel = tk.Label(gui, text='Discount:', font=std_font,
                              bg = colour)
        self.row = -1
        self.col = -1
        # special labels
        self.resultlabel = tk.Label(gui, text='', font=std_font)
        # default entry values
        self.price.insert(tk.END, '0')
        self.size.insert(tk.END, '1')
        self.discount.insert(tk.END, '0')
        self.num_items.insert(tk.END, '1')

    def create(self, row, col):
        # put everything on screen
        self.title.grid(row=row, column=col, sticky='nsew', columnspan=2)
        self.price.grid(row=row+1, column=col + 1, sticky='nsew')
        self.size.grid(row=row + 2, column=col + 1, sticky='nsew')
        self.discount.grid(row=row + 4, column=col + 1, sticky='nsew')
        self.pricelabel.grid(row=row+1, column=col, sticky='nsew')
        self.sizelabel.grid(row=row + 2, column=col, sticky='nsew')
        self.discountlabel.grid(row=row + 4, column=col, sticky='nsew')
        self.percentage.grid(row=row+4, column=col+2, sticky='nsew')
        self.num_items.grid(row=row+3, column=col+1, sticky='nsew')
        self.numlabel.grid(row=row+3, column=col, sticky='nsew')
        self.row = row
        self.col = col

    def calculate(self):
    # this function calculate the unit_price of an item using data
    # stored in it, and display the result to the label in the item
        try: 
            price = float(self.price.get())
            size = float(self.size.get())
            discount = float(self.discount.get())
            num_items = float(self.num_items.get())
        except ValueError:
            # happens when some fields are empty or have non-numbers
            self.resultlabel['text'] = 'Illegal values!'
            self.unit_price = -1
        else:
            self.unit_price = price/size * (1-discount*0.01) / num_items
            self.resultlabel['text'] = '$' + str(round(self.unit_price, 4)) + '/unit'
        finally:
            self.resultlabel.grid(row=self.row+5, column=self.col+1)    


