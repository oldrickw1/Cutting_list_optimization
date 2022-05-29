'''optimization.py contains the algorithms with which the inputted boards can be optimized. Besides the boards, it requires a reference table, which should have already been made in tabulation.py.
The four algorithms are not DRY: they share a lot of the same code. This is done purposefully to better compare the algorithms.
Each algorithm returns a lists of lists, representing the optimized boards'''

import sys

from tabulation import get_table

# import board_generator
# assortment =[[1,'1L',9,12],[1,'1S',5,4],[2,'2L',9,8],[2,'2S',5,3],[3,'3L',9,5],[3,'3S',5,1]]
# boards = board_generator.get_random_boards(100)
# # boards = [[[3,2],[3,2]], [[3,2],[3,2]]]
# table = get_table(assortment, 60)

# tbl = table[:]




def get_optimized_boards(boards, table, algorithm):
    
    cut_boards = []
    for board in boards:
        if algorithm == 'algo_naive':
            cut_boards.append(algo_naive(board, table))
        if algorithm == 'join_algo':
            cut_boards.append(join_algo(board, table))
        if algorithm == 'where_join_algo':
            cut_boards.append(where_join_algo(board, table))
        if algorithm == 'demote_where_join_algo':           #TODOO
            cut_boards.append(join_algo(board, table))
    return cut_boards



def get_min_index(board, worst_possible_quality):
    min_quality = worst_possible_quality
    min_index = False
    for index, section in enumerate(board):
        if not type(section[0]) == int: 
            continue
        current_quality = section[0]
        if current_quality < min_quality: 
            min_quality = current_quality
            min_index = index

    return min_index








def algo_naive(org_board, table):
    """Naive Algorithm
        while there are possible sections in your board, tabulate them, going from best to worst quality. 
        The returned list that comes from the table is then inserted back into the board. The placement of the offcuts is not considered (always goes to the left)
        No joining is done"""
    worst_possible_quality = len(table)+1
    index = get_min_index(org_board, worst_possible_quality)
    if index is False:
        return org_board

    quality = org_board[index][0]
    length = org_board[index][1]

    try:
        pieces = table[quality-1][length][0].copy()
    except:
        print("Your tabulated table is too short! The given lengths you want to optimize are longer than the table. Increase the table size")
        sys.exit()

    # insert pieces into new board
    new_board = org_board.copy()
    new_board.pop(index)
    for piece in pieces:
        new_board.insert(index, piece)
    new_board = algo_naive(new_board, table)
    return new_board













def join_algo(org_board, table):
    '''Join_algo
    Does the same as the Naive Algorithm, but joins/merges the uncutted remaining piece that could not be classified to it's neigbour IF compatible (i.e. same quality)
    Repeats this process recursively until no further optimization can be done'''

    worst_possible_quality = len(table)+1
    index = get_min_index(org_board, worst_possible_quality)
    if index is False:
        return org_board

    quality = org_board[index][0]
    length = org_board[index][1]

    try:
        pieces = table[quality-1][length][0].copy()
    except:
        print("Your tabulated table is too short! The given lengths you want to optimize are longer than the table. Increase the table size")
        sys.exit()

    # insert pieces into new board
    new_board = org_board.copy()
    new_board.pop(index)
    for piece in pieces:
        new_board.insert(index, piece)
    for i in range(len(new_board)-1):

        current = new_board[i]
        next = new_board[i+1]
        if (isinstance(current[0], int) and isinstance(next[0],int)):
            if current[0] == next[0]:    # if the qualities of current and next are same and if both are not classified (qualities are ints):
                new_section = [current[0], current[1] + next[1]] # then combine those 2 [same quality][sum of lengths]
                new_board.pop(i) 
                new_board.pop(i) # delete current and next
                new_board.insert(i, new_section) # and insert it
                break
    new_board = join_algo(new_board, table)
    return new_board











            
