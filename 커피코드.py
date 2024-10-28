
'''def coffee_machine(x) :
    
    print("#1. 뜨거운 물을 준비한다.\n");
    print("#2. 종이컵을 준비한다.");
    if x == 1:
        print("#3. 보통 커피를 탄다.")
    elif x == 2:
        print("#3. 설탕커피를 탄다.")
    elif x == 3:
        print("#3. 블랙커피를 탄다.")
    else:
        print("#3. 아무거나 탄다.\n")
    print("#4. 스푼으로 젓는다.")

# 메인코드
coffee = int(input("어떤 커피 드릴까요?(1:보통,2:설탕,3:블랙)"))

coffee_machine(coffee)
print("#5. 손님에게 서빙한다.")'''

def calc(v1, op, v2):
    res  =0
    if op == "+":
        res = v1 + v2
    elif op == "-":
        res = v1 - v2
    elif op == "*":
        res = v1 * v2
    elif op == "/":
        res = v1 / v2
    return result

result = 0
num1, num2, oper = 0, 0, ""

num1 = int(input("첫 번째 숫자: "))
oper = input("연산자 입력 : ")
num2 = int(input("두 번째 숫자: "))

result = calc(num1,oper,num2)

print("계산기 :%d %s %d = %d" %(num1,oper,num2,result))
