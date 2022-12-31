# AoC 2017 - Day 1

def get_input():
    return [l.strip() for l in open("day1.in", 'r').readlines()]

def p1():
    for captcha in get_input():
        ans = 0

        for i, c in enumerate(captcha):
            if captcha[i] == captcha[(i+1)%len(captcha)]:
                ans += int(c)

        print(ans)

def p2():
    for captcha in get_input():
        ans = 0

        for i, c in enumerate(captcha):
            if captcha[i] == captcha[int((i+(len(captcha)/2))%len(captcha))]:
                ans += int(c)
        
        print(ans)

print("-- Part One --")
p1()
print("-- Part Two --")
p2()
