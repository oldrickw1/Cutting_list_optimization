# Cutting_list_optimization
Visualizes different cutting solutions for a given set of boards and value table with tkinter GUI

# Requirements:
PIL
CV2
Numpy

# Module Description:

# Board_generator.py
Generates random boards with realistic quality-lenght sections

# Color_reference.py
Contians the color reference table used for the visualization

# final.py
The 'final' solution. This approach is different than the other algorithms and stands on its own. 
Takes another input formatting as the other algo's: [1,1,1,2,2] instead of [[1,3],[2,2]]

# gui_basic.py
The gui app. This is where the functionality of all modules comes together. Assortment values should be changed here if required.

# helper_funcs.py
get_values and some other functions live here. Were seperated from gui_basic.py to prevent clutter.

# optimization.py
uses the tables from tabulation.py to get the best solution for a given board.

# planktype.py
A class for plank types. Used to make plank instances with, which are used to get better access to data. 

# tabulation.py
Uses DP to tabulate tables for each category.

# testing.py
Some code to test and print the efficiency of the algorithms. 

# visualization.py
Uses opencv to visualize the input and output boards.
