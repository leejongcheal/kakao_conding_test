from collections import defaultdict
def pos(num):
    if num == 0:
        return 3, 1
    x = (num-1) // 3
    y = (num-1)%3
    return x, y
def solution(numbers, hand):
    answer = []
    left_num = [1,4,7]
    right_num = [3,6,9]
    left = (3,0)
    right = (3,2)
    for num in numbers:
        if num in left_num:
            answer.append('L')
            left = pos(num)
        elif num in right_num:
            answer.append("R")
            right = pos(num)
        else:
            x, y = pos(num)
            lx, ly = left
            l_dis = abs(lx - x) + abs(ly - y)
            rx, ry = right
            r_dis = abs(rx - x) + abs(ry - y)
            if l_dis < r_dis:
                answer.append('L')
                left = pos(num)
            elif l_dis > r_dis:
                answer.append("R")
                right = pos(num)
            else:
                if hand == "right":
                    answer.append("R")
                    right = pos(num)
                else:
                    answer.append('L')
                    left = pos(num)
    return "".join(answer)

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))