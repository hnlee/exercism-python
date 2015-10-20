def valid_board(white, black):
    x1, y1 = white
    x2, y2 = black
    return all(n < 8 for n in (x1, y1, x2, y2)) and white != black

def board(white, black):
    if not valid_board(white, black):
        raise ValueError
    x1, y1 = white
    x2, y2 = black
    chessboard = ['_' * 8 for n in range(8)]
    chessboard[x1] = chessboard[x1][:y1] + 'W' + chessboard[x1][y1 + 1:]
    chessboard[x2] = chessboard[x2][:y2] + 'B' + chessboard[x2][y2 + 1:]
    return chessboard

def can_attack(white, black):
    if not valid_board(white, black):
        raise ValueError
    x1, y1 = white
    x2, y2 = black
    return any([x1 == x2, y1 == y2, abs(x1 - x2) == abs(y1 - y2)])
