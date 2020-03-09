"""
stack에 숫자를 쌓음
연산자를 만나면 stack에서 2개를 pop하고
나온 결과를 다시 stack에 push
이 결과를 끝까지 진행하고
남은 것을 반환
소숫점 2째 자리까지
"""
import sys
input = sys.stdin.readline

def operation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2

def main():
    operator = "+-*/"
    num = int(input())
    stack = []
    num_dict = {}
    order = input().rstrip()
    for elem in order:
        if elem not in num_dict.keys() and elem not in operator:
            num_dict[elem] = int(input())
        else:
            continue
    for elem in order:
        if elem not in operator:
            stack.append(num_dict[elem])
        else:
            basis2 = stack.pop()
            basis1 = stack.pop()
            stack.append(operation(basis1, basis2, elem))
    print("{:.2f}".format(stack[0]))
    return
        
main()
