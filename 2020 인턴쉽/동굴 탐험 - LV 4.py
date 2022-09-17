from collections import defaultdict, deque


def bfs(graph, lock, key, visited):
    q = deque()
    q.append(0)
    visited[0] = True
    block_lock = []
    while q:
        x = q.popleft()
        visited[x] = True
        for next in graph[x]:
            if not visited[next]:
                if lock[next]:
                    if not visited[lock[next]]:
                        block_lock.append(next)
                        visited[next] = True
                        continue
                if key[next]:
                    if key[next] in block_lock:
                        q.append(key[next])
                        block_lock.remove(key[next])
                visited[next] = True
                q.append(next)


def solution(n, path, order):
    graph = defaultdict(list)
    visited = [False]*n
    key = [0]*n
    lock = [0]*n
    now_key = set() # 방문한 key 모음
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    for a, b in order:
        if a == 0:
            continue
        elif b == 0:
            return False
        lock[b] = a
        key[a] = b
    bfs(graph, lock, key, visited)
    if sum(visited) == n:
        return True
    else:
        return False

n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]
print(solution(n, path, order))