def where_join_algo(org_board, table):
    worst_possible_quality = len(table)+1
    index = get_min_index(org_board, worst_possible_quality)
    if index is False:
        return org_board

    quality = org_board[index][0]
    length = org_board[index][1]

    try:
        pieces = table[quality-1][length][0].copy()
    except:
        print("Your tabulated table is too short! The given lengths you want to optimize are longer than the table. Increase the table size")
        sys.exit()

    # insert pieces into new board       THIS IS THE "WHERE" PART
    new_board = org_board.copy()
    new_board.pop(index) 
    is_not_inserted = True

    if isinstance(pieces[-1][0],int):   # check if offcut
        offcut = pieces[-1]
        cur_qlty = offcut[0]
        cur_len = offcut[1]


        if (index-1 >= 0 and index+1 < len(org_board)): # if there is a previous and next piece
            prev = org_board[index-1]
            prev_qlty = prev[0]
            prev_len = prev[1]
            next = org_board[index+1]
            next_qlty = next[0]
            next_len = next[1]
            
            # if both neigbours have same quality as offcut, see which one makes the biggest difference
            if (prev_qlty== cur_qlty and next_qlty == cur_qlty and prev_qlty-1 <= len(table) and not (prev_qlty > len(table))):   
                prev_val = table[prev_qlty-1][prev_len][1]
                nxt_val = table[next_qlty-1][next_len][1]
                prev_with_offcut_val = table[cur_qlty - 1] [prev_len + cur_len] [1]
                nxt_with_offcut_val = table[cur_qlty - 1] [next_len + cur_len] [1]
                prev_dif = prev_with_offcut_val - prev_val
                nxt_dif = nxt_with_offcut_val - nxt_val
                if prev_dif <= nxt_dif:         # If the impact by adding to next is more or same as by adding to previous
                    is_not_inserted = False
                    offcut = pieces.pop()
                    new_board.pop(index)        # Remove the next element
                    joined_item = [cur_qlty, cur_len + next_len]   # Combine the offcut with that next piece
                    new_board.insert(index, joined_item) # Insert that combo
                    for piece in pieces:
                        new_board.insert(index, piece) # Then insert the pieces from the tabulation table
                
                # No else statement needed, by default gets added to the left. 

                    
        if (index+1 < len(org_board) and is_not_inserted): # if there is a next piece that has the same quality
            next = org_board[index+1]
            if (next[0] == offcut[0]):
                is_not_inserted = False
                offcut = pieces.pop()                              # THIS LINEEEEEEEEEEEEEEEEEE!  I#$#$@#$@##$
                new_board.pop(index)
                joined_item = [offcut[0], offcut[1] + next[1]]
                new_board.insert(index, joined_item)
                for piece in pieces:
                    new_board.insert(index, piece) 
            

    if is_not_inserted:  # By default just insert left.
        for piece in pieces:
            new_board.insert(index, piece) 
        
    # Join any pieces if possible:
    for i in range(len(new_board)-1):
        if (new_board[i][0] == new_board[i+1][0]) and (isinstance(new_board[i][0],int) and isinstance(new_board[i+1][0], int)):
            new_section = [new_board[i][0], new_board[i][1] + new_board[i+1][1]]
            new_board.pop(i)
            new_board.pop(i)
            new_board.insert(i, new_section)
            break
    table_copy = table.copy()
    new_board = where_join_algo(new_board, table_copy)
    return new_board




# for board in boards:
#     print(board)
#     where_join_algo(board, table)


# print('hi')













# --------- FOR TESTING THIS MODULE AS A STAND-ALONE ------------------

# from tabulation import get_table


# assortment =[[1,'1L',9,12],[1,'1S',5,4],[2,'2L',9,8],[2,'2S',5,3],[3,'3L',9,5],[3,'3S',5,1]]

# board = [[2,7],[1,5],[3,2]]  # [quality, length]

# table = get_table(10, assortment)



# new_board = algo_naive(board) 
# print(new_board)
