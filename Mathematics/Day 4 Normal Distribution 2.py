# Objective
# In this challenge, we practice solving problems with normally distributed variables.
#
# Task
# In a certain plant, the time taken to assemble a car is a random variable having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:
#
# Less than 19.5 hours?
# Between 20 and 22 hours?
# Output Format
#
# Your output must be a floating point/decimal number, correct to a scale of 3 decimal places. You can submit solutions in either of the 2 following ways:
#
# Solve the problem manually and submit your result as Plain Text. In the text box below, enter 2 lines of floating point/decimal numbers.
#
# Submit an R or Python program, which uses the above parameters (hard-coded), and computes the answer.
#
# Your answer should resemble something like:
#
# 0.123
# 0.456
# (This is NOT the answer, just a demonstration of the answering format.)

import math

mean = 20
std_dev = 2
def normal_cdf(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))
p1 = normal_cdf(19.5, mean, std_dev)
p2 = normal_cdf(22, mean, std_dev) - normal_cdf(20, mean, std_dev)
print(f"{p1:.3f}")
print(f"{p2:.3f}")