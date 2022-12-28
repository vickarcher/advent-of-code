# AOC 2015 - Day 4

import hashlib

def md5hash(start):
    val = 'iwrupvqb'
    counter = 0

    while True:
        temp = val
        temp += str(counter)
        if (hashlib.md5(temp.encode())).hexdigest().startswith(start):
            print(counter)
            break
        counter += 1

md5hash('00000')
md5hash('000000')
