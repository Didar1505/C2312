import threading
import time

def countdown(name, seconds):
    print(f"⏳ Timer '{name}' started for {seconds} seconds.")
    for i in range(seconds, 0, -1):
        print(f"{name}: {i} seconds left")
        time.sleep(1)
    print(f"✅ Timer '{name}' finished!\n")


# --- List of tasks ---
tasks = [
    ("Boil Eggs", 5),
    ("Bake Cookies", 8),
    ("Tea", 3)
]

# Output
"""
⏳ Timer 'Boil Eggs' started for 5 seconds.
⏳ Timer 'Bake Cookies' started for 8 seconds.
⏳ Timer 'Tea' started for 3 seconds.
Boil Eggs: 5 seconds left
Bake Cookies: 8 seconds left
Tea: 3 seconds left
...
✅ Timer 'Tea' finished!
✅ Timer 'Boil Eggs' finished!
✅ Timer 'Bake Cookies' finished!

🎉 All timers are done!
"""