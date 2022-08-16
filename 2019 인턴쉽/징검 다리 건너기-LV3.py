def solution(stones, k):
    answer = 0
    stones = [max(stones) + 1] + stones
    k_list = [1]*(len(stones)+1)
    while 1:
        min_value = min(stones)
        answer += min_value
        new_stone = []
        new_k_list = []
        for i in range(len(stones)):
            if stones[i] <= min_value:
                new_k_list[-1] += k_list[i]
                if new_k_list[-1] > k:
                    return answer
            else:
                new_stone.append(stones[i] - min_value)
                new_k_list.append(k_list[i])
        stones = new_stone
        k_list = new_k_list

stones=[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))