import sys
input = sys.stdin.readline

def main():
    word = input().rstrip("\n")
    stack = []
    ans = ""
    oper_dict = {"+" : 0, "-" : 0, "*" : 1, "/" : 1}
    operator = oper_dict.keys()
    for elem in word:
        if elem not in operator and elem not in "()": # elem이 문자일 때
            ans += elem
        elif elem in operator:
            if not stack: # 스택이 비어있다면 그냥 더하고
                stack.append(elem)
            else: # 스택이 차 있다면
                if stack[-1] == "(": # 괄호가 있을 경우 처음과 같으므로 더함
                    stack.append(elem)
                else: # 괄호가 아니라면 연산자의 우선순위에 따라 정리
                    while stack and stack[-1] != "(" and oper_dict[stack[-1]] >= oper_dict[elem]:
                        ans += stack.pop()
                    stack.append(elem) # 정리하고 남은 현재 push
        else: # elem이 괄호일 때
            if elem == "(":  # 여는 괄호라면
                stack.append(elem) # stack에 더해줌
            else: # elem == ")" # 닫는 괄호라면 이제 여기서 다 정리
                while stack and stack[-1] != "(":
                    ans += stack.pop()
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
    while stack: # 남은 것 모두 push
        ans += stack.pop()
    print(ans)
main()
