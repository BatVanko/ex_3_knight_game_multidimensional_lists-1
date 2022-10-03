def moving_knight(row, col, rows, cols):
    possible_moves = [[row + 2, col + 1],
                      [row + 2, col - 1],
                      [row + 1, col + 2],
                      [row + 1, col - 2],
                      [row - 1, col + 2],
                      [row - 1, col - 2],
                      [row - 2, col + 1],
                      [row - 2, col - 1],
                      ]
    result = []
    for r, c in possible_moves:
        if 0 <= col < cols and 0 <= row < rows:
            result.append([r, c])
    return result


size = int(input())

matrix = []
for _ in range(size):
    matrix.append(input())

counter = 0
for i in range(len(matrix) -2):
    for j in range(len(matrix[i])-2):
        current_knight_position = matrix[i][j]
        if current_knight_position == 'K':
            for ro,co in moving_knight(i,j,len(matrix),len(matrix[i])):
                if matrix[ro][co] == 'K':
                    current_knight_position = 'O'
                    counter += 1

print(counter)
print(matrix)
