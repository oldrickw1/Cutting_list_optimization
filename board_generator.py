import random

def get_random_boards(amount):
    board_list = []
    for n in range(amount):
        board = []
        sections = random.randint(4,8)
        lencount = 0 
        for i in range(sections):
            quality = random.randint(1,4)
            if len(board):
                while (quality == board[-1][0]):
                    quality = random.randint(1,4)
            length = random.randint(1, 20)
            lencount += length
            board.append([quality,length])
        while lencount > 105:
            popped = board.pop()
            lencount -= popped[1]

        board_list.append(board)
    return board_list
