# AoC 2017 - Day 5

def p1():
    f = open("day5.in", 'r')
    instructions = [int(l.strip()) for l in f.readlines()]

    i = 0
    t1 = 0
    t2 = 0
    s = 0

    while -1 <= i < len(instructions): 
        t1 = instructions[i]
        t2 = i
        i += t1
        instructions[t2] += 1
        s += 1

    print(s)

def p2():
    f = open("day5.in", 'r')
    instructions = [int(l.strip()) for l in f.readlines()]

    i = 0
    t1 = 0
    t2 = 0
    s = 0

    while -1 <= i < len(instructions):
        t1 = instructions[i]
        t2 = i
        if t1 < 3:
            instructions[t2] += 1
        else:
            instructions[t2] -= 1
        i += t1
        s += 1
    print(s)

print("-- Part One --")
p1()
print("-- Part Two --")
p2()
