# from PIL import Image, ImageFilter
# import glob
# import time

# files = glob.glob('images/*.jpg')

# t1 = time.time()

# for index, img_file in enumerate(files):
#     img = Image.open(img_file)
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img.thumbnail((1200,1200))

#     filename = img_file.split('\\')[-1]
#     img.save(f'processed/{filename}')
#     print(f'image - {index} was processed')

# t2 = time.time()

# print(f"end time: {t2 - t1:.2f}")


from PIL import Image, ImageFilter
import glob
from concurrent.futures import ProcessPoolExecutor
import time


img_names = glob.glob('images/*.jpg')

def process_image(img_file):
    img = Image.open(img_file)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail((1200,1200))

    filename = img_file.split('\\')[-1]
    img.save(f'processed/{filename}')
    print(f'{filename} - was processed')

if __name__ == "__main__":
    t1 = time.time()

    with ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)
        
    t2 = time.time()

    print(f"end time: {t2 - t1:.2f}")