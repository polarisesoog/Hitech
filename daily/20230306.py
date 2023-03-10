name = "배철수; \가나가\  가나다라;rrrrrrrrrrrrrrrrrr\
f\=dfdfdf\qwereqwerqwer"; middle = 92
final = 88
total = final+middle
avg = total / 2                     #변수 설정이라는 뜻 =한개
print(name, total, avg)
 
print()
password = "abcd"
if(password  =="abcd"):             #같냐? 할때는 ==두개
    print("잘했어")
else:
    print("틀렸어")
    print("안녕")

print()
ch1="a" ; num1=ord(ch1)         #아스키 코드 a=97/b=98     ord("a")=97
print(ch1, num1)
num2 = num1 +5 ; ch2= chr(num2)
print(num2, ch2)


print()
num1 = 70; num2=20
print(num1==num2)
print(num1 != num2)
print(20 < num2 < 80)
print(num1 < 50  or num2 <50)
print(num1 >=40 and num1 <80)      
print(not num1>num2)              #not으로 부정 불린값 정의 가능

print()
a_list = [1,2,4,5,6]
a_list.insert(3,9) #변수 자체를 기능으로 연결 사용할 때   .점 사용 .insert 리스트 추가
print(a_list)
solar = [ "a", "b", "c", "d"]
del solar[3]                      #앞에 del 변수[]
solar.extend(a_list)              #.extend 리스트 병합
star ="b"
if star in solar :
    print("우리는 태양계")
print("우리사는별:", solar[2])
solar[2] = "푸른 별-지구"        #리스트 값 단순 수정 가능
print(solar[2])
print(solar)

print()
b_dict = {"k":"1", "p":"2"}
a_dict = {"a":"남자", "b":"여자"}
print(a_dict["a"])
a_dict["c"] = "중성"            #딕셔너리 추가는 좀 헷갈린다.
del a_dict["a"]                 #앞에 del 변수[]
a_dict.update(b_dict)           # .update를 써서 병합
print(a_dict)

print(4^5)
print(2^7)                                
print(pow(7,3))                     #7의 3제곱


a=2
b=-1
c=1
d=-5
print(a and b and c)
print(not(5+d))
