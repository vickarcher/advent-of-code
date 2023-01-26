# AoC 2018 - Day 2

def get_input():
    return [l.strip() for l in open("day2.in", 'r').readlines()]

def p1():
    twos = 0
    threes = 0

    for l in get_input():
        letter_count = {}

        for c in "abcdefghijklmnopqrstuvwxyz":
            letter_count[c] = 0

        for c in l:
            letter_count[c] += 1

        for c in letter_count:
            if letter_count[c] == 2:
                twos += 1
                break

        for c in letter_count:
            if letter_count[c] == 3:
                threes += 1
                break

    print(twos * threes)

def p2():
    for i, string in enumerate(get_input()):
        for n_str in get_input()[i+1:]:
            t1 = string
            t2 = n_str
            index = 0

            for c in t1:
                if c != t2[index]:
                    t1 = t1[:index] + t1[index+1:]
                    t2 = t2[:index] + t2[index+1:]
                else:
                    index += 1

            if len(t1) == 25:
                print(t1)
                break
        else:
            continue
        break


print("-- Part One --")
p1()
print("-- Part Two --")
p2()
