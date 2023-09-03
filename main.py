# a item price comparator

import tkinter as tk
import function as fn

def calculate_all(item_list):
    # calculate every items and find the minimum
    minimum = -1
    min_index = -1
    for i in range(len(item_list)):
        item_list[i].calculate()
        if item_list[i].unit_price == -1:
            continue
        else:
            # set new minimum if less than or first item
            if (minimum == -1):
                minimum = item_list[i].unit_price
                min_index = 0
            elif (item_list[i].unit_price < minimum):
                minimum = item_list[i].unit_price
                min_index = i
    if (min_index == -1):
        return
    try:
        if (min_index == 0):
            cheaper_by = item_list[1].unit_price - item_list[0].unit_price
            cheaper_by /= item_list[1].unit_price
        elif (min_index == 1):
            cheaper_by = item_list[0].unit_price - item_list[1].unit_price
            cheaper_by /= item_list[0].unit_price
    except:
        # avoid division by zero
        cheaper_by = 0
    result = tk.Label(gui, text='Cheaper item: item ' + str(min_index+1
                        ) + " by " + str(round(cheaper_by*100, 2)) + "%"
                      , font=std_font)
    result.grid(row=16, column=0, columnspan=2)



if __name__ == '__main__':
    gui = tk.Tk()
    # set up the window
    gui.title("Calculator")
    # set up the gui elements
    std_font = ('calibre',18,'normal') # define this as the standard font

    item_1 = fn.item(gui, std_font, 1, 'lawngreen')
    item_1.create(0,0)
    item_2 = fn.item(gui, std_font, 2, 'cyan')
    item_2.create(6,0)
    item_list = [item_1, item_2]
    execute = tk.Button(gui, text='Calculate', font=std_font, 
                        command=lambda: calculate_all(item_list))
    execute.grid(row=15, column=1)


    gui.mainloop()

    
