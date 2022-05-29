import cv2 as cv
import tabulation
import optimization
import visualization
import helper_funcs


# DUMMY DATA 
assortment =[[1,'1L',9,12],[1,'1S',5,4],[2,'2L',9,8],[2,'2S',5,3],[3,'3L',9,5],[3,'3S',5,1]] # [quality, symbol/name, length, value]
table_size = 50
boards_input = [[[2,7],[1,5],[3,1]], [[1,30], [4,3], [2,8]]] # [quality, length] 
dimensioned = True

# Algorithms
algorithms = ['algo_naive', 'join_algorithm', 'join_where_algorihm', 'demote_join_where_algorithm']


# Get the table, a (3 by table_size) matrix. 
table = tabulation.get_table(assortment, table_size)

# Get the optimized boards.
user_algorithm = int(input("Choose algorithm for optimization. \n\n1 for naive_algorithm, \n2 for join_algorithm, \n3 for join_where_algorithm, \n4 for demote_join_where_alorithm\n\n>>>  "))
print(f'Chosen algorithm: {algorithms[user_algorithm-1]}')
boards_optimized = optimization.get_optimized_boards(boards_input, table, algorithms[user_algorithm-1])
board_values = helper_funcs.get_values(boards_optimized, assortment)  
total_value = sum(board_values)

print()
print(f'\nTotal boards optimized: {len(boards_optimized)}\nTotal value after optimization: {total_value}')

board_lens = helper_funcs.get_board_lens(boards_input)

# # Get the before and after images.
boards_input_img = visualization.get_image(boards_input, board_lens, dimensioned=dimensioned)
boards_optimized_img = visualization.get_image(boards_optimized, board_lens, board_values, total_value, dimensioned=dimensioned)



cv.imshow('Input', boards_input_img)
cv.imshow('Optimized', boards_optimized_img)

cv.waitKey(0)
cv.destroyAllWindows()