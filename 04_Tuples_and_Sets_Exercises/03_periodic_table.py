n=int(input())
unique_elem=set()
for _ in range(n):
    elements=input().split()
    for e in elements:
        unique_elem.add(e)
if unique_elem:
    [print(el) for el in unique_elem]
