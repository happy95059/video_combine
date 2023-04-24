import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr


          # [ A8 A7 A6 A5 
          #   B5 B6 B7 B8 ]
class img_trans1:
    def __init__(self,rows=600,cols=1000):
        self.rows = rows
        self.cols = cols
        
        #   img  --> img_bit
    def bit_plane(self,img):
        return [(img & (1 << i)) for i in range(8)]

        #   img1_bit  --> img2_bit
    def inverte_bit(self,img_bit):  
        ans = []
        for i in range(7,3,-1):
            ans.append(img_bit[i]/(2**(i-(7-i))))     
        for i in range(3,-1,-1):
            ans.append(img_bit[i]*(2**(1+(3-i)*2)))
        ans=np.array(ans).astype('uint8')
        return ans


    def show_img_and_bit_img(self,img ,bit_img):
        plt.subplot(3,3,1)
        plt.imshow(img,'gray')
        plt.title("Origin")
        for i in range(8,0,-1):
            plt.subplot(3,3,10-i)
            plt.imshow(bit_img[i-1],'gray')
            plt.title("Bit = %d"%(i))
        plt.show()
        
        
        # img1 + img2 --> img
    def combine_img(self,img1,img2):
        img1 = cv2.resize(img1, (self.cols,self.rows))
        img2 = cv2.resize(img2, (self.cols,self.rows))
        
        img1_bit = self.bit_plane(img1)
        img2_bit = self.bit_plane(img2)

        inverse_img2 = self.inverte_bit(img2_bit)

        
        ans = np.sum(img1_bit[4:8],0) + np.sum(inverse_img2[0:4],0)
        return ans.astype("uint8")
        
        # img1 --> img2
    def trans_picture(self,img):
        bit_img = self.bit_plane(img)
        inverte_img = self.inverte_bit(bit_img)
        return np.sum(inverte_img,0)


    def rgb_combine_img(self,img1,img2):
        r1,g1,b1 = cv2.split(img1)
        r2,g2,b2 = cv2.split(img2)

        r_ans = self.combine_img(r1,r2).astype('uint8')
        g_ans = self.combine_img(g1,g2).astype('uint8')
        b_ans = self.combine_img(b1,b2).astype('uint8')
        return cv2.merge([r_ans,g_ans,b_ans])

    def rgb_trans_picture(self,img):
        r, g, b = cv2.split(img)
        
        r = self.trans_picture(r).astype('uint8')
        g = self.trans_picture(g).astype('uint8')
        b = self.trans_picture(b).astype('uint8')
        return cv2.merge([r,g,b])



       # [A8 A7 A6 X   
       #  X B6 B7 B8 ]    
class img_trans2:
    def __init__(self,rows=600,cols=1000):
        self.rows = rows
        self.cols = cols
        
        #   img  --> img_bit
    def bit_plane(self,img):
        return [(img & (1 << i)) for i in range(8)]

        #   img1_bit  --> img2_bit
    def inverte_bit(self,img_bit):  
        ans = []
        for i in range(7,4,-1):
            ans.append(img_bit[i]/(2**(i-(7-i))))     
        ans.append(np.zeros([self.rows,self.cols]))
        ans.append(np.zeros([self.rows,self.cols]))
        for i in range(2,-1,-1):
            ans.append(img_bit[i]*(2**(1+(3-i)*2)))
        ans=np.array(ans).astype('uint8')
        return ans


    def show_img_and_bit_img(self,img ,bit_img):
        plt.subplot(3,3,1)
        plt.imshow(img,'gray')
        plt.title("Origin")
        for i in range(8,0,-1):
            plt.subplot(3,3,10-i)
            plt.imshow(bit_img[i-1],'gray')
            plt.title("Bit = %d"%(i))
        plt.show()
        
        
        # img1 + img2 --> img
    def combine_img(self,img1,img2):
        img1 = cv2.resize(img1, (self.cols,self.rows))
        img2 = cv2.resize(img2, (self.cols,self.rows))
        
        img1_bit = self.bit_plane(img1)
        img2_bit = self.bit_plane(img2)

        inverse_img2 = self.inverte_bit(img2_bit)

        
        ans = np.sum(img1_bit[5:8],0) + np.sum(inverse_img2[0:3],0)
        return ans.astype("uint8")
        
        # img1 --> img2
    def trans_picture(self,img):
        bit_img = self.bit_plane(img)
        inverte_img = self.inverte_bit(bit_img)
        return np.sum(inverte_img,0)


    def rgb_combine_img(self,img1,img2):
        r1,g1,b1 = cv2.split(img1)
        r2,g2,b2 = cv2.split(img2)

        r_ans = self.combine_img(r1,r2).astype('uint8')
        g_ans = self.combine_img(g1,g2).astype('uint8')
        b_ans = self.combine_img(b1,b2).astype('uint8')
        return cv2.merge([r_ans,g_ans,b_ans])

    def rgb_trans_picture(self,img):
        r, g, b = cv2.split(img)
        
        r = self.trans_picture(r).astype('uint8')
        g = self.trans_picture(g).astype('uint8')
        b = self.trans_picture(b).astype('uint8')
        return cv2.merge([r,g,b])
    

