ll=list(map(int,input().split()))
target=int(input())
targets=set()

# map={}
# for value in ll:
#     if value in targets:
#         p1=value
#         p2=map[value]
#         print(f"{p1} + {p2} = {target}")
#     else:
#         targets.add(target-value)
#         map[target-value]=value

iteration=0
for i1 in range(len(ll)):
    for i2 in range (i1+1, len(ll)):
        if ll[i1]+ll[i2]==target:
            print(f"{ll[i1]} + {ll[i2]} = {target}")
            targets.add((ll[i1],ll[i2]))
        iteration += 1

print(iteration)
[print(v) for v in targets]



