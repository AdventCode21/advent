import sys

def parse_input():
    with open(sys.argv[1], 'r') as file:
        inputs = [words.split('|')[0].split() for words in file.readlines()]
    with open(sys.argv[1], 'r') as file:
        outputs_1 = [word for words in file.readlines() for word in words.split('|')[1].split()]
    with open(sys.argv[1], 'r') as file:
        outputs_2 = [words.split('|')[1].split() for words in file.readlines()]
    return inputs, outputs_1, outputs_2

def mapping(words):
    # find 1, 4, 7, 8
    for word in words:
        if len(word) == 2:
            one = word
        elif len(word) == 3:
            seven = word
        elif len(word) == 4:
            four = word
        elif len(word) == 7:
            eight = word
    potential_numbers = [word for word in words if len(word) == 6]
    for word in potential_numbers:
        if (one[0] in word and not one[1] in word) or (one[1] in word and not one[0] in word):
            six = word
            break
    if one[0] in six:
        d = {one[0] : 5, one[1] : 2}
    else:
        d = {one[1] : 5, one[0] : 2}
    
    for digit in seven:
        if digit not in one:
            d[digit] = 0
    tmp = {}
    for digit in four:
        if digit not in one:
            d[digit] = [1, 3]
            tmp[digit] = [1, 3]
    for word in words:
        if len(word) == 5 and one[0] in word and one[1] in word:
            three = word
            break
    for digit in three:
        if digit in seven:
            continue
        elif digit in tmp:
            d[digit] = 3
            del tmp[digit]
            d[list(tmp.keys())[0]] = 1
        else:
            d[digit] = 6
    for digit in eight:
        if digit not in d:
            d[digit] = 4
    return d

def ex1(words):
    return len([word for word in words if len(word) in [2, 3, 4, 7]])

def ex2(inputs, outputs, sum_map={18:0, 15:2, 16:3, 11:4, 19:6, 21:8, 17:9}):
    count = 0
    for words in zip(inputs, outputs):
        m = mapping(words[0])
        num = []
        for word in words[1]:
            mapped_word = [[m[i] for i in word], sum([m[i] for i in word])]
            if len(word) == 2:
                num.append(1)
            elif len(word) == 3:
                num.append(7)
            elif len(word) == 5 and 1 in mapped_word[0]:
                num.append(5)
            else:
                num.append(sum_map[mapped_word[1]])
        for i, digit in enumerate(num):
            count += digit * 10**(len(num)-i-1)
    return count



if __name__ == "__main__":
    inputs, outputs_1, outputs_2 = parse_input()

    print(ex1(outputs_1))
    print(ex2(inputs=inputs, outputs=outputs_2))

