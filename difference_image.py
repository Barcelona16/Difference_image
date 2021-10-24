'''
Author: Deavan
Date: 2021-10-24 21:00:45
Description: 
'''
from PIL import Image
from numpy import average, dot, linalg

# 对图片进行统一化处理
def get_thum(image, size=(64,64), greyscale=False):
    # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
        image = image.convert('L')
    return image
 
# 计算图片的余弦距离
def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thum(image1)
    image2 = get_thum(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        # linalg=linear（线性）+algebra（代数），norm则表示范数
        # 求图片的范数？？
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    # dot返回的是点积，对二维数组（矩阵）进行计算
    res = dot(a / a_norm, b / b_norm)
    return res

def compute(im1,im2):
    # im1 = '2_1.jpg'
    # m2 = '2_20.jpg'
    print("---------\ncompare \n", im1,im2,"\n")
    image1 = Image.open(im1)
    image2 = Image.open(im2)
    cosin = image_similarity_vectors_via_numpy(image1, image2)
    print('图片余弦相似度',cosin)

    from skimage.measure import compare_ssim
    import imageio
    import numpy as np
    
    # 读取图片
    img1 = imageio.imread(im1)
    img2 = imageio.imread(im2)
    img2 = np.resize(img2, (np.array(img1).shape[0], np.array(img1).shape[1], np.array(img1).shape[2]))
    ssim =  compare_ssim(img1, img2, multichannel = True)
    print('SSIM图像失真度 ',ssim)
    print("---------\n")

if __name__ == '__main__':
    compute('2_1.jpg', '2_2.jpg')
    compute('dogparty1.jpg','dogparty2.jpg')