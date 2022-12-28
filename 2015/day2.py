# AOC 2015 - Day 2

def get_input():
    return open("day2.in", 'r').readlines()

def p1():
    ans = 0
    
    for line in get_input():
        l, w, h = map(int, line.split('x'))
        x = l*w
        y = w*h
        z = h*l
        e = sorted([x, y, z])
    
        ans += (2*(x + y + z) + e[0])
    
    print(ans)

def p2():
    ans = 0

    for line in get_input():
        l, w, h = map(int, line.split('x'))
        e = sorted([l,w,h])

        ans += 2*(e[0] + e[1]) + (l * w * h)
    
    print(ans)

p1()
p2()
