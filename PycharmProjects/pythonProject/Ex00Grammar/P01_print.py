print(52)
help(print)
print(52, 273, "Hello Python")

a = 100 #동적할당 : 초기화와 동시에 자동 타입 설정
print(type(a)) #<class 'int'>

a = " Hello world"
print(type(a)) #<class 'str'>

print("===특수문자===")
print("\\") # \
print("a\tb") # a	b : tab
print("'A'") # 'A'
print('"A"') # "A"
print('\'')
print("\'")
print("Hello \n world")
print("""
    내일은 선거일 입니다.
    빠지지 마시고 주권을 
    꼭 행사하기시 바랍니다.
""")

print(1,2,3,4,5, sep="👻")

# file 입출력
# 'w' = write모드
with open("아름다운_나라.txt", 'w') as f:
    print("""
    저 산자락에 긴 노을 지면 
    걸음걸음도 살며시 
    달님이 오시네""", file=f)

# file 열 때 // 'r' = read
f = open("아름다운_나라.txt", 'r')
lines = f.readlines()

for line in lines:
    print(line)

# %d: 정수 / %s: 문자열 / %c: 문자 1개 (character)
print("%d %s %3.2f %c" %(10, "문자열", 1234.4567, 48), end="\n\n")

print("네모난 침대에서 일어나 눈을 떠보면\
    네모난 창문으로 보이는 똑같은 풍경 \
     네모난 문을 열고 네모난 테이블에 앉아")

print("{0:=^20}".format('제목')) # '='룰 20개 하고 format의 문자열 끼워넣어서 총 문자 수 20개

print("{} {} {}".format(10, 20, 30))
print("{} {}".format(10, 20, 30)) # 중괄호의 갯수 <= 숫자의 갯수 이어야 함

print("{0:=^20}".format('양수, 음수 부호를 표시'))
print("{:+d}".format(-52)) # + 는 양의 부호
print("{:-d}".format(52)) # - 는 양의 부호, 음수일 경우
print("{:d}".format(-52)) # - 는 양의 부호, 음수일 경우
print("{:+5d}".format(52)) #총 5자리에서 부호와 숫자 표시
print("{:5d}".format(-52)) #총 5자리에서 부호와 숫자 표시 //   -52
print("{:=5d}".format(-52)) #총 5자리에서 부호와 숫자 표시 // -  52
print("{:=+5d}".format(-52)) #총 5자리에서 부호와 숫자 표시 // -  52
print("{:+05d}".format(52)) #총 5자리에서 부호와 숫자 표시 // (+0052)
print("{:#5d}".format(52)) #총 5자리에서 부호와 숫자 표시 // (   52)
print("{:+15f}".format(1234.5678)) #소수, 부호 포함 15자리
print("{:-015f}".format(1234.5678)) #소수, 부호 포함 15자리

print("({0:<10})".format('Hello')) # 총 10자리, (<,>,^는 방향)
print("({0:>10})".format('Hello')) # 총 10자리, (<,>,^는 방향)
print("({0:^10})".format('Hello')) # 총 10자리, (<,>,^는 방향)
print("({0:0>10})".format('Hello')) # 총 10자리, (<,>,^는 방향), 빈자리는 0으로 채움
print("({0:10.2f})".format(1234.5678)) # 총 10자리, 소수 2째 자리. (   1234.57) 소수자리 반올림
print("{{ }}는 클래스이다.".format())

print("{0:=^20}".format('기타 문자열 함수'))
print("Hello World".count("l"))
print("Hello World".find("l")) # 없으면 -1 반환 //index 위치로 결과값 나옴 => 2
print("Hello World".rfind("l"))
print("Hello World".index("l")) # 없으면 error 반환
print(",".join("12345")) # 문자열에 "," 삽입
print("hello".upper())
print("hello".lower())
print("hello".capitalize())

str = '1,2,3,4,5'.split(',')
for i in str:
    print(i, end=" ") #end는 출력 마지막에 넣을 입력 값

print()
print('  hel lo   '.strip()) #공백 무시
print('  he llo   '.lstrip())
print('  hell o   '.rstrip())
