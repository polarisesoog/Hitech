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

#while 반복문 및 pass break 
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


#함수
def add(n):
    sum = 0
    for i in range(1,n):
        sum +=i
        print(sum)
add(4)


#함수 디폴트 값
def writeInfo(name, dept, major2="없음"):
    print("%s 님 환영합니다!" % name)
    print("학과 : %s " % dept)
    print("부전공 : %s" % major2)
    
name = input("이름은? : ")
dept = input("학과는? : ")
answer = input("복수전공 이수 여부(Y/N) :")
if answer == "Y" or answer == "y" :
    major2 = input("복수전공명: ")
if answer == "Y" or answer == "y" :
    print("--------------------------------")
    writeInfo(name, dept, major2)
else:
    print("--------------------------------")
    writeInfo(name, dept)    


# 함수: 언제든지 불러와서 출력; 포켓몬을 꺼내는 프로그램.
color = input("포켓몬 색깔(빨/ 파/ 노):  ")  
size = input("크기(대/ 중/ 소):  ")  
def poketmon(color,size):
    if color == "빨":
        monc = "파이리"
    if color == "파":
        monc = "꼬부기"
    if color == "노":
        monc = "피카츄"
    if size == "대":
        mons = "큰 녀석"
    if size == "중":
        mons = "중간 녀석"
    if size == "소":
        mons = "쪼매난 녀석"   
    print("나와라", monc, mons, "!!!", )
poketmon(color, size)


#함수 설계
def writeFactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("%d! = %d" %(n,fact))
n = int(input("정수: "))
writeFactorial(n)

def computeFactorial(n) :
    fact = 1
    for i in range(1, 1+n):
        fact = fact *i 
    return fact
n = int(input("정수:  "))
print("%d! = %d" %(n, computeFactorial(n)))


#전역변수
def localTrade2():
    price = 1200    #지역변수로서 함수내에 존재시 우선
    salePrice = price * 1.2
    print(price, salePrice)    
price = 1000      #전역변수 - 함수실행 시점 이전에 전역변수로 선언 
localTrade2()     #따라서 지역변수 없어도 실행 가능  
                 #함수 이후 price선언하면 실행 x
print(price)


#실습과제1
name=eng=math=None
def readData():
    global name, eng, math
    name=input("이름: ") ; eng = int(input("영어 성적: ")) ; 
    math = int(input("수학 성적: "))
    
def getAvg(eng, math, n):
    return((eng+math)/ n )

def getGrade(score):
    if score>=90 : return("A")
    elif score>=80 : return("B")
    elif score>=70 : return("C")
    elif score>=60 : return("D")
    else: return("F")
def printTitle():
    print("-"*53)
    print(" 이 름 \t\t영어\t수학    총점    평균    학점")
    print("-"*53)
    
def printRecord(name, subj1, subj2, mean, level) :
    print("%s       %3d     %3d     %3d     %.2f       %2c"  %(name, subj1, subj2, subj1+subj2, mean, level))
    print("-"*53)
    
readData()
avg = getAvg(eng, math, 2)
grade = getGrade(avg)
printTitle()
printRecord(name, eng, math, avg, grade)
    