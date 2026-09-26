import time

def clock():
    count = 0
    while True:
        count += 1
        print(f"[Clock] {count} seconds passed...")
        time.sleep(1)

def do_work():
    for i in range(5):
        print(f"[Work] Doing task {i+1}")
        time.sleep(2)
    print("[Work] Done!")

# TODO: Написать поток который программа будет завершения фунцкии do_work() 