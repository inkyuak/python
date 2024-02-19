def binary(n):
    if n == 1:
        return [[0],[1]]
    temp = []
    for i in binary(n-1):
        temp.append([0]+i)
    for i in binary(n-1):
        temp.append([1]+i)
    return temp

num = int(input())
for i in binary(num):
    print(i)