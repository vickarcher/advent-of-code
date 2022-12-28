# AOC 2015 - Day 5

def get_input():
    return open("day5.in", 'r').read().split('\n')

def p1():
    ans = 0

    for line in get_input():
        # print(line)
        
        vowel_flag = False
        double_letter = False
        has_substring = False
    
        prev_letter = ""
        vowelcount = 0
        for c in line:
            if not vowel_flag and c in "aeiou":
                # print("found vowel", c)
                vowelcount += 1
                if vowelcount >= 3:
                    vowel_flag = True
                    # print("more than 3 vowels, vowel_flag set")
                    
            if c == prev_letter:
                double_letter = True
                # print("found double letter", c)
    
            substring = prev_letter + c
            if substring in {'ab', 'cd', 'pq', 'xy'}:
                has_substring = True
                # print(f"{line} has substring {substring}")
                break
    
            prev_letter = c
    
        if vowel_flag and double_letter and not has_substring:
            # print("found a match")
            ans += 1
    
    print(ans)

def p2():
    ans = 0

    for line in get_input():
        # print(line)

        has_pair = False
        repeat_letter = False
        for i in range(len(line)-2):
            pair = line[i:i+2]
            if pair in line[i+2:]:
                has_pair = True

            if line[i] == line[i+2]:
                repeat_letter = True

            # print(has_pair)
            # print(repeat_letter)

            if has_pair and repeat_letter:
                ans += 1
                break

    print(ans)

p1()
p2()
