def my_reverse(s):
    result = ""
    for c in range(len(s) - 1, -1, -1):
        result += s[c]
    return result


def my_new_reverse(s):
    s2 = list(s)

    for i in range(len(s2)//2):
        s2[i], s2[-i-1] = s[-i-1], s[i]

    return "".join(s2)


s = 'Reverse this strings'
print(my_new_reverse(s))
