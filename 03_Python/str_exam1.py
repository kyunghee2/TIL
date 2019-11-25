##문자열 관련 함수들

#문자 개수 세기
a = "hobbby"
print(a.count('b')) #3

#위치값 구하기
a = "Python is best choice"
print(a.find('b')) #10
print(a.find('k')) #-1

#문자열 삽입
a=","
print(a.join('abcd')) # a,b,c,d

#소문자를 대문자로 바꾸기
a="i like you"
print(a.upper()) #I LIKE YOU

#대문자를 소문자로 바꾸기
a="I LIKE YOU"
print(a.lower()) #i like you

#왼쪽 공백 지우기
a = " hi " 
print(a.lstrip())
#오른쪽 공백 지우기
a = " hi "
print(a.rstrip())
#양쪽 공백 지우기
a = " hi "
print(a.strip())

a ="Life is too short"
print(a.replace("Life","Your leg")) #Your leg is too short

a ="Life is too short"
print(a.split()) #['Life', 'is', 'too', 'short']

a = "a:b:c:d"
print(a.split(':')) #['a', 'b', 'c', 'd']














