import time

def worker(num, sec):
    print(f"Worker {num} started")
    time.sleep(sec)
    print(f"Worker {num} finished")

tasks  = [
    ('chrome.exe', 2), 
    ('telegram.exe', 1), 
    ('video.exe', 3), 
    ('song.exe', 1),
    ('store.exe', 2),
    ]

# TODO: использовать цикл for для создание 5 потоков и передать задачи в worker из tasks
