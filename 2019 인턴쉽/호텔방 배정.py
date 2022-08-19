import sys
sys.setrecursionlimit(10 ** 7)
# input = sys.stdin.readline
# 요거 까지는 굳이 안써도 상관없음
from collections import defaultdict
def find(a, parent):
    if parent[a] == 0 or parent[a] == a:
        parent[a] = a
        return parent[a]
    parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
    A, B = find(a, parent), find(b, parent)
    if A < B:
        parent[A] = B
    else:
        parent[B] = A


def solution(k, room_number):
    answer = []
    parent = defaultdict(int)
    for room in room_number:
        now = find(room, parent)
        answer.append(now)
        union(now, now+1, parent)
    return answer


k = 10
room_number = [1, 3, 4, 1, 3, 1]
print(solution(k, room_number))
