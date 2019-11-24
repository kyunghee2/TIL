## 리스트 관련 함수

#append() - 맨 마지막 인덱스에 값을 추가
#extend() - 리스트 확장
my_list = list([1,2,3])
print(my_list)
my_list.append(4)
print(my_list)
my_list.append([5,6,7])
print(my_list)
my_list.extend([5,6,7])
print(my_list)

#sort - 오름차순
#reverse() - 내림차순
my_list = [7,3,1,8,2]
my_list.sort() #리턴값없음, 원본제어
print(my_list)
my_list.reverse()
print(my_list)

#index() - 찾는 값의 위치값 리턴, 위치값 0부터 시작
my_list = [7,3,1,8,2]
print(my_list.index(1))