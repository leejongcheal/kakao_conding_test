def solution(stones, k):
    answer = []
    lo, hi = 1, 200000000
    while lo <= hi:
        mid = (lo + hi)//2
        cnt = 0
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            hi = mid - 1
        else:
            lo = mid + 1
            answer.append(mid)
    return max(answer)


stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))