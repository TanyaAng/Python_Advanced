from collections import deque
green_light_sec = int(input())
free_window_sec = int(input())

cars_on_crossroad = deque()

command = input()
is_crash_happened = False
total_cars_passed=0
while command != 'END':
    if command!='green':
        cars_on_crossroad.append(command)
    elif command=='green' and cars_on_crossroad:
        green_window=green_light_sec
        free_window=free_window_sec
        while cars_on_crossroad:
            current_car=cars_on_crossroad.popleft()
            if len(current_car)==green_window:
                total_cars_passed+=1
                break
            elif len(current_car)<green_window:
                total_cars_passed+=1
                green_window-=len(current_car)
                continue
            else:
                left_chars=current_car[green_window:]
                if len(left_chars)>free_window:
                    print(f'A crash happened!\n{current_car} was hit at {left_chars[free_window]}.')
                    is_crash_happened=True
                    break
                elif len(left_chars)<=free_window:
                    total_cars_passed+=1
                    break
        if is_crash_happened:
            break
    command=input()

if not is_crash_happened:
    print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")




