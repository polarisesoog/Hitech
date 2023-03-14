#전역변수 패스워드 3회 오류 방지
def checkPassword(pw):
    global count
    count = count+1
    if pw == "python":
        return(1)
    return(0)

count = 0
pw = input("패스워드 입력: ")
state = checkPassword(pw) #0,1 값을 가짐
while count < 3 :
    if state == 1 :
        print("로그인 성공")
        break
    pw = input("패스워드 재입력")
    state = checkPassword(pw)

if count > 3:
    print("부정 사용자임(3회 패스워드 오류)")
    
    
#전역변수 검색 개수 파악
def visitSeoul():
    global total, countSeoul
    countSeoul += 1
    total += 1
def visitJeju() :
    global total, countJeju
    countJeju += 1
    total += 1

total = 0 #전역변수
countSeoul = countJeju = 0 
while True :
    choice = input("선택['s','j' or 'any Key']: ")
    #("텍스트")괄호 안에 ['텍스트']괄호가 들어가면 
    # 안에 텍스트는 작은따옴표로 표시해야함('') 
    if choice == "s" :
        visitSeoul()
    elif choice == "j" :
        visitJeju()
    else :
        break
print(countSeoul, countJeju, total  )


#
# def g1():
#     price = 2000
#     value = value + price  
#     #지역,전역 모두 있어서 지역변수가 우선하나 value값 없음
#     print("a")
# value = 1000
# g1()
# print(value)



# def localTrade3():
#     salePrice = price * 1.2
#     print(price, salePrice)
#     price = 2000
#       # 지역, 전역 충돌로 지역변수 우선, 
#       # 함수 내 윗부분 price값 미정.
#     salePrice = price *1.2
#     print(price, salePrice)
# price = 1000
# localTrade3()
# print(price)


#파이썬 타입 None(ex/ price = None) : 아무값 없음


#로그인 정당성 확인 프로그램
id = input("관리자 계정의 아이디를 입력하세요")
pw = input("관리자 계정의 비밀번호4자리를 입력하세요")
check_number = 0

def id_check(id):
    while id != "admin":
        print("""관리자 계정이 아닙니다. 
다시 입력해주세요.""")
        id = input("아이디: ")


def pw_check(pw):
    while pw != "1234":
        print("""비밀번호가 틀렸습니다.
다시 입력해 주세요""")
        pw = input("관리자 계정의 비밀번호4자리를 입력하세요")
        global check_number
        check_number = check_number+1
        if check_number >3:
            print("비밀번호 3회이상 틀렸습니다. 바이")
            break              
    print("로그인에 성공하셨습니다.")

a = id_check(id)
b = pw_check(pw)
# 함수는 변수 값으로 반환해서 출려해야 제대로 나온다.
print(id_check(id), pw_check(pw))
# 함수를 직접 출력하면 none값이 출력된다. 그냥 그렇게 알자


#리스트
score = [1,2,3,4,5,6,7,8]
print(score[2:6]) #2번째부터 6번째 전까지 (1칸씩)
#실제 디폴드 값으로 [2:6:1]
print(score[-6:-2]) #-2번째부터 -6번째 전까지(-1칸씩)
score[2] = [11,12,13] #리스트 [안에 [또다른 리스트]]추가 가능
#범위값에 넣으면 리스트값이 아니라 바로 삽입값


class1 = [70, 80, 60, 80, 90]
class2 = [85, 95, 80, 65, 70]
print("class1 = ", class1)

class1.extend(class2)
print("'class1.extend(class2)' 실행 직후 class1 = ",class1)
n = class1.count(80)
print("class1에서 80의 개수  :", n)
class1.remove(80)
print("'class1.remove(80)' 실행 직후 class1 = ",class1)
high = max(class1)
low = min(class1)
print("max = ", high, "min =", low)
class3 = sorted(class1)
print("'class3.sorted(class1)' 실행 직후 class1 = ",class1)
print("'class3.sorted(class1)' 실행 직후 class3 = ",class3)


