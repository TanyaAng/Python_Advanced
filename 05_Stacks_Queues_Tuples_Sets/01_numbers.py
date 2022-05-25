array_1=set(map(int, input().split()))
array_2=set(map(int, input().split()))

n=int(input())

for _ in range (n):
    command_parts=input().split()
    command=command_parts[0]
    target_set=command_parts[1]

    if command.startswith('Add'):
        if target_set=='First':
            array_1=array_1.union(int(x) for x in command_parts[2:])
        elif target_set=='Second':
           array_2=array_2.union(int(x) for x in command_parts[2:])
    elif command.startswith('Remove'):
        if target_set=='First':
            array_1=array_1.difference(int(x) for x in command_parts[2:])
        elif target_set=='Second':
           array_2=array_2.difference(int(x) for x in command_parts[2:])
    elif command.startswith('Check'):
        if array_1.issubset(array_2) or array_2.issubset(array_1):
            print('True')
        else:
            print('False')


print(', '.join([str(x) for x in sorted(array_1)]))
print(', '.join([str(x) for x in sorted(array_2)]))
