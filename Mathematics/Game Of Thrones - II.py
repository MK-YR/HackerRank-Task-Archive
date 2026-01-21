#This follows from Game of Thrones - I.
#Now that the king knows how to find out whether a given word has an anagram which is a palindrome or not, he encounters another challenge. He realizes that there can be more than one palindrome anagrams for a given word. Can you help him find out how many palindrome anagrams are possible for a given word ?
#The king has many words. For each given word, he needs to find out the number of palindrome anagrams of the string. As the number of anagrams can be large, the king needs the number of anagrams % (109+ 7).
#Input format :
#A single line which contains the input string
#Output format :
#A single line which contains the number of anagram strings which are palindrome % (109 + 7).
#Constraints :
#1<=length of string <= 10^5
#Each character of the string is a lowercase alphabet.
#Each test case has at least 1 anagram which is a palindrome.
#Sample Input 01 :
#aaabbbb
#Sample Output 01 :
#3
#Explanation :
#Three palindrome permutations of the given string are abbabba , bbaaabb and bababab.
#Sample Input 02 :
#cdcdcdcdeeeef
#Sample Output 02 :
#90

import os
import sys
from collections import Counter

MOD = 10**9 + 7
MAXN = 10**5
fact = [1] * (MAXN + 1) #Precompute factorials and inverse factorials
invfact = [1] * (MAXN + 1)
for i in range(1, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
for i in range(MAXN, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD
def solve(s):
    freq = Counter(s)
    half_len = 0
    for c in freq:
        half_len += freq[c] // 2
    result = fact[half_len]
    for c in freq:
        result = result * invfact[freq[c] // 2] % MOD
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    result = solve(s)

    fptr.write(str(result) + '\n')
    fptr.close()