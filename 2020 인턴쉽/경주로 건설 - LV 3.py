from heapq import heappush, heappop


def solution(board):
    answer = 0
    N = len(board)
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 비용 ,x,y,d,visit
    visit = [(0, 0)]
    q = [(0, 0, 0, -1, visit)]
    while q:
        cost, x, y, d, visit = heappop(q)
        if x == N - 1 and y == N - 1:
            return cost
        for nd, (dx, dy) in enumerate(steps):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and (nx, ny) not in visit:
                if d == -1 or nd % 2 == d % 2: # nd == -1로 놓아서 실수함
                    heappush(q, (cost + 100, nx, ny, nd, visit + [(nx, ny)]))
                else:
                    heappush(q, (cost + 600, nx, ny, nd, visit + [(nx, ny)]))
    return -1


board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
print(solution(board))
