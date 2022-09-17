from collections import defaultdict, deque


def bfs(visit_key, graph, check, now_key, visit_n):
    q = deque()
    q.append(0)
    visit_key[0] = len(now_key)
    while q:
        x = q.popleft()
        visit_n[x] = 1
        for next in graph[x]:
            if check[next] == 1:
                now_key.add(next)
            elif check[next] > 1:
                if check[next] not in now_key:
                    continue
            if visit_key[next] == len(now_key) and visit_n[next] == 1:
                continue
            visit_key[next] = len(now_key)
            q.append(next)
    return now_key

def solution(n, path, order):
    graph = defaultdict(list)
    visit_n = [0]*n
    visit_key = defaultdict(int) # 각 정점의 최근 방문했을떄 key의 갯수 저장
    check = defaultdict(int) # lock라면 해당 key숫자적어주기 // key라면 1적기.
    now_key = set() # 방문한 key 모음
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in order:
        if a == 0:
            continue
        elif b == 0:
            return False
        check[a] = 1
        check[b] = a

    while 1:
        prev_key = len(now_key)
        bfs(visit_key, graph, check, now_key, visit_n)
        if prev_key == len(now_key):
            break
    if sum(visit_n) == n:
        return True
    else:
        return False

n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
print(solution(n, path, order))
