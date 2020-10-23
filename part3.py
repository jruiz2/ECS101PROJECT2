# project 2 part 3
# Tristan Waddell, Xinyi Wang, Julia Ruiz, Melissa Tang
import random
#Location of A1
LA1 = 4.0

#Location of A2
LA2 = 4.25

#Cost of A3
CA1 = 5

#Cost of A2
CA2 = 5

customerLocation = 0 # customer location
scoreA1 = 0  # score of location A1
scoreA2 = 0  # score of location A2
scoreB1 = 0  # score of location B1
scoreB2 = 0  # score of location B2
LB1 = 4  # location B1
LB2 = 8  # location B2
CB1 = 5  # cost B1
CB2 = 5  # cost B2
expectedProfit = 0 # expected profit overall
averageExpectedProfitA1 = 0 # average for testing
averageExpectedProfitA2 = 0
pickedA1 = 0
pickedA2 = 0
print("Calculating... ")

for x in range(999999): # does 1000000 trials to find the expected profit
    customerLocation = random.uniform(0.0, 10.0)
    scoreA1 = 10 - abs(LA1 - customerLocation) + 3*(6-CA1)
    scoreA2 = 10 - abs(LA2 - customerLocation) + 3*(6-CA2)
    scoreB1 = 10 - abs(LB1 - customerLocation) + 3*(6-CB1)
    scoreB2 = 10 - abs(LB2 - customerLocation) + 3*(6-CB2)
    PA1 = scoreA1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
    PA2 = scoreA2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
    PB1 = scoreB1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
    PB2 = scoreB2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
    coinToss = random.uniform(0.0, 1.0)
    if coinToss <= PA1:
        expectedProfit = CA1 - 2
        averageExpectedProfitA1 = averageExpectedProfitA1 + expectedProfit
        pickedA1 = pickedA1 + 1
    elif coinToss <= PA1 + PA2:
        expectedProfit = CA2 - 2
        averageExpectedProfitA2 = averageExpectedProfitA2 + expectedProfit
        pickedA2 = pickedA2 + 1
    else:
        expectedProfit = 0

averageExpectedProfitA1 = averageExpectedProfitA1 / pickedA1
averageExpectedProfitA2 = averageExpectedProfitA2 / pickedA2
print("Average expected profit A1: " + str(averageExpectedProfitA1))
print("Average expected profit A2: " + str(averageExpectedProfitA2))