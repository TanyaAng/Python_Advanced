n=int(input())
intersections=[]
max_lenght=0
max_intersection=set()
for _ in range (n):
    first_range,second_range=input().split('-')
    f_start,f_end=tuple(map(int,first_range.split(',')))
    s_start,s_end=tuple(map(int,second_range.split(',')))
    f_set=set(range(f_start,f_end+1))
    s_set=set(range(s_start,s_end+1))
    current_intersection=f_set.intersection(s_set)
    if len(current_intersection)>=max_lenght:
        max_lenght=len(current_intersection)
        max_intersection=current_intersection

print(f"Longest intersection is [{', '.join([str(e) for e in max_intersection])}] with length {max_lenght}")


