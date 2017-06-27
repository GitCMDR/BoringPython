"""this module will try to parse input list and rotate using print and a loop"""

def rotate(heart):
    """this will rotate the input grid"""
    for i in range(len(heart[0])):
        for j in range(len(heart)):
            print(grid[j][i], end=' ')
        print('')

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

rotate(grid)
