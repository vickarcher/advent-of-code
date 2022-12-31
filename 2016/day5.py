# AoC 2016 - Day 5

import hashlib

def p1():
    door_id = "wtnhxymk"
    password = ""
    counter = 0

    for i in range(8):
        while True:
            temp = door_id + str(counter)
            counter += 1
            encoded_str = (hashlib.md5(temp.encode())).hexdigest()
            if encoded_str.startswith("00000"):
                password += encoded_str[5]
                break
    print(password)

def p2():
    door_id = "wtnhxymk"
    ps_list = ['-']*8
    counter = 0
    available_letters = []

    for i in range(8):
        while True:
            temp = door_id + str(counter)
            counter += 1
            encoded_str = (hashlib.md5(temp.encode())).hexdigest()
            if ((encoded_str.startswith("00000")) 
                    and (encoded_str[5] not in available_letters) 
                    and (encoded_str[5].isdigit()) 
                    and (int(encoded_str[5]) in range(8))):
                ps_list[int(encoded_str[5])] = encoded_str[6]
                available_letters.append(encoded_str[5])
                # print(encoded_str[5], encoded_str[6])
                break
        
        print("".join(ps_list))

print("-- Part One --")
p1()
print("-- Part Two --")
p2()
