n, m = map(int, input().split())
data = [[0,0,0],[0,0,0],[0,0,0]]
max = 0

#입력값 배열에 삽입
for i in range(n):
    data[i] = list(map(int, input().split()))
    if max < data[i][0]:
        max = data[i][0]

print(max)

