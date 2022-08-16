from collections import defaultdict
global banid_list, n, answer
def dfs(idx, now):
    global banid_list, n, answer
    if idx == n and set(now) not in answer:
        answer.append(set(now))
        return
    for id in banid_list[idx]:
        if id not in now:
            dfs(idx+1, now+[id])
def solution(user_id, banned_id):
    global banid_list, n, answer
    len_id = defaultdict(list)
    for id in user_id:
        len_id[len(id)].append(id)
    answer = []
    n = len(banned_id)
    banid_list = defaultdict(list)
    for ban_idx, ban in enumerate(banned_id):
        now = 0
        for id in len_id[len(ban)]:
            flag = 1
            for idx in range(len(id)):
                if ban[idx] != "*" and ban[idx] != id[idx]:
                    flag = 0
                    break
            if flag:
                banid_list[ban_idx].append(id)
    dfs(0, [])
    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id =["fr*d*", "*rodo", "******", "******"]
print( solution(user_id, banned_id))