lines = open("1.1.input", "r").readlines()

sum = 0
for line in lines:
    value = -1
    last = -1
    for rune in line:
        if rune.isdigit():
            if value == -1:
                value = int(rune)
            else:
                last = int(rune)
    #print(first, last)
    if last == -1:
        value = value * 10 + value
    else:
        value = value * 10 + last
    print(value)
    sum += value
print(sum)