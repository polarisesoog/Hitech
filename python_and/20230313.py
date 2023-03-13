# 반복문 


#예제 로또 번호를 랜덤으로 추출 한다면?
import random
index = 0
while index <=5: 
   print("오늘 행운의 숫자6개씩 5묶음 드림: ",
         random.randint(1,45),
         random.randint(1,45),
         random.randint(1,45),
         random.randint(1,45),
         random.randint(1,45),
         random.randint(1,45),
        random.randint(1,45))
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
더이상 비밀번호 기능을 사용할 수 없습니다.byeeeeeeeeeeeeee""")
        
         
#모찌 산책을 누가 시킬까? 랜덤 순번
song = ["산나", "기삐", "혜찌"]
old = random.sample(song,3)
oldp = random.sample(song,2)
c = ["찬기","찬기"]
print("\t\t월|\t화|\t수|\t목|\t금|\t토|\t일|")
print("이번주는?!", old+oldp+c)
        

#continue문
sum = 0
for i in range(1,101):
    if i%3==0: continue
    sum = sum+i 
print("합: %d" %(sum))

sum=0; i=0
while i < 100:     #+1 자가증식 계산식이 있어서 < 100으로 사용        
        i=i+1               
        if i % 3== 0: continue
        sum = sum +i
print("합: %d" %(sum))


while True:
    print("==메뉴 화면===")
    print("   메뉴1 (1)")
    print("   메뉴2 (2)")
    print("   종류 (q)\n")
    print("==============")
    ch = input("메뉴를 선택하세요(1, 2): ")
    if ch =="1":
        input("주문이 끝났으면 엔터를 두 번 치세요") 
    elif ch =="2":
        pass   #의미 없음
        input("주문이 끝났으면 엔터를 두 번 치세요")
    else :
        print("1, 2를 선택해야 합니다!")
        print("메뉴 화면을 종료합니다")
        break


while 0:      #0만 == False값/ 나머지 == True 값
    print("하이")
    
for i in range(0,0):
    print("보이나?")    #0~0미만이니까 없음
         
for i in range(1, 10, 3):
    print("A")         # 1부터 10미만, 3칸씩



#점수 입력시 학점 출력        
my_score = int(input("점수를 입력하세요: "))
if 100>=my_score>=95:
    grade = "A+ 입니다. 참 잘했어요."
if 94>=my_score>=90:
    grade ="A 입니다. 참 잘했어요."
if 89>=my_score>=85:
   grade ="B+ 입니다.  잘했어요."
if 84>=my_score>=80:
    grade ="B 입니다.  잘했어요."
if 79>=my_score>=75:
    grade ="C 입니다.  수고했어요."
if 74>=my_score>=70:
    grade ="C 입니다.  수고했어요."
if 69>=my_score>=65:
    grade ="D+ 입니다. 분발하세요."
if 64>=my_score>=60:
    grade ="D 입니다. 분발하세요."
if 59>=my_score:
    grade ="F 자퇴하세요." 
print("귀하의 점수는: ", my_score, "학점은: ", grade, "" )

   

    
