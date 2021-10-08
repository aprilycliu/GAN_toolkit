from PIL import Image
import glob
import os

def resize_image(newpath, oldpath):
    if not os.path.exists(newpath):
    os.makedirs(newpath)

    for filename in glob.glob(oldpath+"/*.jpeg"): #path of raw images, filetype to be modified
    img = Image.open(filename).resize((256,256)) #size to be modified
    # save resized images to new folder with existing filename
    img.save('{}{}{}'.format(newpath,'/',os.path.split(filename)[1]))

def crop_image(newpath, oldpath):
    #newpath as the assigned new folder
    #oldpath as the current folder with images to be cropped
    if not os.path.exists(newpath):
    os.makedirs(newpath)

    for filename in glob.glob(oldpath+"/*.jpeg"):
        im = Image.open(filename)
        left = 0
        top = 140
        right = 1280
        bottom = 720 #cropped dimenstion to be modified

        im1 = im.crop((left, top, right, bottom))
        im1.save('{}{}{}'.format(path,'/',os.path.split(filename)[1]))
