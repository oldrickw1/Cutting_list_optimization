import board_generator
import optimization
import tabulation
import helper_funcs
import final

assortment1 =[[1,'1L',9,12],[1,'1S',5,4],[2,'2L',9,8],[2,'2S',5,3],[3,'3L',9,5],[3,'3S',5,1]] # [quality, symbol/name, length, value]
assortment2 =[[1,'1L',5,7],[1,'1S',2,3],[2,'2L',5,4],[2,'2S',2,2]] 
table_size = 70

table1 = tabulation.get_table(assortment1, table_size)
table2 = tabulation.get_table(assortment2, table_size)

to_be_tested_boards = board_generator.get_random_boards(1000)

# format boards
to_be_formatted = to_be_tested_boards.copy()
formatted_boards = []
for board in to_be_formatted:
    formatted_board = []
    for section in board:
        formatted_board += [section[0]] * section[1]
    formatted_boards.append(formatted_board)





# Algo_naive

naive_optimized_boards1 = []
naive_optimized_boards2 = []
for board in to_be_tested_boards:
    naive_optimized_boards1.append(optimization.algo_naive(board, table1))
    naive_optimized_boards2.append(optimization.algo_naive(board, table2))

naive_optimized_board_values1 = helper_funcs.get_values(naive_optimized_boards1, assortment1)
naive_optimized_board_values2 = helper_funcs.get_values(naive_optimized_boards2, assortment2)

naive_val1 = sum(naive_optimized_board_values1)
naive_val2 = sum(naive_optimized_board_values2)



# Join_algo
join_optimized_boards1 = []
join_optimized_boards2 = []
for board in to_be_tested_boards:
    join_optimized_boards1.append(optimization.join_algo(board, table1))
    join_optimized_boards2.append(optimization.join_algo(board, table2))

join_optimized_board_values1 = helper_funcs.get_values(join_optimized_boards1, assortment1)
join_optimized_board_values2 = helper_funcs.get_values(join_optimized_boards2, assortment2)

join_val1 = sum(join_optimized_board_values1)
join_val2 = sum(join_optimized_board_values2)



# where_join_algo
where_join_optimized_boards1 = []
where_join_optimized_boards2 = []
for board in to_be_tested_boards:
    where_join_optimized_boards1.append(optimization.where_join_algo(board, table1))
    where_join_optimized_boards2.append(optimization.where_join_algo(board, table2))

where_join_optimized_board_values1 = helper_funcs.get_values(where_join_optimized_boards1, assortment1)
where_join_optimized_board_values2 = helper_funcs.get_values(where_join_optimized_boards2, assortment2)

where_join_val1 = sum(where_join_optimized_board_values1)
where_join_val2 = sum(where_join_optimized_board_values2)

# optimal algo:
optimal_optimized_boards1 = []
optimal_optimized_boards2 = []
for board in formatted_boards:
    optimal_optimized_boards1.append(final.get_optimal(board, assortment1))
    optimal_optimized_boards2.append(final.get_optimal(board, assortment2))

optimal_optimized_board_values1 = helper_funcs.get_values(optimal_optimized_boards1, assortment1)
optimal_optimized_board_values2 = helper_funcs.get_values(optimal_optimized_boards2, assortment2)

optimal_val1 = sum(optimal_optimized_board_values1)
optimal_val2 = sum(optimal_optimized_board_values2)





# Print results

print(f'Values:')
print()
print(f'assortment 1')
print('---------------------------------------------------')
print(f'algo_naive:             $ {naive_val1}           improvement relative to algo_naive (=100)')
print(f'join_algo:              $ {join_val1}           {round(100+float(((join_val1-naive_val1)/naive_val1)*100),2)}')
print(f'where_join_algo:        $ {where_join_val1}           {round(100+float(((where_join_val1-naive_val1)/naive_val1)*100), 2)}')
print(f'optimal:                $ {optimal_val1}           {round(100+float(((optimal_val1-naive_val1)/naive_val1)*100), 2)}')
print('\n'*2)

print(f'assortment 2')
print('---------------------------------------------------')
print(f'algo_naive:             $ {naive_val2}           improvement relative to algo_naive (=100)')
print(f'join_algo:              $ {join_val2}           {round(100+float(((join_val2-naive_val2)/naive_val2)*100), 2)}')
print(f'where_join_algo:        $ {where_join_val2}           {round(100+float(((where_join_val2-naive_val2)/naive_val2)*100),2)}')
print(f'optimal:                $ {optimal_val2}           {round(100+float(((optimal_val2-naive_val2)/naive_val2)*100), 2)}')

