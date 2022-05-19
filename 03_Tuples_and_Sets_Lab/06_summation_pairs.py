numbers=sorted(list(map(int,input().split())))
print(numbers)
target_number=int(input())
unique_pairs=set()
iterations=0

while len(numbers)>1:
    if numbers[0]+numbers[-1]==target_number:
        unique_pairs.add((numbers[0],numbers[-1]))
        print(f"{numbers[0]}+{numbers[-1]}={target_number}")
        numbers.pop(0)
        numbers.pop()
        iterations+=1
    elif numbers[0]+numbers[-1]>target_number:
        numbers.pop()
    elif numbers[0]+numbers[-1]<target_number:
        numbers.pop(0)

print(iterations)
[print(t) for t in unique_pairs]


