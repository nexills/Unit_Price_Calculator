# a item price comparator

import tkinter as tk
import function as fn

def calculate_all(item_list):
    # calculate every items and find the minimum
    minimum = -1
    min_index = -1
    for i in range(len(item_list)):
        item_list[i].calculate()
        try: 
            float(item_list[i].resultlabel['text'])
        except:
            # happens if some fields in the item is empty
            continue
        else:
            # set new minimum if less than or first item
            if (minimum == -1):
                minimum = float(item_list[i].resultlabel['text'])
                min_index = 0
            elif (float(item_list[i].resultlabel['text']) < minimum):
                minimum = float(item_list[i].resultlabel['text'])
                min_index = i
    if (min_index == -1):
        return
    result = tk.Label(gui, text='Cheapest item: item ' + str(min_index+1)
                      , font=std_font)
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

    
