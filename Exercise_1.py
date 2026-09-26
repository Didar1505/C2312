import time

def watch_tv():
    time.sleep(6)
    print("watching tv")

def eat_popcorn():
    time.sleep(4)
    print("eating poporn ")

def talk_on_phone():
    time.sleep(3)
    print('talking on the phone with friends')

# Начало секуномера
start_time = time.time()

# ВАШ КОД ...

# Конец секундомера
end_time = time.time()

print(f"-- Конец всех задач: {end_time - start_time:.2f}")