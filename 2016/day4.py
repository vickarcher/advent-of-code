# AoC 2016 - Day 4

def get_input():
    return open("day4.in", 'r').read().split('\n')

def p1():
    total = 0

    for line in get_input():
        freq_table = {}
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for c in alpha:
            freq_table[c] = 0

        name = line[:line.rfind('-')]
        sector_id = line[line.rfind('-')+1:line.rfind('[')]
        checksum = line[line.rfind('[')+1:line.rfind(']')]

        for s in name.split('-'):
            for c in s:
                freq_table[c] += 1
        
        sorted_ft = sorted(freq_table, key=freq_table.get, reverse=True)[:5]

        my_checksum = ""
        for c in sorted_ft:
            my_checksum += c
        
        if checksum == my_checksum:
            total += int(sector_id)

    print(total)

def p2():    
    rooms = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    for line in get_input():
        freq_table = {}
        for c in alpha:
            freq_table[c] = 0
        name = line[:line.rfind('-')]
        sector_id = line[line.rfind('-')+1:line.rfind('[')]
        checksum = line[line.rfind('[')+1:line.rfind(']')]
        for s in name.split('-'):
            for c in s:
                freq_table[c] += 1
        
        sorted_ft = sorted(freq_table, key=freq_table.get, reverse=True)[:5]

        my_checksum = ""
        for c in sorted_ft:
            my_checksum += c
        
        if checksum == my_checksum:
            rooms.append((name, int(sector_id)))

    for name, shift in rooms:
        new_name = ""

        for word in name.split('-'):
            for c in word:
                new_name += alpha[(alpha.find(c) + shift % 26) % 26]
            new_name += " "

        if new_name.startswith("northpole"):
            print(shift)


print("-- Part One --")
p1()
print("--Part Two--")
p2()
