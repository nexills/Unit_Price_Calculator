# a item price comparator

import tkinter as tk
import function as fn

def calculate(item):
    # item is a item object
    # this function calculate the unit_price of an item using data
    # stored in it, and display the result to the label in the item
    try: 
        price = float(item.price.get())
        size = float(item.size.get())
        discount = float(item.discount.get())
    except ValueError:
        item.resultlabel['text'] = 'Field(s) are empty!'
    else:
        unit_price = price/size * (1-discount)
        item.resultlabel['text'] = str(round(unit_price, 4))
    finally:
        item.resultlabel.grid(row=item.row+3, column=item.col+1)

def calculate_all(item_list):
    calculate(item_list[0])
    minimum = float(item_list[0].resultlabel['text'])
    min_index = 0
    for i in range(1, len(item_list)):
        calculate(item_list[i])
        if (float(item_list[i].resultlabel['text']) < minimum):
            minimum = float(item_list[i].resultlabel['text'])
            min_index = i
    result = tk.Label(gui, text='Cheapest: ' + str(min_index), font=std_font)
    result.grid(row=11, column=1)



if __name__ == '__main__':
    gui = tk.Tk()
    # set up the window
    gui.geometry("600x800")
    gui.title("Calculator")
    # set up the gui elements
    std_font = ('calibre',14,'normal') # define this as the standard font

    item_1 = fn.item(gui, std_font)
    item_1.create(0,0)
    item_2 = fn.item(gui, std_font)
    item_2.create(5,0)
    item_list = [item_1, item_2]
    execute = tk.Button(gui, text='Calculate', font=std_font, 
                        command=lambda: calculate_all(item_list))
    execute.grid(row=10, column=1)



    
    gui.mainloop()

    
