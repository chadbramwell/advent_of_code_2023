# trick - "sevenine" is 79. I originally assumed it'd be 7 and then ignore "ine"
lines = open("1.1.input", "r").readlines()
# lines = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".split()

# returns (value, skip) - value and how far to advance to skip past it.
# "98" would return (9,1) for first digit and 1 rune to skip
# "onetwo" would return (1, 3) for value of "one" and 3 to skip past it
def magic(x):
    # brute = {"1":(1,1), "2":(2,1), "3":(3,1), "4":(4,1), "5":(5,1), "6":(6,1), "7":(7,1), "8":(8,1), "9":(9,1),
    #          "one":(1,3), "two":(2,3), "three":(3,5), "four":(4,4), "five":(5,4), "six":(6,3), "seven":(7,5), "eight":(8,5), "nine":(9,4)}
    # for k,v in brute:
    #     if x.startswith(k): return v
    if x[0].isdigit(): return (int(x[0]),1)
    named_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    named_len = len(named_digits)
    for i in range(named_len):
        if x.startswith(named_digits[i]): 
            # return (i+1, len(named_digits[i]))
            return (i+1, 1)
    return (-1,-1)

# test = "1onetwothree5"
# while test:
#     (val, skip) = magic(test)
#     if skip == -1 and len(test) != 0: 
#         print("not sure how to parse what's left: ", test)
#         break
#     print(test, val, skip)
#     test = test[skip:]

sum = 0
for line in lines:
    copy = line
    value = -1
    last = -1
    # parse first and last digits
    while line:
        (digit, skip) = magic(line)

        if digit == -1:
            line = line[1:]
            continue

        if value == -1:
            value = digit
        else:
            last = digit

        line = line[skip:]

    # combine digits (if single digit like 7, value is 77)
    if last == -1:
        value = value * 10 + value
    else:
        value = value * 10 + last

    # 
    print(copy, value)
    sum += value

# final result
print(sum)