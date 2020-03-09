import sys
input = sys.stdin.readline
"""
stack에 넣고
다음 숫자가 들어왔을 때
1) 다음 숫자가 stack[-1]보다 크다.
    stack[-1]의 nge값 = 다음 숫자
    (1) 하고 pop 계속 : s
        stack[-1]의 값이 다음 숫자보다 커지거나
        stack이 빌 때까지
    그리고 나서 다음 숫자 stack에 append
2) 다음 숫자가 stack[-1]보다 작다.
    stack에 append
한 바퀴 돌았는데도 정해지지 않은 애들
모두 -1 : 초기화 -1로 할 것이라서 사실 상관 없음
"""
def main():
    num = int(input())
    num_list = list(map(int, input().rstrip().split()))
    nge_list = [-1] * (num)
    stack = []
    for iter in range(len(num_list)):
        if not stack:
            stack.append(iter)
        else:
            basis = stack[-1]
            if num_list[basis] < num_list[iter]: # stack = [2, 3] num_list[iter] = 5
                """
                num_list[basis] >= num_list[iter] 일 때까지 계속 nge_list[basis] = num_list[iter]
                """
                while stack:
                    basis = stack[-1]
                    if num_list[basis] < num_list[iter]:
                       nge_list[basis] = num_list[iter]
                       stack.pop()
                    else:
                        break
                stack.append(iter) 
            else: # basis >= num_list[iter]:
                stack.append(iter)
    print(*nge_list)
    return

main()