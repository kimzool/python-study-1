num=input("숫자를 입력하세요")
num1 = int(input("3의 배수 입력: "))
num2 = int(input("5의 배수 입력: "))

# 파이선에서 match case 문은 다른 c언어나 java 와 달리 break 가 필요 없다
match num1%3, num2%5:
    case 0,0: 
        print("num1은 3의 배수 num2는 5의 배수")
    case 0,_: 
        print("num1은 3의 배수")
    case _,0:
        print("num1은 5의 배수")
    case _:
        print("둘다 아무 숫자")
        

