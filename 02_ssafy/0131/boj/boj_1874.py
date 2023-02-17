# boj 1874 스택 수열

n = int(input())
cnt = 0
n_list = list(i for i in range(2, n + 1))
n_list.sort(reverse=True)
result_list = [1]
print_list = ["+"]

for _ in range(n):

    target_num = int(input())

    if result_list:
        while result_list[-1] != target_num:
            if (target_num in n_list) or (target_num in result_list):
                if target_num in n_list:
                    result_list.append(n_list.pop())
                    print_list.append("+")
                else:
                    print("NO")
                    break
            else:
                print("NO")
                break

        if result_list[-1] == target_num:
            result_list.pop()
            print_list.append("-")
            cnt += 1
        else:
            print("NO")
            break
    else:
        print("NO")
        break

for _ in print_list:
    print(_)


