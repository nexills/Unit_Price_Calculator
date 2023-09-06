# Unit_Price_Calculator

A simple calculator to calculate which stores sell some items the cheapest.

By entering the total price, size (grams, lb, kg, etc.) per pack, number of packs, and discount (eg. credit card cash back, membership rebate), this calculator can calculate the price per unit and compare the cost between two different packages.

# Progress
The calculator is complete.

# Background
I often see different shops selling the same item in different packages, for different prices. For instance, one shop may sell 3 packs of ships, 210g each, for $10, while the other sell 2 packs of 290g chips for $8 - this makes it difficult to get the best deals.
Therefore, I built this calculator to automatically calculate and compare the unit price of different items.

# Build Instructions (Windows)
1. Install Python and Pip
2. In Command Prompt, enter py -m pip install pyinstaller
3. Change directory to the location where the repo is downloaded
4. Run py -m PyInstaller main.py
5. Go to ./dist/main/
6. Run main.exe
