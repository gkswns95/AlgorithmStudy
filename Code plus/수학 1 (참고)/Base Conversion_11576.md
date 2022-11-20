[![image](https://user-images.githubusercontent.com/69138191/202888587-aad7bcf1-3cef-439d-98ed-9e967503369a.png)](https://www.acmicpc.net/problem/11576)
### 나의 풀이
1. A진법을 10진법으로 변환
2. 10진법을 B진법으로 변환
3. 출력
```python
# inputs
A, B = map(int, input().split())
N = int(input())
nums = list(map(int, input().split()))

# Convert A to 10
ten = 0
cnt = len(nums) -1
for num in nums:
    ten += num * A ** cnt
    cnt -= 1

# Convert 10 to B
ret = []
while ten !=0:
    ret.append(str(ten % B))
    ten //= B
print(*ret[::-1])
```
