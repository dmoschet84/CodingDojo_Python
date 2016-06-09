import random

flips = []
totalHeads = 0
totalTails = 0

def AppendResult(flip):
    if flip == 0:
        global totalHeads
        global totalTails
        totalHeads += 1
        print("Attempt #" + str(totalHeads + totalTails) + ": Throwing a coin... It's a head! ... Got " + str(totalHeads) + " head(s) so far and " + str(totalTails) + " tail(s) so far")
    else:
        global totalHeads
        global totalTails
        totalTails += 1
        print("Attempt #" + str(totalHeads + totalTails) + ": Throwing a coin... It's a tail! ... Got " + str(totalHeads) + " head(s) so far and " + str(totalTails) + " tail(s) so far")

def CoinFlip():
    while (len(flips) < 5000):
        x= random.randint(0,1) #where 0 will be Heads and 1 will be Tails
        flips.append(x)
        AppendResult(x)


CoinFlip()
print("Ending the program, thank you!")
