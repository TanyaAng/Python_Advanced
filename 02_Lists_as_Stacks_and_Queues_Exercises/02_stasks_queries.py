def push(n, stack):
    stack.append(n)

def delete(stack):
    if stack:
        stack.pop()

def print_max(stack):
    if stack:
        print(max(stack))

def print_min(stack):
    if stack:
        print(min(stack))

number = int(input())
my_stack = []
for _ in range(number):
    command = input()
    if command.startswith('1'):
        action,n=command.split()
        number=int(n)
        push(number, my_stack)
    elif command.startswith('2'):
        delete(my_stack)
    elif command.startswith('3'):
        print_max(my_stack)
    elif command.startswith('4'):
        print_min(my_stack)

print(', '.join([str(my_stack[i]) for i in range (len(my_stack)-1,-1,-1)]))


