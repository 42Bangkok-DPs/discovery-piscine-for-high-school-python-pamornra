#!/usr/bin/env python3

def checkmate(board):
    # Convert the board string into a 2D list
    board = [list(row) for row in board.splitlines()]
    n = len(board)
    king_pos = None

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break

    if not king_pos:
        print("Fail")
        return

    king_x, king_y = king_pos

    if is_attack(board, king_x, king_y, 'R', rook_moves) or \
       is_attack(board, king_x, king_y, 'B', bishop_moves) or \
       is_attack(board, king_x, king_y, 'Q', queen_moves) or \
       is_attack(board, king_x, king_y, 'P', pawn_moves):
        print("Success")
    else:
        print("Fail")

def is_attack(board, king_x, king_y, piece_type, move_func):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == piece_type:
                if move_func(board, i, j, king_x, king_y):
                    return True
    return False


def rook_moves(board, x, y, king_x, king_y):
    """Check if a rook at (x, y) can attack the King at Position(king_x, king_y)"""
    if x == king_x:
        step = 1 if king_y > y else -1
        for j in range(y + step, king_y, step):
            if board[x][j] != '.':
                return False
        return True
    elif y == king_y:
        step = 1 if king_x > x else -1
        for i in range(x + step, king_x, step):
            if board[i][y] != '.':
                return False
        return True
    return False


def bishop_moves(board, x, y, king_x, king_y):
    """Check if a bishop at (x, y) can attack the king at Position(king_x, king_y)"""
    if abs(king_x - x) == abs(king_y - y):
        step_x = 1 if king_x > x else -1
        step_y = 1 if king_y > y else -1
        i, j = x + step_x, y + step_y
        while i != king_x and j != king_y:  
            if board[i][j] != '.':
                return False
            i += step_x
            j += step_y
        return True
    return False


def queen_moves(board, x, y, king_x, king_y):
    """A queen moves like both a rook and a bishop"""
    return rook_moves(board, x, y, king_x, king_y) or bishop_moves(board, x, y, king_x, king_y)


def pawn_moves(board, x, y, king_x, king_y):
    """Check if a pawn at (x, y) can attack the king at Position(king_x, king_y)"""
    if board[x][y] == 'P':
        return (king_x == x - 1 and abs(king_y - y) == 1)
    elif board[x][y] == 'p':
        return (king_x == x + 1 and abs(king_y - y) == 1)
    return False

def main():
    board = """\
........
........
..R.....
...K....
....P...
........
........
........\
"""
    checkmate(board)

if __name__ == "__main__":
   main()
