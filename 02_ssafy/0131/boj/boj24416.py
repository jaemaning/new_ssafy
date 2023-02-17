def fibo(number):
    global cnt

    if len(fibo_list) >= number+1:
        return fibo_list[number]

    else:
        for i in range(len(fibo_list), number+1):
            fibo_list.append(0)
            fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
            cnt +=1
        
        return fibo_list[number]


fibo_list = [0, 1, 1]
cnt = 0
n = int(input())

print(fibo(n), cnt)