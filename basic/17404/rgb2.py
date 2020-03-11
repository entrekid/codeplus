import sys
input = sys.stdin.readline
# print = sys.stdout.write
"""
n번은 2번과 n-1과 같지 않다.
1번이 r일때
2번은 gb만 가능
연속은 어차피 안됨

1번 집만 고려하면 됨
N번과 다르다는 어떻게 쓸 수 있나?

1번이 g일 때
1번이 b일 때

1번이 무엇인가를 선택하는 순간 나머지는 그냥 색갈 반복이 됨
즉 rgbgbgbgbgbgbgbgb이런식이 됨

"""
MAX = 3001
num = int(input())
color = [list(map(int, input().rstrip().split())) for _ in range(num)]
dp0 = [[MAX, MAX, MAX] for _ in range(num)]
dp0[0][0] = color[0][0]
dp1 = [[MAX, MAX, MAX] for _ in range(num)]
dp1[0][1] = color[0][1]
dp2 = [[MAX, MAX, MAX] for _ in range(num)]
dp2[0][2] = color[0][2]
dp0[1][1] = dp0[0][0] + color[1][1]
dp0[1][2] = dp0[0][0] + color[1][2]
dp1[1][0] = dp1[0][1] + color[1][0]
dp1[1][2] = dp1[0][1] + color[1][2]
dp2[1][0] = dp2[0][2] + color[1][0]
dp2[1][1] = dp2[0][2] + color[1][1]
# 1번이 color[0][0]
for iter in range(2, num):
    dp0[iter][0] = min(dp0[iter - 1][1], dp0[iter - 1][2]) + color[iter][0] 
    dp0[iter][1] = min(dp0[iter - 1][2], dp0[iter - 1][0]) + color[iter][1] 
    dp0[iter][2] = min(dp0[iter - 1][1], dp0[iter - 1][0]) + color[iter][2]
    dp1[iter][0] = min(dp1[iter - 1][1], dp1[iter - 1][2]) + color[iter][0] 
    dp1[iter][1] = min(dp1[iter - 1][2], dp1[iter - 1][0]) + color[iter][1] 
    dp1[iter][2] = min(dp1[iter - 1][1], dp1[iter - 1][0]) + color[iter][2]
    dp2[iter][0] = min(dp2[iter - 1][1], dp2[iter - 1][2]) + color[iter][0] 
    dp2[iter][1] = min(dp2[iter - 1][2], dp2[iter - 1][0]) + color[iter][1] 
    dp2[iter][2] = min(dp2[iter - 1][1], dp2[iter - 1][0]) + color[iter][2]
no0 = min(dp0[num - 1])
no1 = min(dp1[num - 1])
no2 = min(dp2[num - 1])
print(dp0)
print(dp1)
print(dp2)
# 1번이 color