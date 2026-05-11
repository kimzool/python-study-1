# 함수
def add(a,b): # () 안에는 인수와 개수가 맞게 매개변수가 선언되어져 있어야 함
    res = a+b
    return res

n1 = int(input("숫자 1을 입력하세요:"))
n2 = int(input("숫자 2를 입력하세요:"))

print(add(n1,n2)) # 함수 호출, 리턴값을 받아서 저장혹은 출력
