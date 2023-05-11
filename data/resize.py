import os
from tqdm import tqdm
from PIL import Image
import time

max_size = (500, 500)

files = [x for x in os.listdir("originals")]

length = len(files)
pbar = tqdm(total=length)

for img_path in files:
	image = Image.open(f"originals/{img_path}")
	image.thumbnail(max_size)
	image.save(f"originals/{img_path}")
	print(img_path)