# A8 A7 A6 A5 A4 A3 [B8 B6 B4] [B7 B5 B3]

class img_trans3:
    def __init__(self,rows=600,cols=1000):
        self.rows = rows
        self.cols = cols
    def bit_plane(self,img):
        return np.array([(img & (1 << i)) for i in range(8)])

    def compress_3to1(self,three_img):
        rows = self.rows
        cols = self.cols

        rC = np.zeros([rows,cols], dtype=np.uint8)
        gC = np.zeros([rows,cols], dtype=np.uint8)
        bC = np.zeros([rows,cols], dtype=np.uint8)

        rC[0:rows:2,1:cols:2]=three_img[0][0:rows:2,1:cols:2]
        gC[0:rows:2,0:cols:2]=three_img[1][0:rows:2,0:cols:2]
        gC[1:rows:2,1:cols:2]=three_img[1][1:rows:2,1:cols:2]
        bC[1:rows:2,0:cols:2]=three_img[2][1:rows:2,0:cols:2]
        return (rC+gC+bC).astype('uint8')
        #RC

    def decompress_1to3(self,img):
        rows = self.rows
        cols = self.cols
        rC = np.zeros([rows,cols], dtype=np.uint16)
        gC = np.zeros([rows,cols], dtype=np.uint16)
        bC = np.zeros([rows,cols], dtype=np.uint16)
        
        rC[0:rows:2,1:cols:2]=img[0:rows:2,1:cols:2]
        gC[0:rows:2,0:cols:2]=img[0:rows:2,0:cols:2]
        gC[1:rows:2,1:cols:2]=img[1:rows:2,1:cols:2]
        bC[1:rows:2,0:cols:2]=img[1:rows:2,0:cols:2]
          
        rC[0:rows-1:2,2:cols-1:2]=(rC[0:rows-1:2,1:cols-2:2]+rC[0:rows-1:2,3:cols:2])/2
        rC[1:rows-1:2,1:cols-1:2]=(rC[0:rows-2:2,1:cols-1:2]+rC[2:rows:2,1:cols-1:2])/2
        rC[1:rows-1:2,2:cols-1:2]=(rC[0:rows-2:2,1:cols-2:2]+rC[0:rows-2:2,3:cols:2]+rC[2:rows:2,1:cols-2:2]+rC[2:rows:2,3:cols:2])/4
        #RB

        bC[1:rows-1:2,1:cols-1:2]=(bC[1:rows-1:2,0:cols-2:2]+bC[1:rows-1:2,2:cols:2])/2
        bC[2:rows-1:2,0:cols-1:2]=(bC[1:rows-2:2,0:cols-1:2]+bC[3:rows:2,0:cols-1:2])/2
        bC[2:rows-1:2,1:cols-1:2]=(bC[1:rows-2:2,0:cols-2:2]+bC[1:rows-2:2,2:cols:2]+bC[3:rows:2,0:cols-2:2]+bC[3:rows:2,2:cols:2])/4
        #RG

        gC[1:rows-1:2,2:cols-1:2]=(gC[0:rows-2:2,2:cols-1:2]+gC[2:rows:2,2:cols-1:2]+gC[1:rows-1:2,1:cols-2:2]+gC[1:rows-1:2,3:cols:2])/4 
        gC[2:rows-1:2,1:cols-1:2]=(gC[1:rows-2:2,1:cols-1:2]+gC[3:rows:2,1:cols-1:2]+gC[2:rows-1:2,0:cols-2:2]+gC[2:rows-1:2,2:cols:2])/4 
        return [rC,gC,bC]



    def show_img_and_bit_img(self,img ,bit_img):
        plt.subplot(3,3,1)
        plt.imshow(img,'gray')
        plt.title("Origin")
        for i in range(8,0,-1):
            plt.subplot(3,3,10-i)
            plt.imshow(bit_img[i-1],'gray')
            plt.title("Bit = %d"%(i))
        plt.show()
        
      
        #   img1  -->  img2
    def trans_picture(self,img):  
        img_bit = self.bit_plane(img).astype('uint8')
        trans_bit = [0,0,0,0,0,0,0,0]

        trans_bit[0] = self.compress_3to1([img_bit[4]/2**4,img_bit[6]/2**6,img_bit[2]/2**2])
        trans_bit[1] = self.compress_3to1([img_bit[5]/2**5,img_bit[7]/2**7,img_bit[3]/2**3])*2
        
        
        trans_bit[5], trans_bit[7], trans_bit[3] = self.decompress_1to3(img_bit[1]/2)
        trans_bit[4], trans_bit[6], trans_bit[2] = self.decompress_1to3(img_bit[0])
        for i in range(2,8):
            trans_bit[i] = trans_bit[i] * 2 ** i
        return np.sum(trans_bit[0:8],0).astype('uint8')    
      
        # img1 + img2 --> img
    def combine_img(self,img1,img2):

        img1 = cv2.resize(img1, (self.cols,self.rows))
        img2 = cv2.resize(img2, (self.cols,self.rows))

        bit = [0,0,0,0,0,0,0,0]
        
        img1_bit = self.bit_plane(img1)
        img2_bit = self.bit_plane(img2)
        
        bit2 = self.compress_3to1([img1_bit[5]/2**5,img1_bit[7]/2**7,img1_bit[3]/2**3])*2
        bit1 = self.compress_3to1([img1_bit[4]/2**4,img1_bit[6]/2**6,img1_bit[2]/2**2])


        bit[1] = self.compress_3to1([img2_bit[5]/2**5,img2_bit[7]/2**7,img2_bit[3]/2**3])*2
        bit[0] = self.compress_3to1([img2_bit[4]/2**4,img2_bit[6]/2**6,img2_bit[2]/2**2])
         
        bit[5], bit[7], bit[3] = self.decompress_1to3(bit2/2)
        bit[4], bit[6], bit[2] = self.decompress_1to3(bit1)
        for i in range(2,8):
            bit[i] = bit[i] * 2 ** i
        return (np.sum(bit[0:8],0)).astype("uint8")


    def rgb_combine_img(self,img1,img2):
        r1,g1,b1 = cv2.split(img1)
        r2,g2,b2 = cv2.split(img2)

        r_ans = self.combine_img(r1,r2)
        g_ans = self.combine_img(g1,g2)
        b_ans = self.combine_img(b1,b2)

        return cv2.merge([r_ans,g_ans,b_ans]).astype('uint8')

    def rgb_trans_picture(self,img):
        r, g, b = cv2.split(img)
        
        r = self.trans_picture(r)
        g = self.trans_picture(g)
        b = self.trans_picture(b)
        plt.imshow(cv2.merge([r,g,b]))
        return cv2.merge([r,g,b])



