# AOC 2015 - Day 3

def get_input():
    return open("day3.in", 'r').read().split('\n')

def p1():
    pos = (0, 0)
    visited = {(0, 0)}
    dirs = {'^':(0,1), 'v':(0,-1), '>':(1,0), '<':(-1,0)}

    for line in get_input():
        for c in line:
            # print(dirs[c])
            x, y = pos
            a, b = dirs[c]
            pos = (x+a, y+b)
            visited.add(pos)

    # print(visited)
    print(len(visited))

def p2():
    s_pos = (0, 0)
    r_pos = (0, 0)
    pos = (0, 0)
    visited = {(0, 0)}
    dirs = {'^':(0,1), 'v':(0,-1), '>':(1,0), '<':(-1,0)}

    for line in get_input():
        for i, c in enumerate(line):
            pos = s_pos if i % 2 == 0 else r_pos
            x,y = pos
            a,b = dirs[c]
            pos = (x+a, y+b)
            visited.add(pos)
            if i % 2 == 0:
                s_pos = pos
            else:
                r_pos = pos

    print(len(visited))

p1()
p2()

