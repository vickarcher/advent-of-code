# AoC 2018 - Day 1

def get_input():
    return [l.strip() for l in open("day1.in", 'r').readlines()]

def p1():
    freq = 0

    for l in get_input():
        op, val = l[0], int(l[1:])

        if op == '+':
            freq += val
        else:
            freq -= val

    print(freq)

def p2():
    freq = 0
    freq_list = [0]

    while True:
        for l in get_input():
            op, val = l[0], int(l[1:])
    
            if op == '+':
                freq += val
            else:
                freq -= val

            if (freq in freq_list):
                print(freq)
                break

            freq_list.append(freq)

        else:
            continue
        break



print("-- Part One --")
p1()
print("-- Part Two --")
p2()
