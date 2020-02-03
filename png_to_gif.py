import os
import sys
import imageio
import regex as re

png_dir = sys.argv[1] 
images = []
dirFiles = os.listdir(png_dir)
dirFiles.sort(key=lambda f: int(re.sub('\D', '', f)))

print('making gif...')
for file_name in dirFiles:
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('movie.gif', images, duration=0.25)
