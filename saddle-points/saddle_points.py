def saddle_points(matrix):
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError('Please input a regular matrix.')
    transpose = zip(*matrix)
    return set((i, j) for i in range(len(matrix))
               for j in range(len(transpose))
               if matrix[i][j] == max(matrix[i])
               and matrix[i][j] == min(transpose[j]))
                         
