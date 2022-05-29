from typing_extensions import IntVar
import cv2 as cv
import tkinter as tk
import tabulation
import optimization
import visualization
import helper_funcs
from PIL import ImageTk, Image

import ast

root = tk.Tk()
root.title("Cutting Optimization Advanced")

width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

# DEFAULT VALUES / DUMMY DATA 

default_assortment =[[1,'1L',9,12],[1,'1S',5,4],[2,'2L',9,8],[2,'2S',5,3],[3,'3L',9,5],[3,'3S',5,1]] # [quality, symbol/name, length, value]
default_table_size = 50
default_boards_input = [[[2,7],[1,5],[3,1]], [[1,30], [4,3], [2,8]]] # [quality, length] 
dimensioned = True


algorithms = ['algo_naive', 'join_algo', 'where_join_algo','demote_where_join_algo']

# Optimize the input boards, get results
def optimize_boards(algorithm):
    table = tabulation.get_table(assortment, int(table_size))
    boards_optimized = optimization.get_optimized_boards(boards_user_input, table, algorithm)
    board_values = helper_funcs.get_values(boards_optimized, assortment)  
    total_value = sum(board_values)
    boards_optimized_img = visualization.get_image(boards_optimized, board_lens, board_values, total_value, dimensioned=dimension_lines)
    cv.imwrite('output.jpg', boards_optimized_img)

    # Board after:
    board_after_announce.config(text=f"Boards optimized with {algorithm}:")
    output_img = ImageTk.PhotoImage(Image.open('output.jpg'))
    output_img_label = tk.Label(board_display_frame, image=output_img)
    output_img_label.grid(row=5, column=0, columnspan= 4, padx=30, pady=20)
    output_img_label.img = output_img



# Enter and make the input boads
def enter_board():
    global boards_user_input
    incorrect_board_input.grid_remove()
    if (boards_entry.get() == ''):
        if boards_user_input == []:
            boards_user_input = default_boards_input
        else:
            boards_user_input = boards_user_input
    else:
        try:   
            arr = boards_entry.get()
            arr = ast.literal_eval(arr) 
            boards_user_input.append(arr)
        except:
            for widget in board_display_frame.winfo_children():
                widget.grid_remove()
            incorrect_board_input.grid(row=0,column=0)
            return
    boards_entry.delete(0,'end')
    global board_lens
    board_lens = helper_funcs.get_board_lens(boards_user_input)

    boards_input_img = visualization.get_image(boards_user_input, board_lens, dimensioned=dimension_bool.get())
    cv.imwrite('input.jpg', boards_input_img)

    # Board Before:
    board_before_announcement.grid(row=0,column=0)

    input_img = ImageTk.PhotoImage(Image.open('input.jpg'))
    input_img_label = tk.Label(board_display_frame, image=input_img)
    input_img_label.grid(row=1, column=0, columnspan= 4, padx=30, pady=20)
    input_img_label.img = input_img

    # Add delete functionality
    delete_boards_button = tk.Button(board_display_frame, text="Delete all boards", command= delete_boards)
    delete_boards_button.grid(row=1, column=4)


    # Add 'optimize' functionality



def delete_boards():
    global boards_user_input
    boards_user_input = []
    for widget in board_display_frame.winfo_children():
        widget.grid_remove()
    
def make_board():
    enter_board()
    global assortment
    global table_size
    global dimension_lines
    if (assortment_entry.get()): 
        assortment = assortment_entry.get()
    else:
        assortment = default_assortment
    if (table_size_entry.get()):
        table_size = table_size_entry.get()
    else: 
        table_size = default_table_size
    dimension_lines = dimension_bool.get()

    # Display the algorithm buttons
    algo_announcement_label.grid(row=2, column=0, sticky=tk.W)
    naive_algo_button.grid(row=2, column=1, sticky=tk.W)
    join_algo_button.grid(row=2, column=2, sticky=tk.W)
    where_join_algo_button.grid(row=2, column=3, sticky=tk.W)
    demote_where_join_algo_button.grid(row=2, column=4, sticky=tk.W)


 


