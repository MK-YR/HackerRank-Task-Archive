# A blindfolded marksman finds that on the average he hits the target 4 times out of 5. If he fires 4 shots, what is the probability of
#
# (a) more than 2 hits?
#
# (b) at least 3 misses?
#
# Submission Modes and Output Format
#
# Your output should be two floating point/decimal numbers rounded to a scale of 3 decimal places (i.e., 1.234 format). There are two submission options:
#
# Complete the challenge manually using pen and paper. Select Plain Text from the editor's language drop-down. Put the answer to question (a) on the first line and the answer to question (b) on the second line.
#
# Hard-code the given parameters into a Python or R program that solves the probem, printing the solution to (a) on the first line and (b) on the second line.
#
# Your answer should resemble something like:
#
# 0.123
# 0.456
# (This is NOT the answer, just a demonstration of what the answering format should resemble).

import math

p = 0.8
q = 0.2
n = 4
prob_more_than_2_hits = ( #More than 2 hits - 3 or 4 hits
    math.comb(n, 3) * (p ** 3) * (q ** 1) +
    math.comb(n, 4) * (p ** 4)
)
prob_at_least_3_misses = ( #At least 3 misses - 3 or 4 misses
    math.comb(n, 3) * (q ** 3) * (p ** 1) +
    math.comb(n, 4) * (q ** 4)
)
print(f"{prob_more_than_2_hits:.3f}")
print(f"{prob_at_least_3_misses:.3f}")