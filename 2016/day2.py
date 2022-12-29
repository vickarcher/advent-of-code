# AoC 2016 - Day 2

def get_input():
    return open("day2.in", 'r').readlines()

def p1():
    grid = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
    x, y = 1, 1
    code = ""

    for line in get_input():
        line = line.strip()

        for c in line:
            # print(c)
            if c == 'U' and (0 <= x-1 < len(grid)):
                x -= 1
                # print(grid[x][y])
            elif c == 'D' and (0 <= x+1 < len(grid)):
                x += 1
                # print(grid[x][y])
            elif c == 'R' and (0 <= y+1 < len(grid[0])):
                y += 1
                # print(grid[x][y])
            elif c == 'L' and (0 <= y-1 < len(grid[0])):
                y -= 1
                # print(grid[x][y])

        code += grid[x][y]

    print(code)
    
def p2():
    grid = [
            ["", "", "1", "", ""],
            ["", "2", "3", "4", ""],
            ["5", "6", "7", "8", "9"],
            ["", "A", "B", "C", ""],
            ["", "", "D", "", ""]
        ]
    x, y = 2, 0
    code = ""

    for line in get_input():
        line = line.strip()

        for c in line:
            # print(c)
            if c == 'U' and (0 <= x-1 < len(grid)) and (grid[x-1][y] != ""):
                x -= 1
                # print(grid[x][y])
            elif c == 'D' and (0 <= x+1 < len(grid)) and (grid[x+1][y] != ""):
                x += 1
                # print(grid[x][y])
            elif c == 'R' and (0 <= y+1 < len(grid[0])) and (grid[x][y+1] != ""):
                y += 1
                # print(grid[x][y])
            elif c == 'L' and (0 <= y-1 < len(grid[0])) and (grid[x][y-1] != ""):
                y -= 1
                # print(grid[x][y])

        code += grid[x][y]

    print(code)

print('-- Part 1 --')
p1()
print('-- Part 2 --')
p2()

