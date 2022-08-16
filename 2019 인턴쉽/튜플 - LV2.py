def solution(s):
    ls = sorted([set(ns.split(',')) for ns in s[2:-2].split("},{")], key=len)
    answer = []
    prev = set()
    for l in ls:
        now = l - prev
        prev = l
        answer.append(int(list(now)[0]))
    return answer

# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{123}}"
print(solution(s))