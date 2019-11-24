## 리스트 관련 함수

#append() - 맨 마지막 인덱스에 값을 추가
#extend() - 리스트 확장
my_list = list([1,2,3])
print(my_list) #[1, 2, 3]
my_list.append(4)
print(my_list) #[1, 2, 3, 4]
my_list.append([5,6,7])
print(my_list) #[1, 2, 3, 4, [5, 6, 7]]
my_list.extend([5,6,7])
print(my_list) #[1, 2, 3, 4, [5, 6, 7], 5, 6, 7]

#sort - 오름차순
#reverse() - 내림차순
my_list = [7,3,1,8,2]
my_list.sort() #리턴값없음, 원본제어
print(my_list) #[1, 2, 3, 7, 8]
my_list.reverse()
print(my_list) #[8, 7, 3, 2, 1]

#index() - 찾는 값의 위치값 리턴, 위치값 0부터 시작
my_list = [7,3,1,8,2]
print(my_list.index(1)) #2

#인덱싱
a = [1,2,['a','b',['Life','is']]]
print(a[2][2][0]) #Life

#슬라이싱
a = [1,2,3,['a','b','c'],4,5]
print(a[2:5]) #[3, ['a', 'b', 'c'], 4]
print(a[3][:2]) #['a', 'b']


