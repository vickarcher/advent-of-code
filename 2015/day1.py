# AOC 2015 - Day 1

def get_input(): 
    return open("day1.in", 'r').read().split('\n')

def p1():
    counter = 0
    
    for line in get_input():
        for c in line:
            if c == "(":
                counter += 1
            else:
                counter -= 1
    
    print(counter)
    
def p2():
    counter = 0

    for line in get_input():
        for i, c in enumerate(line):
            if counter == -1:
                print(i)
                break

            if c == "(":
                counter += 1
            else:
                counter -= 1
    
p1()
p2()
