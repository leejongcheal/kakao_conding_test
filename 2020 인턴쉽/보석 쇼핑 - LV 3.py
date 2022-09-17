from collections import defaultdict
def solution(gems):
    answer = []
    gem_list = list(set(gems))
    gem_int = defaultdict(int)
    for i, gem in enumerate(gem_list):
        gem_int[gem] = i
    gem_check =[0]*len(gem_list)
    start, end = 0, 0
    now_dist = 1e10
    for end, gem in enumerate(gems):
        gem_i = gem_int[gem]
        gem_check[gem_i] += 1
        while end - start >= now_dist:
            gem_j = gem_int[gems[start]]
            gem_check[gem_j] -= 1
            start += 1
        while 0 not in gem_check:
            if now_dist > end - start:
                now_dist = end - start
                answer = [start + 1, end + 1]
            gem_j = gem_int[gems[start]]
            gem_check[gem_j] -= 1
            start += 1
    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))