import sys
input = sys.stdin.readline
from collections import Counter
"""
일단 1번씩은 다 스택에 다녀감
지금 숫자가
1) stack의 최신 수보다 빈도수가 작다
    그냥 append
2) stack의 최신 수보다 빈도수가 크다
    stack의 최신 수의 ngf = 지금 숫자
    그리고 지금 수를 append 해줌
3) stack의 최신 수와 빈도수가 같다
    stack에 append(idx)
"""
def main():
    num = int(input())
    num_list = list(map(int, input().rstrip().split()))
    ngf_list = [-1] * (num)
    stack = []
    freq_dict = Counter(num_list)
    for iter in range(len(num_list)):
        if not stack:
            stack.append(iter) # stack에 idx를 담을 것
        else:
            basis = stack[-1]
            if freq_dict[num_list[basis]] >= freq_dict[num_list[iter]]:
                stack.append(iter)
            else: # 우측이 더 클 때
                while stack:
                    basis = stack[-1]
                    if freq_dict[num_list[basis]] >= freq_dict[num_list[iter]]:
                        break
                    ngf_list[basis] = num_list[iter]
                    stack.pop()
                stack.append(iter)
    print(*ngf_list)
    return
main()

