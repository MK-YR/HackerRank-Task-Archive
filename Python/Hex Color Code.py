import re
import sys

pattern = re.compile(r'(#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}))(?![0-9A-Fa-f])')
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    inside_block = False
    for _ in range(n):
        line = sys.stdin.readline()
        if '{' in line:
            inside_block = True
            continue
        if inside_block:
            for match in pattern.findall(line):
                print(match)
        if '}' in line:
            inside_block = False