from itertools import permutations
def solution(expression):
    max_res = -int(1e10)
    origin = []
    s = ""
    for ex in expression:
        if ex in "+-*":
            origin.append(int(s))
            origin.append(ex)
            s = ""
        else:
            s += ex
    origin.append(int(s))
    for oper_list in permutations("+-*"):
        list = origin[::]
        for op in oper_list:
            list_temp = []
            flag = 0
            for l in list:
                if flag == 1:
                    list_temp[-1] = eval(str(list_temp[-1])+op+str(l))
                    flag = 0
                    continue
                if l == op:
                    flag = 1
                else:
                    list_temp.append(l)
                    flag = 0
            list = list_temp
        max_res = max(max_res, abs(list[0]))
    return max_res


expression = "50*6-3*2"
print(solution(expression))