boards_user_input = []

# Frames
aside_frame = tk.Frame(root)
aside_frame.grid(row=0,column=0, sticky=tk.NW)

board_display_frame = tk.Frame(root, height=120, width=700)
board_display_frame.grid(row= 0, column=4, rowspan=9)

# Widgets for boards entry
boards_entry_usage = tk.Label(aside_frame, text="Enter board. Usage: [[quality, length], [quality, length],[...]]", padx=10,pady=10)
boards_entry_usage.grid(row=0, column=0, columnspan=3)

boards_entry_label = tk.Label(aside_frame, text="Board: ", padx=10, pady=10)
boards_entry_label.grid(row=1, column=0)

boards_entry = tk.Entry(aside_frame)
boards_entry.grid(row=1, column=1)

boards_entry_button = tk.Button(aside_frame, text='see board', command=enter_board)
boards_entry_button.grid(row=1, column=2)


# Widgets Assortment & table size
assortment_entry_label = tk.Label(aside_frame, text="Assortment:", padx=10,pady=10)
assortment_entry_label.grid(row=2,column=0)

assortment_entry = tk.Entry(aside_frame)
assortment_entry.grid(row=2,column=1)

assortment_entry_usage = tk.Label(aside_frame, text="Assortment: [quality(1-4), symbol('qlty+letter'), length, value]", padx=10)
assortment_entry_usage.grid(row=3, column=0, columnspan=3, padx=10)

table_size_label = tk.Label(aside_frame, text="Table size:", padx=10,pady=10)
table_size_label.grid(row=4,column=0)

table_size_entry = tk.Entry(aside_frame)
table_size_entry.grid(row=4,column=1)

dimension_lines_label = tk.Label(aside_frame, text="Dimension lines?",padx=10, pady=10)
dimension_lines_label.grid(row=5, column=0)

dimension_bool = tk.IntVar()
dimension_lines_checkbox = tk.Checkbutton(aside_frame, variable=dimension_bool)
dimension_lines_checkbox.grid(row=5, column=1)

submit_all_button = tk.Button(aside_frame, text="Make board", command=make_board)
submit_all_button.grid(row=6,column=1)




# Not visible at start
board_before_announcement = tk.Label(board_display_frame, text="Board(s) before: ")

board_after_announce = tk.Label(board_display_frame)
board_after_announce.grid(row=3, column=0)


# Algo_buttons
algo_announcement_label = tk.Label(board_display_frame, text="Choose optimization method:")

naive_algo_button = tk.Button(board_display_frame, text="Naive algorithm", command=lambda: optimize_boards(algorithms[0]), padx=0)
join_algo_button = tk.Button(board_display_frame, text="Join algorithm", command=lambda: optimize_boards(algorithms[1]))
where_join_algo_button = tk.Button(board_display_frame, text="Where_Join algorithm", command=lambda: optimize_boards(algorithms[2]))
demote_where_join_algo_button = tk.Button(board_display_frame, text="Demote_Where_Join algorithm", command=lambda: optimize_boards(algorithms[3]))


# Warnings:
incorrect_board_input = tk.Label(board_display_frame, text="Invalid input: must enter [[quality,length],..]", fg=r'red')

default_announcement_label = tk.Label(aside_frame, text="If not values are entered, default data will be used. Config in gui.py", padx=10, pady=10, fg='grey')
default_announcement_label.grid(row=9, column=0, columnspan=4)

default_boards_label = tk.Label(aside_frame, text="boards = " + str(default_boards_input), padx=10, fg='grey')
default_boards_label.grid(row=10, column=0, columnspan=4)   

default_assortment_label = tk.Label(aside_frame, text="assortment = " + str(default_assortment), padx=10, fg='grey')
default_assortment_label.grid(row=11, column=0, columnspan=4)  

default_table_size_label = tk.Label(aside_frame, text="table size = " + str(default_table_size), padx=10, fg='grey')
default_table_size_label.grid(row=12, column=0, columnspan=4)  



root.mainloop()



# Left of at adding algorithm buttons. They need more columnspace, and the before img should span wider. 