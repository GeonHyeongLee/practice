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
    return res

result = 0
num1, num2, oper = 0, 0, ""

num1 = int(input("첫 번째 숫자: "))
oper = input("연산자 입력 : ")
num2 = int(input("두 번째 숫자: "))

result = calc(num1,oper,num2)

print("계산기 :%d %s %d = %d" %(num1,oper,num2,result))
