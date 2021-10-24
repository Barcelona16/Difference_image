# Difference_image
计算两个图像的相似度(cosine + SSIM)

# interface 
Compute(imgpath1,imgpath2)

# Examples

compute('2_1.jpg', '2_2.jpg')
compute('dogparty1.jpg','dogparty2.jpg')

```
$ python difference_image.py
---------
compare 
 2_1.jpg 2_2.jpg 

图片余弦相似度 0.9590403818886338
SSIM图像失真度  0.6480795714242451
---------

---------
compare 
 dogparty1.jpg dogparty2.jpg 

图片余弦相似度 0.9267255157392655
SSIM图像失真度  0.6440620256559084
---------


```
