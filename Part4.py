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
# initialize the customer location and expected profit
customerLocation = 0
expectedProfit = 0

# random values for location A1 and A2, and cost of coffee for A1 and A2
for j in range(1):
    LA1 = random.randint(0, 10)
    CA1 = random.randint(2, 6)
    LA2 = random.randint(0, 10)
    CA2 = random.randint(2, 6)
    for i in range(1): # Computing the score for each shop and the probability
        customerLocation = random.uniform(0.0, 10.0)
        scoreA1 = 10 - abs(LA1 - customerLocation) + 3 * (6 - CA1)
        scoreA2 = 10 - abs(LA2 - customerLocation) + 3 * (6 - CA2)
        scoreB1 = 10 - abs(LB1 - customerLocation) + 3 * (6 - CB1)
        scoreB2 = 10 - abs(LB2 - customerLocation) + 3 * (6 - CB2)
        PA1 = scoreA1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        PA2 = scoreA2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        PB1 = scoreB1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        PB2 = scoreB2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        # convert code in part 3 as a function
        def part3():
            coinToss = random.uniform(0.0, 1.0)
            if coinToss <= PA1:
                expectedProfit = CA1 - 2
            elif coinToss <= PA1 + PA2:
                expectedProfit = CA2 -2
            else:
                expectedProfit = 0
            return coinToss,expectedProfit
        maxProfit = 0
        if expectedProfit > maxProfit:
            maxProfit = expectedProfit
            bestLA1 = LA1
            bestLA2 = LA2
            bestCA1 = CA1
            bestCA2 = CA2
            print("bestLA1",bestLA1,"\nbestLA2",bestLA2,"\nbestCA1",bestCA1,"\nbestCA2",bestCA2)
