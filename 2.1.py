import re
lines = open("2.1.input", "r").readlines()
# Game 94: 7 blue, 5 red, 14 green; 8 green, 3 blue, 1 red; 4 blue, 8 red

class Round:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    def __repr__(self):
        return f"Round(red:{self.red}, green:{self.green}, blue:{self.blue})"

class Game:
    def __init__(self, line):
        gameid_rounds = re.split("Game (\d+): ", line)
        self.id = int(gameid_rounds[1])
        self.rounds = []
        for r in re.split(";", gameid_rounds[2]):
            marbles = list(filter(None, re.split("[ ,\n]", r)))
            red=0
            green=0
            blue=0
            for i in range(len(marbles)):
                if i % 2 == 1:
                    num = int(marbles[i-1])
                    if marbles[i] == "red":
                        red = num
                    elif marbles[i] == "green":
                        green = num
                    elif marbles[i] == "blue":
                        blue = num
            self.rounds.append(Round(red, green, blue))
            #print("%s -> red(%d), green(%d), blue(%d)" % (marbles, red, green, blue))

sum_possible_ids = 0
for line in lines:
    game = Game(line)
    print(game.id, game.rounds)
    impossible = False
    for r in game.rounds:
        if r.red > 12 or r.green > 13 or r.blue > 14:
            impossible = True
            break
    if not impossible:
        sum_possible_ids += game.id
print(sum_possible_ids)