import sys
from collections import deque

input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    queue = deque()
    N, target = map(int, input().split())
    num_list = map(int, input().rstrip().split())
    # queue 완성
    for idx, priority in enumerate(num_list):
        queue.append((priority, idx))

    """

    """
    cnt = 0
    while queue:
        priority_list = [elem[0] for elem in queue]
        num_max = max(priority_list)
        if num_max <= priority_list[0]:
            done = queue.popleft()
            cnt += 1
            if done[1] == target:
                break
        else:
            queue.rotate(-1)
        
    print(cnt)
