def solution(board, moves):
    n = len(board)
    L = [[] for _ in range(n)]
    for b in board:
        for idx, bb in enumerate(b):
            if bb != 0:
                L[idx].append(bb)
    for i in range(n):
        L[i] = L[i][::-1]
    answer = 0
    res = []
    for move in moves:
        if L[move-1]:
            now = L[move-1].pop()
            if res and res[-1] == now:
                answer += 2
                res.pop()
            else:
                res.append(now)
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))