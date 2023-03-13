# 반복문 

#예제 로또 번호를 랜덤으로 추출 한다면?
import random
index = 0
while index <=5: 
   print("오늘 행운의 숫자 5묶음 드림: ",random.randint(1,45),random.randint(1,45),random.randint(1,45),random.randint(1,45),random.randint(1,45),random.randint(1,45))
   index = index + 1

# 공배수가 아닌 것들만 추출 한다면?
for num in range(1,100):
    if (num%2 and num%5 and num%3) != 0 :
        print(num)
        
#비밀번호 맞추기
you = input("""움직이는 비밀번호 4자리 맞춰봐: """)
password = random.randint(1000,9999)
try:
    while you != password :
        if int(you) > password:  
            you = input("그것보다 작은데 다시 바꿨어(힌트 1111):")
            if you != "런닝맨":
                print("뻥이야")
                continue
            password = random.randint(1000,9999)
        elif int(you) < password:  
            you = input("그것보다 큰데 다시 바꿨어: ")
            if you == "런닝맨":
                print("관리자 권한으로 해제되었습니다.축하합니다")
                break
            password = random.randint(1000,9999)
except: 
    if you == "런닝맨":
        print("관리자 권한으로 해제되었습니다. 축하합니다 ")  
    else:
        print("""부정한 방법 사용이 감지되어,
더이상 비밀번호 기능을 사용할 수 없습니다.바이""")
        
         
#반복문 중첩사용
n = int(input("양의 정수: "))
k=0
for i in range(2, n+1):
    flag = 0
    for j in range(2,i):
        if i%j==0:
            flag = 0
    if flag ==0:
        if k ==5:
            k=0
            print("")
        print("%3d" %(i), end="")
        k+=1
        

#모찌 산책을 누가 시킬까? 랜덤 순번
song = ["산나", "기삐", "혜찌"]
old = random.sample(song,3)
oldp = random.sample(song,2)
c = ["찬기","찬기"]
print("\t\t월|\t화|\t수|\t목|\t금|\t토|\t일|")
print("이번주는?!", old+oldp+c)
        

        



   

    
