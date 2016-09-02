from PIL import Image
from glob import glob

size = 256, 144
images = glob('../images/*.jpg')
images = [i for i in images if 'thumb' not in i]

for image in images:
    print image
    name, ext = image[2:].split('.')
    expName = '..' + name+'_thumb.'+ext
    img = Image.open(image)
    img.thumbnail(size, Image.ANTIALIAS)
    background = Image.new('RGBA', size, (255, 255, 255, 0))
    background.paste(img, ((size[0] - img.size[0]) / 2, (size[1] - img.size[1]) / 2))
    background.save(expName, "JPEG", quality=95)
    img.close()
    background.close()
