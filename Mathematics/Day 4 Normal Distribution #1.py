# Objective
# In this challenge, we practice solving problems with normally distributed variables.
#
# Task
# X is a normally distributed variable with a mean of u=30 and a standard deviation of o=4. Find:
# P(x<40)
# P(x>21)
# P(30<x<35)
#
# Output Format
#
# Your output must be a floating point/decimal number, correct to a scale of 3 decimal places. You can submit solutions in either of the 2 following ways:
#
# Solve the problem manually and submit your result as Plain Text. In the text box below, enter  lines of floating point/decimal numbers.
#
# Submit an R or Python program, which uses the above parameters (hard-coded), and computes the answer.
#
# Your answer should resemble something like:
#
# 0.123
# 0.456
# 0.789
# (This is NOT the answer, just a demonstration of the answering format.)

import math

mu = 30
sigma = 4
def normal_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))
p1 = normal_cdf((40 - mu) / sigma)
p2 = 1 - normal_cdf((21 - mu) / sigma)
p3 = normal_cdf((35 - mu) / sigma) - normal_cdf((30 - mu) / sigma)
print(f"{p1:.3f}")
print(f"{p2:.3f}")
print(f"{p3:.3f}")
