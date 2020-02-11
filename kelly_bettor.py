# Simple command line program to calculate the optimal percent of your money you should bet.
# by Nicholas Kross

import random

#unlikely_given_odds = 0.2: odds bookmakers were giving to trump, i think, circa the eve of 2016 election
#unlikely_real_odds = 0.286: trump wins, according to 538, circa the eve of 2016 election
#numiters = 52

print("What odds are THEY giving you?")
print("(4 = 4-to-1 odds in THEIR favor, 0.2 = 1-to-4 odds in YOUR favor)")
print("(This is also how much you would multiply your money by, if you won the bet.)")
unlikely_given_odds = 1 /(float(input("Enter: ")) + 1)
print("How likely do YOU think the event is?")
print("(0 to 100%, 50 = 50% chance)")
unlikely_real_odds = float(input("Enter: ")) / 100
print("How many times in a row do you get to bet on this event?")
numiters = int(input("Enter: "))


numtrials = 1000



# kelly criterion
B = (1/unlikely_given_odds) - 1
percent_to_bet_each_time = ((B * unlikely_real_odds) - (1 - unlikely_real_odds)) / B


def flip(p):
    if random.random() < p:
        return True
    else:
        return False


winningsacrosstrials = 0
print("")
print("You should bet about %" + str(round(percent_to_bet_each_time*100)) + " of your total money each time.")
for k in range(numtrials):
    total = 100
    for i in range(numiters):
        amount_to_bet_now = percent_to_bet_each_time * total
        total -= amount_to_bet_now
        if flip(unlikely_real_odds):
            total += (amount_to_bet_now/unlikely_given_odds)
    winningsacrosstrials += total


print("")
print("If you started with $100, you'd expect to end up with $" + str(winningsacrosstrials/numtrials) + ", on average.")
