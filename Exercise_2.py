import time

def do_work(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} finished after {delay} seconds")

# TODO: create 3 threads using the same function
# Example: do_work("A", 1), do_work("B", 2), do_work("C", 3)
