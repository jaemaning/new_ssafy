s = input().strip()
boom = input().strip()
boom_len = len(boom)
boom_stack = list(boom)
last_boom = boom[-1]
stack = []

for character in s:
    stack.append(character)
    if character == last_boom:
        while boom_stack == stack[-boom_len:]:
            del stack[-boom_len:]

print(''.join(stack) if stack else "FRULA")