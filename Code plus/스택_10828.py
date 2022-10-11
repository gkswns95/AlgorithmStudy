import sys

num_of_commands = int(sys.stdin.readline())

stack_list = []

for i in range(num_of_commands):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack_list.append(command[1])
    
    elif command[0] == 'pop':
        print(stack_list.pop() if stack_list else -1)
    
    elif command[0] == 'size':
        print(len(stack_list))
    
    elif command[0] == 'empty':
        print(0 if stack_list else 1)

    elif command[0] == 'top':
        print(stack_list[-1] if stack_list else -1)
