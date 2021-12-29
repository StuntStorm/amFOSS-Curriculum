import random
streakcount = 0
for i in range(10000):
    ls = []
    value = 0
    streaks = 0
    for x in range(100):
        ls.append(random.randint(0,1))
    for x in ls:
        if x == value:
            streaks += 1
            if streaks == 6:
                streakcount += 1
                break
        else:
            value != value
            streaks = 0
print("Chance of streak: "+str(streakcount / 100))
