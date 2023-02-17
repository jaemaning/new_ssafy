# 보이어-무어 알고리즘

def bm_search(txt, pat):
    # txt 인덱스
    ti = 0
    # pattern 인덱스
    pi = 0

    # 텍스트, 패턴의 길이
    n = len(txt)
    m = len(pat)

    # skip table (교재는 list 지만 dictionary로 만들어보자)
    skip = {}

    # 패턴 안에 있는 문자는 몇 칸 건너 뛸지 정해준다. (skip table 만들기)
    for p in pat:
        skip[p] = m - pat.rfind(p) - 1

    # 만약 딕셔너리에 없는 경우는 패턴에 없다는 뜻이니까 그냥 패턴의 길이만큼 건너 뛴다.

    print(skip)

    ti = m - 1
    while ti < n:
        pi = m - 1  # 패턴의 뒤에서부터 비교 시작

        # 같은 문자가 나오면 계속 앞으로 이동
        # 다른 문자가 나오면 건너 뛰기 표를 참고해서 skip

        while txt[ti] == pat[pi]:
            if pi == 0:
                # 패턴의 맨 앞까지 왔으므로, 글자를 찾았다.
                return ti
            ti -= 1
            pi -= 1

        # 건너뛰기 표에 있는 문자가 나오면 표에 적힌대로 skip
        # 건너뛰기 표에 없는 문자가 나오면 패턴의 길이만큼 skip

        offset = skip.get(txt[ti]) if skip.get(txt[ti]) else m

        # 다시 비교를 시작할 위치를 정해준다.
        # 위에서 계산한 건너뛰기 만큼 이동.
        ti += offset if offset > m - pi else m - pi

    # 못찾을 경우
    return -1


t = "zzzabcdabcdabcefabcd"
p = "abcdabcef"
print(f"res :", bm_search(t, p), t.find(p))
