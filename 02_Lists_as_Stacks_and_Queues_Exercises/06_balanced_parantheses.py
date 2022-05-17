valid_starting_symbols = ['(', '{', '[']

openning_parantheses = []

expression = list(input())
is_valid_expression=True
for ch in expression:
   if ch in valid_starting_symbols:
       openning_parantheses.append(ch)
   else:
       if not openning_parantheses:
           is_valid_expression=False
           break
       elif ch==')' and openning_parantheses.pop()!='(':
           is_valid_expression=False
           break
       elif ch=='}' and openning_parantheses.pop()!='{':
           is_valid_expression=False
           break
       elif ch == ']' and openning_parantheses.pop() !='[':
           is_valid_expression = False
           break

if is_valid_expression:
    print('YES')
else:
    print('NO')