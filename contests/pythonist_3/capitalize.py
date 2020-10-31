"""
Capitalize!

:author: Dela Anthonio
:hackerrank: https://hackerrank.com/delaanthonio
:problem: https://www.hackerrank.com/contests/pythonist3/challenges/capitalize
"""

def solve(s: str):
    words = [word.capitalize() for word in s.split(' ')]
    return " ".join(words)

print(solve('hi jake   hj '))