n=int(input())
even_set=set()
odd_set=set()

for row in range(1,n+1):
    name=input()
    current_ASCII_sum=0
    for ch in name:
        current_ASCII_sum+=ord(ch)
    current_ASCII_sum//=row
    if current_ASCII_sum%2==0:
        even_set.add(current_ASCII_sum)
    else:
        odd_set.add(current_ASCII_sum)

if sum(even_set)==sum(odd_set):
    print(', '.join([str(e) for e in even_set.union(odd_set)]))
elif sum(even_set)>sum(odd_set):
    print(', '.join([str(e) for e in even_set.symmetric_difference(odd_set)]))
else:
    print(', '.join([str(e) for e in odd_set.difference(even_set)]))


