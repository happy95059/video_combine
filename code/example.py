import cv2
import video_combine
import img_combine
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
#########################################            image              ########################################


rows = 600
cols = 1000

# choose method   img_trans1 or img_trans2 or img_trans3
X = img_combine.img_trans2(rows,cols)


# gray combine img
tiger = cv2.imread('../data/tiger.jpeg', 0)
flower = cv2.imread('../data/flower.jpg', 0)

tiger = cv2.resize(tiger,(cols,rows))
flower = cv2.resize(flower,(cols,rows))

ans = X.combine_img(tiger,flower)
ans2 = X.trans_picture(ans)
ans1 = X.trans_picture(ans2)


# color combine image
rgb_tiger = cv2.imread('../data/tiger.jpeg')
rgb_flower = cv2.imread('../data/flower.jpg')

rgb_tiger = cv2.resize(rgb_tiger,(cols,rows))
rgb_flower = cv2.resize(rgb_flower,(cols,rows))


rgb_ans = X.rgb_combine_img(rgb_tiger,rgb_flower)


rgb_ans2 = X.rgb_trans_picture(rgb_ans)
rgb_ans1 = X.rgb_trans_picture(rgb_ans2)

# show bit plane
X.show_img_and_bit_img(ans1, X.bit_plane(ans1))
X.show_img_and_bit_img(ans2, X.bit_plane(ans2))






psnr_tiger = psnr(rgb_tiger, rgb_ans1, data_range = 255)
print('PSNR tiger=',psnr_tiger)

psnr_flower = psnr(rgb_flower, rgb_ans2, data_range = 255)
print('PSNR flower=',psnr_flower)





#########################################            video              ########################################

# out video_combine.avi 
video_combine.combine('../data/video1.mp4', '../data/video2.mp4', [300,500],2)

# out video_trans.avi
video_combine.trans('../data/video_combine.avi', [300,500],2)




