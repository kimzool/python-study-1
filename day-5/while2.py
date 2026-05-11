# 숫자 입력 -> 출력 반복 , 0을 입력하면 종료
on=True
while (on):
    on = int(input("숫자를 입력하세요"))
    print(on)
print("반복문 종료")

print("="*20)
menu = ["쫄면","김밥","냉면","오뎅"]
b= input("메뉴 선택")
while b in menu: # 조건이 참일때 수행 거짓이면 실행하지 않고 탈출 #in은 포함 연산자  
    print(b)
    b= input("메뉴 선택")
    # while 문장안에서 반드시 거짓으로 변경되는 문장이 나와야 종료됨

