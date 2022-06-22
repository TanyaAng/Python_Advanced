from pyfiglet import figlet_format
from termcolor import colored

print(figlet_format(input(), font='isometric1'))

print(colored('Python', 'blue', attrs=['underline']))


