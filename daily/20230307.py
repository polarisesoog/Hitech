
name = "이강인" ; avg = 88.3
print("이름:", name, "평균:", avg, sep="||", end="\n\n")
# sep 서식, end 서식
print("이름:", format(name, "s"), ", 평균: ", format(avg, "^10"))
#format() 함수에서 출력서식은 한개만
print("이름:", format(name, "s"), ", 평균: ", format(avg, "10.4f"))
#자릿수.반올림자리 f는 실수화


name = "홍길동" ; avg = 88.3
print("이름운 %s이고 평균은 %5.2f점 입니다." %(name,avg))
#출력값은 서식 갯수 동일해야 됨. %순서대로 읽음


num1 = 82 ; num2 = 2021 ; num3 = -64
print("num1=%d, num2=%7d num3=%010d"  %(num1,num2,num3))
# 출력서식 d는 정수, 0은 왼쪽부터 0추가, 숫자는 자릿수, 

n1 = 1234 ; n2=-365
print("%-6d %6d" %(n1,n2))
print("10진수 :%d   8진수:%o" %(n1,n2))
#진법 출력 서식 2,8,16, 10진법

str1 = "Hi!" ; str2 = "Welcome!" ; ch1 =42 ; ch2="G"
print("%c%c" %(ch1, ch2))
# c  유니코드 문자로 변화

num = int(input("정수 입력: "))
prime = (num % 2) ==0
# 변수 ==?  t/f 출
print(num, "은 짝수이다 :", prime)                 

name = input("이름: ")
#input은 모두 문자열로 취급
eng = int(input("영어성적:"))
math = int(input("수학성적:"))
total = eng + math ; avg = total /2
print("-" * 45)
print("이름 \t\t 영어 \t 수학 \t 총점 \t 평균")
print("-"*45)
print("%s \t\t %3d \t %3d \t %3d \t %.2f" %(name, eng, math, total, avg))
print("-"*45)
# 탭서식 활용시 띄어쓰기 시작. 끝점. 구조 동일하게 해야함

str1 = "가나다라"
int1 = 11
float1 = 55.5
print("{:s} {:d} {:7.3f}".format(str1, int1, float1))
print(format(str1,"6s"))
print(str1)
print("%10f" %(1234.56))
print(""""It's leviOsa, not leviosa."
-Hermione Granger""")

krw = 1236.80
usd = 1
x = 1000000
tra = x*usd/krw
print("1,000,000 KRW --------> USD", end=" ")
print(tra, ",")

print(format("*", ">7"))
print(format("*"*2, ">7"))
print(format("*"*3, ">7"))
print(format("*"*4, ">7"))
print(format("*"*5, ">7"))
print(format("*"*6, ">7"))
print(format("*"*7, ">7"))

