n=int(input())
collection_of_names=set()
for _ in range(n):
    collection_of_names.add(input())

[print(name) for name in collection_of_names]