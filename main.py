# a item price comparator

import tkinter as tk
import function as fn

def calculate(item, label):
    # item is a item object
    # row and column is where the result should be displayed
    # label is to label to save the result
    # this function calculate the unit_price of an item, and
    # save it in a label
    try: 
        price = float(item.price.get())
        size = float(item.size.get())
        discount = float(item.discount.get())
    except ValueError:
        label['text'] = 'Field(s) are empty!'
    else:
        unit_price = price/size * (1-discount)
        label['text'] = str(round(unit_price, 2))
    finally:
        label.grid(row=item.row+3, column=item.col+1)


if __name__ == '__main__':
    gui = tk.Tk()
    # set up the window
    gui.geometry("600x800")
    gui.title("Calculator")
    # set up the gui elements
    std_font = ('calibre',14,'normal') # define this as the standard font

    label = tk.Label(gui, text='', font=std_font)

    item_1 = fn.item(gui, std_font)
    item_1.create(0,0)
    item_2 = fn.item(gui, std_font)
    item_2.create(5,0)
    execute = tk.Button(gui, text='Calculate', font=std_font, 
                        command=lambda: calculate(item_1, label))
    execute.grid(row=10, column=1)



    
    gui.mainloop()

    
