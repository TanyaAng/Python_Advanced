import sys
from io import StringIO
from reading import read_until_command
from fibonacci_sequence import locate, create_sequence

test_input = '''Create Sequence 10
Locate 13
Create Sequence 3
Locate 10
Stop

'''


def parse_command(command):
    parts = command.split()
    if parts[0] == 'Create':
        return ('Create', int(parts[2]))
    else:
        return ('Locate', int(parts[1]))


sys.stdin = StringIO(test_input)
commands = read_until_command('Stop', map_func=parse_command)
print(commands)

for command, value in commands:
    result = None
    if command == 'Create':
        result = create_sequence(value)
    elif command == 'Locate':
        result = locate(value)

    print(result)
