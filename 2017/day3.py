# AoC 2017 - Day 3

def calc_val(x, y, visited):
    counter = 0
    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    for xi, yi in dirs:
        if (x+xi,y+yi) in visited:
            counter += visited[(x+xi,y+yi)]

    return counter

def p1():
    puzzle_input = 312051 
    visited = {(0, 0)}
    counter = 1
    direction = 'D'
    x, y = 0, 0

    while counter != puzzle_input:
        if direction == 'R':
            if (x+1, y) not in visited:
                x += 1
                direction = 'U'
            else:
                y -= 1

            visited.add((x, y))
        elif direction == 'U':
            if (x, y+1) not in visited:
                y += 1
                direction = 'L'
            else:
                x += 1

            visited.add((x, y))
        elif direction == 'L':
            if (x-1, y) not in visited:
                x -= 1
                direction = 'D'
            else:
                y += 1

            visited.add((x, y))
        elif direction == 'D':
            if (x, y-1) not in visited:
                y -= 1
                direction = 'R'
            else:
                x -= 1

            visited.add((x, y))

        counter += 1

    print(abs(x) + abs(y))

def p2():
    puzzle_input = 312051 
    visited = {(0, 0):1}
    counter = 1
    direction = 'D'
    x, y = 0, 0

    while counter <= puzzle_input:
        if direction == 'R':
            if (x+1, y) not in visited:
                x += 1
                direction = 'U'
            else:
                y -= 1
        elif direction == 'U':
            if (x, y+1) not in visited:
                y += 1
                direction = 'L'
            else:
                x += 1

        elif direction == 'L':
            if (x-1, y) not in visited:
                x -= 1
                direction = 'D'
            else:
                y += 1

        elif direction == 'D':
            if (x, y-1) not in visited:
                y -= 1
                direction = 'R'
            else:
                x -= 1

        counter = calc_val(x,y,visited)
        visited[(x,y)] = counter
    
    print(counter)

print("-- Part One --")
p1()
print("-- Part Two --")
p2()

