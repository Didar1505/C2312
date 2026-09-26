import time 

def cpu_bound_task():
    count = 0
    for i in range(10**7):
        count += i
    
start_time = time.time()

for _ in range(4):
    cpu_bound_task()

end_time = time.time()

print(f"Время выполнение программы заняло: {end_time - start_time:.2f}")