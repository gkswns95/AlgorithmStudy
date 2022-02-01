import sys

n = int(sys.stdin.readline())

stack_list = []
result_list = []
count = 1
flag = True
for i in range(n):
    num = int(sys.stdin.readline())
   
    for _ in range(num - count + 1):
        stack_list.append(count)
        result_list.append('+')  # push
        count += 1

    if stack_list[-1] == num:
        stack_list.pop()
        result_list.append('-')  # pop
    else:
        flag = False
        break

[print(x) for x in result_list] if flag else print("NO")
