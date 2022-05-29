from dataclasses import dataclass
from functools import lru_cache


mem = {}
 
@dataclass(frozen=True, eq=True)
class Planks:
  id: str
  length: int
  quality: int
  value: int

 




def allowed_plank(board, start, cut):
  if start + cut.length > len(board):
    return False
  for i in range(start, start + cut.length):
    if board[i] > cut.quality:
      return False
  return True


def find_best_cuts(board, planks):

 
  def f(i):
    if i in mem: return mem[i]
    if i > len(board):
      return float("-inf"), None
    if i == len(board):
      return 0, None

 
    # Possibly skip this block of wood.
    # best_value, best_cut = f(i + 1)
    best_value = 0
    best_cut = None
 
    for cut in planks:
      if not allowed_plank(board, i, cut):
        continue
      value, _ = f(i + cut.length)
      value += cut.value
      if value > best_value:
        best_value = value
        best_cut = cut

    mem[i] = (best_value, best_cut)
    return (best_value, best_cut)
 

  # DP from bottom up to avoid recursion exceeded error. @lru_cache stores the answers for each f()
  for i in range(len(board) + 1, -1, -1):
    f(i)

 
  value, cut = f(0)
  cuts = []
  length = 0
  while cut != None:
    cuts.append(cut)
    length += cut.length
    value, cut = f(length)


  return cuts

def get_optimal_cuts(board, assortment):
  planks = []
  for item in assortment:
    quality = item[0]
    id = item[1]
    length = item[2]
    value = item[3]
    planks.append(Planks(id, length, quality, value))
  # planks.append(Planks('garbage', 1,4,0))
  find_best_cuts(board, planks)

  cut_board = []
  i = 0 
  while (i < len(board)):
    value, cut = mem[i]
    if cut is None:
      cut_board.append(board[i])
      i += 1
    else:
      cut_board.append([cut.id, cut.length])
      i += cut.length

  # Format cut_board:
  formatted_board = []
  print(cut_board)
  i = 0
  while i < len(cut_board):
    if isinstance(cut_board[i], int):
      for j in range(i + 1, len(cut_board)):
        if (j == len(cut_board)-1):
          formatted_board.append([int(cut_board[i]), j - i + 1])
          i += j
          break
        elif cut_board[j] != cut_board[i]:
          formatted_board.append([int(cut_board[i]), j - i])
          i += j-i
          break
    else:
       formatted_board.append(cut_board[i])
       i += 1

  
  mem.clear
  return formatted_board

assortment =[[1,'1L',9,12],[1,'1S',5,4],[2,'2L',9,8],[2,'2S',5,3],[3,'3L',9,5],[3,'3S',5,1]]
board = [1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,4,4,3,2,2,2,2,2,2,3,3,3,3,3]
print(get_optimal_cuts(board, assortment))