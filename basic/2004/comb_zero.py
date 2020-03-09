"""
n!
m! (n-m)!
"""
def make_2(num):
    no_2 = 0
    while num:
        no_2 += num // 2
        num = num // 2
    return no_2

def make_5(num):
    no_5 = 0
    while num:
        no_5 += num // 5
        num = num // 5
    return no_5

def main():
    a, b = map(int, input().split())
    two = make_2(a) - (make_2(b) + make_2(a - b))
    five = make_5(a) - (make_5(b) + make_5(a - b))
    print(min(two, five))
    return

main()