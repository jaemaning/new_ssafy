a = [[False, False, True, True, True],
    [False, False, True, True, True],
    [False, True, True, True, True],
    [False, False, True, True, True],]

b = [z[:] for z in a]

a[0][0] = 1

print(b)
print(a)