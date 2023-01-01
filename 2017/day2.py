# AoC 2017 - Day 2

def get_input():
    return [l.strip() for l in open("day2.in", 'r').readlines()]

def p1():
    checksum = 0

    for line in get_input():
        sorted_row = sorted(map(int, line.split()))
        checksum += (int(sorted_row[-1]) - int(sorted_row[0]))

    print(checksum)

def p2():
    checksum = 0

    for line in get_input():
        nums = line.split()
        for i, n in enumerate(nums):
            n = int(n)
            for j in nums[i+1:]:
                j = int(j)
                if (n / j == n // j) or (j / n == j // n):
                    if (n / j == n // j):
                        checksum += n // j
                    else:
                        checksum += j // n
        
    print(checksum)



print("-- Part One --")
p1()
print("-- Part Two --")
p2()
