import threading
import time

counter = 0

def increment():
    global counter
    for _ in range(100000):
        current_value = counter
        time.sleep(0) 
        counter = current_value + 1

threads = []
for _ in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter:", counter)
