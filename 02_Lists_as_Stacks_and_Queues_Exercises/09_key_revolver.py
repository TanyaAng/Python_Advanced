from collections import deque

price_per_bullet = int(input())
size_gun_barrel = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
intelligence = int(input())

counter = 0
while locks:
    if bullets:
        current_lock = locks.popleft()
        current_bullet = bullets.pop()
        counter += 1
        if current_bullet <= current_lock:
            print('Bang!')
        else:
            print('Ping!')
            locks.appendleft(current_lock)

        if counter % size_gun_barrel == 0 and bullets:
            print('Reloading!')
    else:
        break

if not locks:
    money_earned = intelligence - counter * price_per_bullet
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
