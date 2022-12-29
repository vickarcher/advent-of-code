# AoC 2016 - Day 1

def get_input():
    return open("day1.in", 'r').read().split('\n')

def p1():
    pos = (0, 0)
    direction = 'N'

    for line in get_input():
        for move in line.split(', '):
            turn = move[0:1]
            distance = move[1:]
            x, y = pos

            if ((direction == 'N' and turn == 'R')
                    or (direction == 'S' and turn == 'L')):
                direction = 'E'
                x += int(distance)
                pos = (x, y)
                # print(pos)
            elif ((direction == 'E' and turn == 'R')
                    or (direction == 'W' and turn == 'L')):
                direction = 'S'
                y -= int(distance)
                pos = (x, y)
                # print(pos)
            elif ((direction == 'S' and turn == 'R')
                    or (direction == 'N' and turn == 'L')):
                direction = 'W'
                x -= int(distance)
                pos = (x, y)
                # print(pos)
            elif ((direction == 'W' and turn == 'R')
                    or (direction == 'E' and turn == 'L')):
                direction = 'N'
                y += int(distance)
                pos = (x, y)
                # print(pos)
    
    x,y = pos
    print(abs(x)+abs(y))

def p2():
    pos = (0, 0)
    direction = 'N'
    visited = [] 

    for line in get_input():
        found = False

        for move in line.split(', '):
            turn = move[0:1]
            distance = move[1:]
            x, y = pos

            if ((direction == 'N' and turn == 'R')
                    or (direction == 'S' and turn == 'L')):
                direction = 'E'
                x += int(distance)
                pos = (x, y)
                # print(pos)
                for i in range(int(distance)):
                    if (x-i, y) in visited:
                        # print(pos)
                        print(abs(x-i)+abs(y))
                        found = True
                        break
                    visited.append((x-i, y))
            elif ((direction == 'E' and turn == 'R')
                    or (direction == 'W' and turn == 'L')):
                direction = 'S'
                y -= int(distance)
                pos = (x, y)
                # print(pos)
                for i in range(int(distance)):
                    if (x, y+i) in visited:
                        # print(pos)
                        print(abs(x)+abs(y+i))
                        found = True
                        break
                    visited.append((x, y+i))
            elif ((direction == 'S' and turn == 'R')
                or (direction == 'N' and turn == 'L')):
                direction = 'W'
                x -= int(distance)
                pos = (x, y)
                # print(pos)
                for i in range(int(distance)):
                    if (x+i, y) in visited:
                        # print(pos)
                        print(abs(x+i)+abs(y))
                        found = True
                        break
                    visited.append((x+i, y))
            elif ((direction == 'W' and turn == 'R')
                or (direction == 'E' and turn == 'L')):
                direction = 'N'
                y += int(distance)
                pos = (x, y)
                # print(pos)
                for i in range(int(distance)):
                    if (x, y-i) in visited:
                        # print(pos)
                        print(abs(x)+abs(y-i))
                        found = True
                        break
                    visited.append((x, y-i))

            if found:
                break

print("-- Part 1 --")
p1()
print("-- Part 2 --")
p2()

