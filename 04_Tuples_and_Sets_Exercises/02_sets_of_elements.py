n,m=tuple(map(int,input().split()))
n_set=set()
m_set=set()

for _ in range(n):
    n_set.add(int(input()))

for _ in range(m):
    m_set.add(int(input()))


result=n_set.intersection(m_set)
if result:
    [print(num) for num in result]