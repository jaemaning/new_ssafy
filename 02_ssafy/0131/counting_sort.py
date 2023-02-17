def counting_sort(a, b, k):
    """

    :param a: 정렬대상
    :param b: 정렬결과
    :param k: 정렬 대상 중 최댓값
    :return: 없음. (기존 리스트를 정렬하여 뱉음)
    """

    c = [0] * (k + 1)

    # 1. 각 원소의 등장 횟수를 세준다.
    for i in range(len(a)):
        c[a[i]] += 1

    # 2. 각 원소의 등장횟수를 계산해서 내가 들어갈 자리의 위치를 구해준다.
    for i in range(1, len(c)):
        # i 번째 원소의 앞에 몇개의 원소가 있는 확인하면
        # i 번째 원소가 최소 몇번째부터 등장하게 되는지 (결과 배열의 자리를) 알 수 있게 된다.
        c[i] += c[i - 1]

    # 3. 뒤에서부터 a를 확인하면서 자리를 확인하고 채워 준다.
    # 자리를 채울때마다 1 감소 시켜야 다음 원소가 들어 올때 자리 중복이 안된다.
    for i in range(len(a) - 1, -1, -1):
        # c[a[i]] => a[i] 원소가 들어갈 자리 (들어가기 전에 1 빼준다)
        c[a[i]] -= 1
        # 정렬 결과 대상의 자리에 a[i] 를 넣어준다.
        b[c[a[i]]] = a[i]


nums = [0, 4, 1, 3, 1, 2, 4, 1]
result_asc = [0] * 8
counting_sort(nums, result_asc, max(nums))
print(result_asc)


def count_sort_dec(a, b, k):
    """

    :param a: 정렬대상
    :param b: 정렬결과
    :param k: 정렬 대상 중 최댓값
    :return: 없음. (기존 리스트를 정렬하여 뱉음)
    """
    c = [0] * (k + 1)

    # 1. 원소의 등장 횟수를 센다.
    for i in range(len(a)):
        c[a[i]] += 1

    # 2. 자리를 계산하는데... 내림차순
    for i in range(len(c) - 1, 0, -1):
        c[i - 1] += c[i]

    # 3. 뒤에서부터 원소의 자리를 찾아주면 된다.
    for i in range(len(b) - 1, -1, -1):
        c[a[i]] -= 1
        b[c[a[i]]] = a[i]


nums = [0, 4, 1, 3, 1, 2, 4, 1]
result_asc = [0] * 8
count_sort_dec(nums, result_asc, max(nums))
print(result_asc)