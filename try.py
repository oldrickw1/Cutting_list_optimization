from dataclasses import dataclass


assortment =[[1,'1L',5,6],[1,'1S',2,4],[2,'2L',5,5],[2,'2S',2,3]] # [quality, symbol/name, length, value]


board = [1,1,1,1,1]
len = len(board)

memo = {}
memo[0] = (0, None)

@dataclass
class Planks:
    id: str
    length: int
    quality: int
    value: int


planks = []
for item in assortment:
    quality = item[0]
    id = item[1]
    length = item[2]
    value = item[3]
    planks.append(Planks(id, length, quality, value))


def allowed_plank(board, end, plank):
    if end + 1 + plank.length > len:
        return False
    if end + 1 - plank.length < 0:
        return False
    for i in range(end + 1-plank.length, end + 1):
        if board[i] > plank.quality:
            return False
    return True


def f(i):
    if i in memo: return memo[i]
    if i > len: return float("-inf"), None
    if i == len: return 0, None
    if i <=0 : return 0, None

    best_value = 0
    best_cut = None


    # For each plank, check if it can be cut
    for plank in planks:
        if not allowed_plank(board, i, plank):
            continue
        value, _ = f(i + 1 - plank.length)  # Look for previous cut values if there are any
        value += plank.value # Add current cut value to that
        if value > best_value:
            best_value = value
            best_cut = plank


    memo[i] = (best_value, best_cut)
    return (best_value, best_cut)

def main():
   

    for i in range(len + 1):
        f(i)


main()
print('hi')