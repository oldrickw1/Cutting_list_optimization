import cv2 as cv
import tkinter as tk

from numpy import imag, pad
import tabulation
import optimization
import visualization
import helper_funcs
from PIL import ImageTk, Image
import board_generator
import final


# DUMMY DATA 
assortment =[[1,'1L',9,12],[1,'1S',5,4],[2,'2L',9,8],[2,'2S',5,3],[3,'3L',9,5],[3,'3S',5,1]] # [quality, symbol/name, length, value]
# assortment =[[1,'1L',5,6],[1,'1S',2,4],[2,'2L',5,5],[2,'2S',2,3]] # [quality, symbol/name, length, value]

table_size = 80
# boards_input = [[[1,13], [3,9], [2,6], [1,16]],[[1,13], [3,9], [2,6], [1,16]]]
boards_input = board_generator.get_random_boards(4)
# boards_input = [[[2,6], [3,4]]] # [quality, length] 
# boards_input = [[[1,9]],[[1,5]], [[2,9]], [[2,5]], [[3,9]], [[3,5]]]
dimensioned = True
# [1,'1M',7,8]      extra category (for demo)



root = tk.Tk()
root.title("Cutting Optimization Basic")

width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

# Get before boards
table = tabulation.get_table(assortment, table_size)
board_lens = helper_funcs.get_board_lens(boards_input)
boards_input_img = visualization.get_image(boards_input, board_lens, dimensioned=dimensioned)
cv.imwrite('input.jpg', boards_input_img)
input_img = ImageTk.PhotoImage(Image.open('input.jpg'))

def get_new_boards():
    # Get before boards
    after_img_label.config(image='')
    after_img_label_announce.config(text=" ")
    table = tabulation.get_table(assortment, table_size)
    global boards_input
    boards_input = board_generator.get_random_boards(4)
    board_lens = helper_funcs.get_board_lens(boards_input)
    boards_input_img = visualization.get_image(boards_input, board_lens, dimensioned=dimensioned)
    cv.imwrite('input.jpg', boards_input_img)
    input_img = ImageTk.PhotoImage(Image.open('input.jpg'))
    before_img_label.config(image=input_img)
    before_img_label.img = input_img
    
    


def optimize(algo):
    table = tabulation.get_table(assortment, table_size)
    boards_optimized = optimization.get_optimized_boards(boards_input, table, algo)
    board_values = helper_funcs.get_values(boards_optimized, assortment)  
    total_value = sum(board_values)
    
    boards_optimized_img = visualization.get_image(boards_optimized, board_lens, board_values, total_value, dimensioned=dimensioned)
    cv.imwrite('output.jpg', boards_optimized_img)
    output_img = ImageTk.PhotoImage(Image.open('output.jpg'))
    after_img_label.config(image=output_img)
    after_img_label.img = output_img

    after_img_label_announce.config(text='Optimized with: ' +algo)

def optimize_optimal():
    # format boards
    to_be_formatted = boards_input.copy()
    formatted_boards = []
    for board in to_be_formatted:
        formatted_board = []
        for section in board:
            formatted_board += [section[0]] * section[1]
        formatted_boards.append(formatted_board)


    optimal_boards = []
    for board in formatted_boards:
        optimal_board = final.get_optimal(board, assortment)
        optimal_boards.append(optimal_board)
    print(optimal_boards)
    
    boards_values = helper_funcs.get_values(optimal_boards, assortment)
    total_value = sum(boards_values)

    boards_optimized_img = visualization.get_image(optimal_boards, board_lens, boards_values, total_value, dimensioned)
    cv.imwrite('output.jpg', boards_optimized_img)
    output_img = ImageTk.PhotoImage(Image.open('output.jpg'))
    after_img_label.config(image= output_img)
    after_img_label.img = output_img

    after_img_label_announce.config(text='Optimized with: Optimal_algo')


# Widgets
aside_frame = tk.Frame(root, padx=30, pady=55)
aside_frame.grid(row=0, column=0, sticky=tk.N)

board_frame = tk.Frame(root, pady=30)
board_frame.grid(row=0, column=1)

before_img_label_announce = tk.Label(board_frame, text="Input:")
before_img_label_announce.grid(row=0,column=0, sticky=tk.W)

before_img_label = tk.Label(board_frame, image=input_img)
before_img_label.grid(row=1,column=0, pady=10, sticky=tk.W)

after_img_label_announce = tk.Label(board_frame, text="Optimized:")
after_img_label_announce.grid(row=2,column=0, sticky=tk.W)

after_img_label = tk.Label(board_frame)
after_img_label.grid(row=3,column=0, pady=10)

optimize_naive_button = tk.Button(aside_frame, text="naive_optimize", command=lambda: optimize('algo_naive'))
optimize_naive_button.grid(row=0, column=0,pady=4)

optimiz_join_button = tk.Button(aside_frame, text="join_optimize", command=lambda: optimize('join_algo'))
optimiz_join_button.grid(row=1, column=0, pady=4)

optimize_where_button = tk.Button(aside_frame, text="where_join_optimize", command=lambda: optimize('where_join_algo'))
optimize_where_button.grid(row=2, column=0, pady=4)

optimize_optimal_button = tk.Button(aside_frame, text="Optimal_algo", command= optimize_optimal)
optimize_optimal_button.grid(row=3, column=0, pady=4)

get_new_boards_button = tk.Button(aside_frame, text='Get new boards', command=get_new_boards)
get_new_boards_button.grid(row=5, column=0, pady=30)





root.mainloop()
