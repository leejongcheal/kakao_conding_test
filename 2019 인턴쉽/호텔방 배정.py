def find(a, parent):
    if parent[a] == a:
        return parent[a]
    parent[a] = find(parent[a], parent)
    return parent[a]


def union(a,b, parent):
    A, B = find(a, parent), find(b, parent)
    if A < B:
        parent[a] = B
    else:
        parent[b] = A


def solution(k, room_number):
    answer = []
    parent = [i for i in range(k+1)]
    check = [0]*(k+1)
    for room in room_number:
        if check[room] == 0:
            check[room] = 1
            answer.append(room)
        else:
            next = room + 1
            next_parent = find(next, parent)
            while check[next_parent]:
                union(room, next_parent, parent)
                next_parent = find(next_parent + 1, parent)
            check[next_parent] = 1
            answer.append(next_parent)
    return answer


k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))