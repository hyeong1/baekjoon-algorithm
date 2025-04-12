s = input()
no_reverse = False
word = []

for c in s:
    if no_reverse:
        if c == '>':
            no_reverse = False
        print(c, end='')
        continue
    if c == '<':
        if word:
            while word:
                print(word.pop(), end='')
        print(c, end='')
        no_reverse = True
    elif c == ' ':
        while word:
            print(word.pop(), end='')
        print(' ', end='')
    else:
        word.append(c)
if word:
    while word:
        print(word.pop(), end='')