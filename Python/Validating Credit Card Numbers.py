import re

pattern = re.compile(r'^(?:4|5|6)\d{3}(?:-?\d{4}){3}$')
n = int(input())
for _ in range(n):
    card = input().strip()
    if not pattern.match(card):
        print("Invalid")
        continue
    digits_only = card.replace('-', '')
    if re.search(r'(\d)\1{3}', digits_only):
        print("Invalid")
    else:
        print("Valid")
