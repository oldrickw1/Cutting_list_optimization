from dataclasses import dataclass
from functools import lru_cache

@dataclass(frozen=True, eq=True)
class PossibleCut:
    id: str
    length: int
    quality: int
    value: int

board = [3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
possible_cuts = [
    PossibleCut(id="L1", length=9, quality=1, value=12),
    PossibleCut(id="S1", length=5, quality=1, value=4),
    PossibleCut(id="L1", length=9, quality=2, value=8),
    PossibleCut(id="S2", length=5, quality=2, value=3),
    PossibleCut(id="L3", length=9, quality=3, value=5),
    PossibleCut(id="S3", length=5, quality=3, value=2),
    PossibleCut(id="L4", length=9, quality=4, value=3),
    PossibleCut(id="S4", length=5, quality=4, value=1),
]

def allowed_cut(board, start, cut):
    if start + cut.length > len(board):
        return False
    for i in range(start, start + cut.length):
        if board[i] > cut.quality:
            return False
    return True

def find_best_cuts(board, possible_cuts):

    @lru_cache(maxsize=None)
    def f(i):
        if i > len(board):
            return float('-inf'), None
        if i == len(board):
            return 0, None

        best_value = 0
        best_cut = None
        for cut in possible_cuts:
            if not allowed_cut(board, i, cut):
                continue
            value, _ = f(i + cut.length)
            value += cut.value
            if value > best_value:
                best_value = value
                best_cut = cut
        
        return (best_value, best_cut)

    _, cut = f(0)
    cuts = []
    while cut != None:
        cuts.append(cut)
        _, cut = f(0 + cut.length)

    return cuts

print(find_best_cuts(board, possible_cuts))