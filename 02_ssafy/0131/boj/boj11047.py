# boj 11047 동전0

n, money = map(int, input().split())
m_list = []
cnt = 0

for _ in range(n):
    m_list.append(int(input()))

m_list = m_list[::-1]

for m in m_list:
    while money // m != 0:
        cnt += 1
        money -= m

print(cnt)