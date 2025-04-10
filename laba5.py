def spiral_order(matrix):
    if not matrix:
        return
    rows, cols = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    center_row, center_col = rows // 2, cols // 2
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    x, y = center_row, center_col
    while top <= bottom and left <= right:
        yield (x, y, matrix[x][y])
        if direction_index == 0 and y == right:
            top += 1
            direction_index = (direction_index + 1) % 4
        elif direction_index == 1 and x == bottom:
            right -= 1
            direction_index = (direction_index + 1) % 4
        elif direction_index == 2 and y == left:
            bottom -= 1
            direction_index = (direction_index + 1) % 4
        elif direction_index == 3 and x == top:
            left += 1
            direction_index = (direction_index + 1) % 4
        x += directions[direction_index][0]
        y += directions[direction_index][1]

def filter_spiral_elements(matrix):
    spiral_gen = spiral_order(matrix)
    
    filtered_elements = filter(
        lambda elem: (elem[2] % 2) == ((elem[0] + elem[1]) % 2),
        spiral_gen
    )
    mapped_elements = map(lambda elem: elem[2], filtered_elements)
    return mapped_elements
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
result = list(filter_spiral_elements(matrix))
print("Ответ:",(result))