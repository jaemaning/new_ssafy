# boj 1918  - 후위 표기식

s = input()
isp = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}
icp = {"(": 3, "+": 1, "-": 1, "*": 2, "/": 2}
stk = []
rlt = ""

for c in s:
    if str.isalpha(c):
        rlt += c
    else:
        if c == ")":
            while stk:
                n = stk.pop()
                if n == "(":
                    break
                rlt += n
        else:
            while stk and isp[stk[-1]] >= icp[c]:
                rlt += stk.pop()
            stk.append(c)

while stk:
    rlt += stk.pop()

print(rlt)