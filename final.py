from dataclasses import dataclass

@dataclass
class Planks:
    id: str
    length: int
    quality: int
    value: int


def join(board):
    for i in range (len(board) - 1):
        if isinstance(board[i][0], int) and board[i][0] == board[i+1][0]:
            combo = [board[i][0], board[i][1] + 1]
            board.pop(i)
            board.pop(i)
            board.insert(i, combo)
            board = join(board)
            return board
    return board


def allowed_cut(board, start, plank):
    if start + plank.length > len(board):
        return False
    for i in range(start, start + plank.length):
        if board[i] > plank.quality:
            return False
    return True


def get_optimal(board, assortment):

    planks = []
    for item in assortment:
        quality = item[0]
        id = item[1]
        length = item[2]
        value = item[3]
        planks.append(Planks(id, length, quality, value))

    table = [(0, None)] * (len(board)  + 1) # initialize table of size board length + 1, last index is just after the board

    # Tabulation
    for i in range(len(board) - 1, -1, -1): # from end to start of board
        best_value, _ = table[i + 1] # possibly skip this block of wood
        best_cut = board[i] # and save the skipped over quality, so that it can be visualized
        for plank in planks:
            if not allowed_cut(board, i, plank):
                continue
            value, _ = table[i + plank.length] # check for the previous values if this cut is made
            value += plank.value    # add value of current plank to previous values
            if value > best_value:
                best_value = value
                best_cut = plank 
        table[i] = (best_value, best_cut) # best option is stored, skipping the current block is considered -> stores value of previous step and quality of stepped over block

    # Getting cuts out of the table
    value, cut = table[0]
    cuts = []
    length = 0
    while cut != None:
        cuts.append(cut)
        if isinstance(cut, int):
            length += 1
        else:
            length += cut.length
        _, cut = table[length]

    # formatting
    format_board = []
    for item in cuts:
        if isinstance(item, int):
            format_board.append([item, 1])
        else:
            format_board.append([item.id, item.length])
    return join(format_board)
















# test snippets

# print(format_board)

# print(join(format_board))
# assortment =[[1,'1L',5,6],[1,'1S',2,4],[2,'2L',5,5],[2,'2S',2,3]] # [quality, symbol/name, length, value]
# board = [1,1,1,4,4,1,1]