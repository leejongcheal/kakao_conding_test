def solution(stones, k):
    answer = []
    stones = [max(stones) + 1] + stones
    lo, hi = 1, 200000000
    while lo <= hi:
        k_list = [1]
        mid = (lo + hi)//2
        flag = 0
        for s in stones:
            if s < mid:
                k_list[-1] += 1
                if k_list[-1] > k:
                    flag = 1
                    break
            else:
                k_list.append(1)
        if flag:
            hi = mid - 1
        else:
            answer.append(mid)
            lo = mid + 1
    return max(answer)


stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))