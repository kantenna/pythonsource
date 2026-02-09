# 모듈
# 함수, 변수, 클래스를 모아놓은 파이썬 파일
# math module 전체 import
# import math
# import sys

# print(math.sqrt(16))
# print(math.sin(2))
# print(sys.builtin_module_names)

# math 모듈에서 사용할 함수만 가져오기
# from math import sin, cos, floor, ceil

# print(sin(1))
# print(cos(1))
# print(floor(1.5))
# print(ceil(1.6))

# from random import random, uniform, randrange, choice, shuffle, sample

# print(random())  # 0 < random() <= 1
# print(uniform(10, 20))  # 10 ~ 20 사이의 float
# print(randrange(10, 20))  # 10 ~ 20 사이의 int
# print(choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 주어진 리스트 안에서 랜덤하게 선택
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# shuffle(list1)  # 섞기
# print(list1)  # 섞은 후 결과 학인
# print(sample(list1, 2))  # 원하는 요소 개수만큼 추출

# 별칭 붙여서 쓰기
# import math as m

# print(m.ceil(3.14))
# print(m.sin(3))

# custom module 호출
# import prt

# prt.prt1()
# prt.prt2()

# from prt import prt1
# prt1()

import sum1

print(sum1.add(6, 7))

number = sum1.number_input()

print(sum1.getcirc(number))
print(sum1.getarea(number))
