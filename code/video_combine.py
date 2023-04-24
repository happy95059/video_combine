from img_combine import img_trans1 as trans1
from img_combine import img_trans2 as trans2
from img_combine import img_trans3 as trans3
import cv2
import numpy as np

# combine two vedio

def combine(v1,v2,row_cos,method = 1):
    video1 = cv2.VideoCapture(v1)
    video2 = cv2.VideoCapture(v2)
    rows ,cols = row_cos

    fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    out1 = cv2.VideoWriter('../data/video_combine.avi', fourcc, 20.0, (cols, rows),isColor = True)

    if not video1.isOpened():
        print("无法打开 video1")
        exit()
        
    if not video2.isOpened():
        print("无法打开 video3")
        exit()
    a=0
    # 循环读取 webcam 的每一帧并保存
    while True:
        # 读取一帧
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()
        # 检查是否成功读取一帧
        if not ret1:
            print("video1 无法读取一帧")
            break
        if not ret2:
            print("video2 无法读取一帧")
            break
        
            
        a+=1
        
        if   method==1:
            T = trans1(rows,cols)
        elif method==2:
            T = trans2(rows,cols)
        elif method==3:
            T = trans3(rows,cols)
        trans_frame = T.rgb_combine_img(frame1, frame2)
        
        # 把当前帧写入视频
        out1.write(trans_frame)

        # 显示当前帧
        cv2.imshow('Webcam', trans_frame)

        # 按下 q 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放资源
    video1.release()
    video2.release()
    out1.release()
    cv2.destroyAllWindows()
 
# trans your combine's vedio    

def trans(video,row_col,method = 1):
    video1 = cv2.VideoCapture(video)
    rows, cols = row_col

    fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    out1 = cv2.VideoWriter('../data/video_trans.avi', fourcc, 20.0, (cols, rows),isColor = True)

    if not video1.isOpened():
        print("无法打开 vedio")
        exit()
        
    a=0
    # 循环读取 webcam 的每一帧并保存
    while True:
        # 读取一帧
        ret, frame = video1.read()
        # 检查是否成功读取一帧
        if not ret:
            print("无法读取一帧")
            break
        a+=1
        
        if   method==1:
            T = trans1(rows,cols)
        elif method==2:
            T = trans2(rows,cols)
        elif method==3:
            T = trans3(rows,cols)
        ans = T.rgb_trans_picture(frame)
        # 把当前帧写入视频
        out1.write(ans)

        # 显示当前帧
        cv2.imshow('Webcam', ans)

        # 按下 q 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放资源
    video1.release()
    out1.release()
    cv2.destroyAllWindows()
 
    
if __name__=='__main__':
    
    
    combine('../data/video1.mp4', '../data/video2.mp4', [480,640],2)
    
    trans('../data/video_combine.avi', [480,640],2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


