import threading
import requests
import time

urls = [
    "https://picsum.photos/200/300",
    "https://picsum.photos/300/200",
    "https://picsum.photos/250/250",
    "https://picsum.photos/400/300",
    "https://picsum.photos/500/500"
]

def download_image(url, index):
    print(f"Downloading image {index}")
    r = requests.get(url)
    with open(f"image_{index}.jpg", "wb") as f:
        f.write(r.content)
    print(f"Finished image {index}")

start = time.time()
# ВАШ КОД ...


end = time.time()
print(f"All images downloaded in {end - start:.2f}s")
