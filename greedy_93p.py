# 93p 그리디 알고리즘 - 그리디답지 않음

import math

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬
first = data[n-1]
second = data[n-2]
result = 0

while True:
    for i in range(k): #k번 반복
        if m == 0: break
        result += first
        m -= 1
    if m == 0: break
    result += second
    m -= 1

print(result)