# LCS

n = 'heyhibye'
target = 'bye'

i = 0
while i <= len(n) - len(target):
    word_pointer = len(target)-1+i
    target_pointer = len(target)-1
    while target_pointer != -1:
        # print(f"t : {target_pointer}")
        # print(word_pointer)

        if target[target_pointer] == n[word_pointer]:
            word_pointer -= 1
            target_pointer -= 1
            # print(f"t : {target_pointer}")
            # print(word_pointer)
        # 만약 문자가 불일치일 경우
        else:
            # 불일치 일경우 해당 문자가 target 문자중에 들어 있는지 검사
            if n[word_pointer] in target:
                i += len(target) - target.index(n[word_pointer]) - 1
                # print(f"dd {i}")
                break
            # 안들어 있다면?
            else:
                i += len(target)
                break

    if target_pointer == -1:
        print(word_pointer)
        break