# start

if __name__=='__main__':
    rows = 600
    cols = 1000
    
    
    # method img_trans1 or img_trans2 or img_trans3
    X = img_trans2(rows,cols)
    
    # gray combine img
    tiger = cv2.imread('../data/tiger.jpeg', 0)
    flower = cv2.imread('../data/flower.jpg', 0)

    tiger_bit = X.bit_plane(tiger)
    flower_bit = X.bit_plane(flower)


    tiger = cv2.resize(tiger,(cols,rows))
    flower = cv2.resize(flower,(cols,rows))

    ans = X.combine_img(tiger,flower)
    ans2 = X.trans_picture(ans)
    ans1 = X.trans_picture(ans2)

    plt.subplot(2,2,1)
    plt.imshow(tiger,'gray')
    plt.title("origin tiger")

    plt.subplot(2,2,2)
    plt.imshow(flower,'gray')
    plt.title("origin flower")

    plt.subplot(2,2,3)
    plt.imshow(ans1,'gray')
    plt.title("trans tiger")

    plt.subplot(2,2,4)
    plt.imshow(ans2,'gray')
    plt.title("trans flower")
    plt.show()

    # color combine image
    rgb_tiger = cv2.imread('../data/tiger.jpeg')
    rgb_flower = cv2.imread('../data/flower.jpg')

    rgb_tiger = cv2.cvtColor(rgb_tiger, cv2.COLOR_BGR2RGB)
    rgb_flower = cv2.cvtColor(rgb_flower, cv2.COLOR_BGR2RGB)

    rgb_tiger = cv2.resize(rgb_tiger,(cols,rows))
    rgb_flower = cv2.resize(rgb_flower,(cols,rows))


    rgb_ans = X.rgb_combine_img(rgb_tiger,rgb_flower)


    rgb_ans2 = X.rgb_trans_picture(rgb_ans)
    rgb_ans1 = X.rgb_trans_picture(rgb_ans2)
    
    
    plt.subplot(2,2,1)
    plt.imshow(rgb_tiger)
    plt.title("origin tiger")

    plt.subplot(2,2,2)
    plt.imshow(rgb_flower)
    plt.title("origin flower")

    plt.subplot(2,2,3)
    plt.imshow(rgb_ans1)
    plt.title("trans tiger")

    plt.subplot(2,2,4)
    plt.imshow(rgb_ans2)
    plt.title("trans flower")
    plt.show()
    
    psnr_tiger = psnr(rgb_tiger, rgb_ans1, data_range = 255)
    print('PSNR tiger=',psnr_tiger)
    
    psnr_flower = psnr(rgb_flower, rgb_ans2, data_range = 255)
    print('PSNR flower=',psnr_flower)
    
    # show bit plane
    X.show_img_and_bit_img(ans1, X.bit_plane(ans1))
    X.show_img_and_bit_img(ans2, X.bit_plane(ans2))





