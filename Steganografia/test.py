from matplotlib import pyplot as plt
from skimage import img_as_float
import skimage.io as io
from skimage.color import rgb2gray
import random


def get_Sn(image_to_watermark, seed, n, a=0.004):
    i = 0
    while i < len(image_to_watermark):
        j = 0
        while j < len(image_to_watermark[i]):
            if image_to_watermark[i][j] < a:
                image_to_watermark[i][j] = a
            if image_to_watermark[i][j] > 1 - a:
                image_to_watermark[i][j] = 1 - a
            j += 1
        i += 1

    random.seed(seed)

    to_change = []
    for i in range(n):
        to_change.append(
            (
                (random.randint(0, len(image_to_watermark) - 1), random.randint(0, len(image_to_watermark[0]) - 1)),
                (random.randint(0, len(image_to_watermark) - 1), random.randint(0, len(image_to_watermark[0]) - 1))
            )
        )
    watermarked_img = image_to_watermark.copy()

    Sn = 0
    for pixels in to_change:
        Sn += watermarked_img[pixels[0][0]][pixels[0][1]] - watermarked_img[pixels[1][0]][pixels[1][1]]
    return Sn


def watermark(image_to_watermark, seed, n, a=0.004):
    i = 0
    while i < len(image_to_watermark):
        j = 0
        while j < len(image_to_watermark[i]):
            if image_to_watermark[i][j] < a:
                image_to_watermark[i][j] = a
            if image_to_watermark[i][j] > 1 - a:
                image_to_watermark[i][j] = 1 - a
            j += 1
        i += 1

    random.seed(seed)

    to_change = []
    for i in range(n):
        to_change.append(
            (
                (random.randint(0, len(image_to_watermark) - 1), random.randint(0, len(image_to_watermark[0]) - 1)),
                (random.randint(0, len(image_to_watermark) - 1), random.randint(0, len(image_to_watermark[0]) - 1))
            )
        )
    watermarked_img = image_to_watermark.copy()
    for pixels in to_change:
        watermarked_img[pixels[0][0]][pixels[0][1]] += a
        watermarked_img[pixels[1][0]][pixels[1][1]] -= a

    Sn = 0
    for pixels in to_change:
        Sn += watermarked_img[pixels[0][0]][pixels[0][1]] - watermarked_img[pixels[1][0]][pixels[1][1]]
    return watermarked_img, Sn


def check(image_to_check, seed, n, a=0.004):
    random.seed(seed)

    to_change = []
    for i in range(n):
        to_change.append(
            (
                (random.randint(0, len(image_to_check) - 1), random.randint(0, len(image_to_check[0]) - 1)),
                (random.randint(0, len(image_to_check) - 1), random.randint(0, len(image_to_check[0]) - 1))
            )
        )
    image_after_check = image_to_check.copy()
    for pixels in to_change:
        image_after_check[pixels[0][0]][pixels[0][1]] -= a
        image_after_check[pixels[1][0]][pixels[1][1]] += a

    Sn = 0
    for pixels in to_change:
        Sn += image_after_check[pixels[0][0]][pixels[0][1]] - image_after_check[pixels[1][0]][pixels[1][1]]
    return image_after_check, Sn


imgo = img_as_float(io.imread('test.png'))
imgo = rgb2gray(imgo)
changed_img = img_as_float(io.imread('changed_test.png'))
changed_img = rgb2gray(changed_img)

rand_seed = 15

oSn = get_Sn(imgo, rand_seed, 100)
img_with_watermark, Si0 = watermark(imgo, rand_seed, 100)
tmp1, Si1 = check(changed_img, rand_seed, 100)
tmp2, Si2 = check(img_with_watermark, rand_seed, 100)

fig, axs = plt.subplots(1, 3)
axs[0].imshow(imgo, cmap="gray")
axs[1].imshow(img_with_watermark, cmap="gray")
axs[2].imshow(changed_img, cmap="gray")

fig.set_size_inches(14, 10)
plt.show()

print("Original value: ", round(oSn, 5))
print("Value for edited picture: ", round(Si1, 5))
print("Value for unedited picture: ", round(Si2, 5))
