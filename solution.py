# 93p 그리디 알고리즘 - 그리디답지 않음

import math

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬
first = data[n-1]
second = data[n-2]
count_first = 0 #M내에 K가 몇 번 들어가는지
count_second = 0

while m>k:
    m -= k 
    count_first += 1
    if m > 0:
        m -= 1
        count_second += 1

#k가 count번만큼 반복될 수 있음
result = first*k*count_first + second*count_second
print(result)