from collections import deque
def fill_the_box(*args):
    height=args[0]
    length=args[1]
    width=args[2]
    cubes=args[3:]
    volume=height*length*width
    cubes_to_fill=deque([])
    for c in cubes:
        if c=='Finish':
            break
        else:
            cubes_to_fill.append(c)
    while cubes_to_fill:
        c=cubes_to_fill.popleft()
        if volume-c>=0:
            volume-=c
        else:
            c-=volume
            cubes_to_fill.appendleft(c)
            return f"No more free space! You have {sum(cubes_to_fill)} more cubes."
    return f"There is free space in the box. You could put {volume} more cubes."




print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
