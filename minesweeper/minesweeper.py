def board(layout):
    if any(q not in ' +-*|' for p in layout for q in p):
        raise ValueError
    if len(set(len(n) for n in layout)) > 1:
        raise ValueError
    if any(set(layout[n]) != {'+', '-'} for n in [0, len(layout) - 1]):
        raise ValueError
    if any(p[q] != '|' for p in layout[1:len(layout)-2]
           for q in [0, len(p) - 1]):
        raise ValueError
    coordinates = set((p, q) for p in range(len(layout))
                      for q in range(len(layout[p]))
                      if layout[p][q] in ' *')
    mines = set((x, y) for (x, y) in coordinates
                if layout[x][y] == '*') 
    for (x, y) in coordinates:
        if (x, y) not in mines:
            adjacent = set((i, j) for i in range(x - 1, x + 2)
                           for j in range(y - 1, y + 2)
                           if (i, j) in coordinates)
            number = str(len(adjacent & mines))
            if number != '0':
                layout[x] = layout[x][:y] + number + layout[x][y + 1:]
    return layout
