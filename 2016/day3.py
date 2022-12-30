# AoC 2016 - Day 3

def get_input():
    return open("day3.in", 'r').readlines()

def calculate_triangle(_list):
    x,y,z = _list
    return (x+y > z) and (y+z > x) and (z+x > y)

def p1():
    counter = 0

    for line in get_input():
        line = line.strip()
        x,y,z = map(int, line.split())
        print(f"x = {x}, y = {y}, z = {z}")
        if (x+y > z) and (y+z > x) and (z+x > y):
            counter += 1
            print("counter increment by one")


    print(counter)

def p2():
    xlist, ylist, zlist = [], [], []
    counter = 0

    for i, line in enumerate(get_input()):
        line = line.strip()
        x,y,z = map(int, line.split())
        xlist.append(x)
        ylist.append(y)
        zlist.append(z)
        
        if (i+1) % 3 == 0:
            counter += calculate_triangle(xlist)
            counter += calculate_triangle(ylist)
            counter += calculate_triangle(zlist)

            xlist.clear()
            ylist.clear()
            zlist.clear()

    print(counter)

print("-- Part One --")
p1()
print("-- Part Two --")
p2()
