# boj 1541 잃어버린 괄호
import sys
from collections import deque
input = sys.stdin.readline

s = input().strip()
q = deque()
switch = 1
result = 0

for c in s:
    if switch:
        if c == "+":
            num = 0
            for i in range(len(q)):
                num = num * 10 + int(q.popleft())
            result += num
        elif c == "-":
            switch = 0
            num = 0
            for i in range(len(q)):
                num = num * 10 + int(q.popleft())
            result += num
        else:
            q.append(c)
    else:
        if c == "+" or c == "-":
            num = 0
            for i in range(len(q)):
                num = num * 10 + int(q.popleft())
            result -= num
        else:
            q.append(c)
else:
    num = 0
    for i in range(len(q)):
        num = num * 10 + int(q.popleft())

    if switch:
        result += num
    else:
        result -= num

print(result)