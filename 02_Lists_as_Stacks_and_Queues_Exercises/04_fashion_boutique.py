clothes=list(map(int, input().split()))
rack_capacity=int(input())

if clothes:
    number_of_racks=1
    current_sum = 0
    while clothes:
        take_clothe = clothes.pop()
        current_sum += take_clothe
        if current_sum == rack_capacity:
            current_sum = 0
            if clothes:
                number_of_racks += 1
        elif current_sum > rack_capacity:
            clothes.append(take_clothe)
            current_sum = 0
            number_of_racks += 1
else:
    number_of_racks=0

print(number_of_racks)


