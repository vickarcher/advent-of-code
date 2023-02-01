# AoC 2018 - Day 3

def get_input():
    return [l.strip() for l in open("day3.in", 'r').readlines()]

def p1():
    fabric = {}

    for line in get_input():
        claim_id, _, distance, size = line.split()
        x, y = map(int, distance[:-1].split(','))
        w, l = map(int, size.split('x'))
        
        for row in range(l):
            for col in range(w):
                if (y+row, x+col) not in fabric: 
                    fabric[(y+row, x+col)] = []

                fabric[(y+row, x+col)].append(claim_id)

    # area = 0
    # for key in fabric:
    #     if len(fabric[key]) > 1:
    #         area += 1
    area = sum([1 for key in fabric if len(fabric[key]) > 1])

    print(area)

def p2():
    fabric = {}

    claims = set()
    for line in get_input():
        claim_id, _, distance, size = line.split()
        x, y = map(int, distance[:-1].split(','))
        w, l = map(int, size.split('x'))
        
        claims.add(claim_id)
        for row in range(l):
            for col in range(w):
                key = (y+row, x+col)
                if key in fabric: 
                    fabric[key].append(claim_id)
                    for v in fabric[key]:
                        if v in claims:
                            claims.remove(v)
                else:
                    fabric[key] = [claim_id]

    for i in claims:
        print(i)


print("-- Part One --")
p1()
print("-- Part Two --")
p2()
