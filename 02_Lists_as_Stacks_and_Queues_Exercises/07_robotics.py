from datetime import datetime, timedelta
from collections import deque

robots = deque(input().split(";"))
# create Time object
hours, minutes, seconds = tuple(map(int, input().split(":")))
start_time = datetime(year=1, month=1, day=1, hour=hours, minute=minutes, second=seconds)
format_time = "%H:%M:%S"

names = []
process_time = []
available_at = []
for r in robots:
    robot_name, process = r.split('-')
    names.append(robot_name)
    process_time.append(int(process))

robots_count=len(names)
for sec in range(1, robots_count + 1):
    available_at.append(start_time + timedelta(seconds=sec))
current_time = start_time


items=deque()
item = input()
while item!='End':
    items.append(item)
    item = input()

while items:
    current_item=items.popleft()
    current_time += timedelta(seconds=1)
    is_found_available_robot=False
    for i in range (robots_count):
        if current_time >= available_at[i]:
            available_at[i] += timedelta(seconds=process_time[i])
            print(f"{names[i]} - {current_item} [{current_time.strftime(format_time)}]")
            is_found_available_robot=True
            break
    if not is_found_available_robot:
        items.append(current_item)



