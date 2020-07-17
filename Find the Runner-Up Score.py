x = int(input())
arr = list(map(int, input().split()))
ma = max(arr)

for i in range (x):
    if ma == max(arr):
        arr.remove(max(arr))
print(max(arr))