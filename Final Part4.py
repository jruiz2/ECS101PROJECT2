# Xinyi Wang
import random
# Location B1
LB1 = 4
# Location B2
LB2 = 8
# cost of the coffee for B1
CB1 = 5
# cost of the coffee for B2
CB2 = 5
# initialize the variables
customerLocation = 0
expectedProfit = 0
expectedProfit1 = 0
expectedProfit2 = 0
bestProfit = 0
bestCA1 = 0
bestCA2 = 0
bestLA1 = 0
bestLA2 = 0


# loop 6 times one for each possible value
for CA1 in (2, 5):
    for LA1 in (0, 10):
        for CA2 in (2, 5):
            for LA2 in (0, 10):
                for x in range(49999):  # does 50000 trials to find the expected profit
                    customerLocation = random.uniform(0.0, 10.0) # Computing the scores for each shop and the probability
                    scoreA1 = 10 - abs(LA1 - customerLocation) + 3 * (6 - CA1)
                    scoreA2 = 10 - abs(LA2 - customerLocation) + 3 * (6 - CA2)
                    scoreB1 = 10 - abs(LB1 - customerLocation) + 3 * (6 - CB1)
                    scoreB2 = 10 - abs(LB2 - customerLocation) + 3 * (6 - CB2)
                    PA1 = scoreA1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
                    PA2 = scoreA2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
                    PB1 = scoreB1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
                    PB2 = scoreB2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
                    coinToss = random.uniform(0.0, 1.0) # code from part 3
                    # computing expected profit
                    if coinToss <= PA1:
                        expectedProfit = CA1 - 2
                        expectedProfit1 = expectedProfit + expectedProfit1
                    elif coinToss <= PA1 + PA2:
                        expectedProfit2 = CA2 - 2
                        expectedProfit2 = expectedProfit + expectedProfit2
                    else:
                        expectedProfit = 0
                # Find the best profit
                if expectedProfit1 > bestProfit or expectedProfit2 > bestProfit:
                    bestProfit1 = bestProfit + expectedProfit1
                    bestProfit2 = bestProfit + expectedProfit2
                    bestCA1 = CA1
                    bestCA2 = CA2
                    bestLA1 = LA1
                    bestLA2 = LA2


print("Best CA1: " + str(bestCA1),"\nBest CA2: " + str(bestCA2),"\nBest LA1: " + str(bestLA1),"\nBest LA2: " + str(bestLA2),"\nBest Profit A1: " + str(bestProfit1),"\nBest Profit A2: " + str(bestProfit2))
