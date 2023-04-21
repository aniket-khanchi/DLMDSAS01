import math
import numpy as np

# define the rate parameter lambda
lamda = 46

# define the value of x for which we want to calculate the probability
x = 23

# calculate the Poisson probability using the formula P(X = x) = (e^(-lamda) * lamda^x) / x!
for i in range(1,63):
    x = i
    prob = math.exp(-lamda) * (lamda ** x) / math.factorial(x)
    probability = round(prob*100,3)
    print("The probability of observing exactly", x, "events in a Poisson process with rate", lamda, "is", probability)

# print the result
# print("The probability of observing exactly", x, "events in a Poisson process with rate", lamda, "is", probability)
