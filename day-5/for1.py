import time

# a="봄"
# b="여름"
# print(a,b,sep="과",end=" 끝 ")
# print(a+b,sep="과",end=" 끝 ") #,가 아닌 +로 출력하면 하나로 합쳐저 sep 이 적용 안 된다 +는 같은 타입끼리 쓰인다
# sep : 변수 사이에 들어가는것을 나타냄
# end : 줄을 바꾸지 않고 옆으로 표시(공백도 가능)

# for i in range(1,100,2) # 1에서 시작 2씩 증가 99까지
# 구구단에서 원하는 단을 입력받아서 출력
dan = int(input("원하는 단은"))
for k in range(1,10):
        print(dan ,"*",k,"=",dan * k , end=" ")


#1~9단 출력
for i in range(1,10):
    print("\n")
    print(i,"단 입니다")
    for j in range(1,10):
        print(i ,"*",j,"=",j * i , end=" ")
        
for l in range(10,0,-1): # range 할때 -1을 하니 10에서 -1까지 range 된다?
    print(l)
    time.sleep(1) 
print("발사!") 