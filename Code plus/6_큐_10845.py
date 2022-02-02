import sys

n = int(sys.stdin.readline())

queue_list = []
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue_list.append(command[1])
    
    elif command[0] == 'pop':
        if queue_list:
            print(queue_list[0])
            del queue_list[0]
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(len(queue_list))

    elif command[0] == 'empty':
        print(0 if queue_list else 1)
    
    elif command[0] == 'front':
        print(queue_list[0] if queue_list else -1)
    
    elif command[0] == 'back':
        print(queue_list[-1] if queue_list else -1) 
