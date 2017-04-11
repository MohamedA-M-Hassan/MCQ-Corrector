from circhoughtrans import getCenterOfBottomLeftCircle


def crop(src):
    x, y = getCenterOfBottomLeftCircle(src)
    return src[x-780:x-145, y-25:y+820]


def vertical_crop(img):
    img1 = img[:, 0:175]
    img2 = img[:, 340:510]
    img3 = img[:, 670:]
    return [img1, img2, img3]

