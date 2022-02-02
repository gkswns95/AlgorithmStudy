import sys

## stack1 represent cursor's left side, stack2 is cursor's right side
stack_list1 = list(sys.stdin.readline().rstrip())  # remove '\n' token
stack_list2 = []


n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'L': 
        if stack_list1:
            stack_list2.append(stack_list1.pop())
    
    elif command[0] == 'D':
        if stack_list2:
            stack_list1.append(stack_list2.pop())

    elif command[0] == 'B':
        if stack_list1:
            stack_list1.pop()    
    
    elif command[0] == 'P':
        stack_list1.append(command[1])

stack_list1.extend(reversed(stack_list2))

print(''.join(stack_list1))
