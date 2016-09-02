from PIL import Image, ImageOps
from glob import glob

size = 256, 144
images = glob('../images/*.jpg')
images = [i for i in images if 'thumb' not in i]

def resize(image):
    print image
    name, ext = image[2:].split('.')
    expName = '..' + name+'_thumb.'+ext
    img = Image.open(image)
    img = ImageOps.fit(img, size, Image.ANTIALIAS)
    img.save(expName, "JPEG", quality=95)
    img.close()
    
if __name__ == '__main__':
    for image in images:
        resize(image)
     
    
