# AoC 2017 - Day 4

def get_input():
    return [l.strip() for l in open("day4.in", 'r').readlines()]

def p1():
    counter = 0

    for pwd in get_input():
        words = set()
        for word in pwd.split():
            if word in words:
                break
            else:
                words.add(word)
        else:
            counter += 1
    
    print(counter)

def p2():
    counter = 0

    for pwd in get_input():
        words = []

        for word in pwd.split():
            if word in words:
                break
            else:
                words.append(word)
        else:
            for i, word in enumerate(words):

                for next_words in words[i+1:]:
                    word_list = set([c for c in word])
                    next_word_list = set([c for c in next_words])

                    if (len(word) == len(next_words) 
                            and word_list == next_word_list):
                        break
                else:
                    continue
                break
            else:
                counter += 1

    print(counter)	     

print("-- Part One --")
p1()
print("-- Part Two --")
p2()
