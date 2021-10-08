import skimage.io as sk
from scipy.linalg import norm
import matplotlib.pyplot as plt
from scipy import sum, average
import glob
import os
import imageio

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

def to_grayscale(arr):
    #If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def compare_images(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)
    # calculate the difference and its norms
    diff = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diff))  # Manhattan norm

    return m_norm

def pixeldistance(query, real_dir):

    img_raw_1 = cv2.imread(query)
    img1 = to_grayscale(img_raw_1)

    ls=[]

    for filename in glob.glob(real_dir +'*.jpg'):
        img_raw_2 = cv2.imread(filename)
        img2 = to_grayscale(img_raw_2)
        diff = img1 - img2
        m_norm = sum(abs(diff))
        ls.append([m_norm, filename])

    return sorted(ls)[:3]

query = '/seed0001.png'
real_dir = '/Task1/256-with-tool-small/'
top3= pixeldistance(query, real_dir)

fig, axes = plt.subplots(1, 4, figsize=(12, 8))
ax = axes.ravel()
[ax.set_axis_off() for ax in ax.ravel()]

ax[0].imshow(sk.imread(query))
ax[1].imshow(sk.imread(top3[0][1]))
ax[2].imshow(sk.imread(top3[1][1]))
ax[3].imshow(sk.imread(top3[2][1]))
