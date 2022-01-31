num = int(input())

for _ in range(num):
  seq = input()
  stack_list = []

  for j in seq:
    if j == "(":
      stack_list.append(j)
    elif j == ")":
      if len(stack_list) != 0 and stack_list[-1] == "(":
        stack_list.pop()
      else:
        stack_list.append(")")
        break
  
  print("YES") if len(stack_list) ==0 else print("NO")
