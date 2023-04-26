# 影片疊合（加密）
<font size=5>Combine(
    <img src='data/video1.gif' width=150>,
    <img src='data/video2.gif' width=150>) =
    <img src='data/video1.gif' width=150>
</font><br></br>

<font size=5>Trans(
    <img src='data/video1.gif' width=150>)=
    <img src='data/video2.gif' width=150>
</font>

- 將B影片加密流程
  - 尋找一個A影片
  - 將A影片和B影片合併得到C影片
  - 將轉換器(trans)保存作為鑰匙

# 圖片疊合（加密）
<font size=5>Combine(
    <img src='data/tiger.jpeg' width=150>,
    <img src='data/flower.jpg' width=150>) =
    <img src='data/tiger.jpeg' width=150>
</font><br></br>

<font size=5>Trans(
    <img src='data/tiger.jpeg' width=150>)=
    <img src='data/flower.jpg' width=150>
</font>

- 定義 A (tiger) , B (flower)
    
  - 合併A與B得到C(看起來像B)
  - 將C過轉換器得到C_bar看起來像C)
  - C與C_bar透過轉換器可無損轉換1

- 原理
  - 將圖片轉換乘bit plane ,將令一張圖片壓縮至bit plane後面層，bit plane的特性 後面層對顯示的影像較小，因此可能儲存資訊，本專案做了三種合成器。

- 三種加密方式
  - method1 :[A8 A7 A6 A5 B5 B6 B7 B8]
  - method2 :[A8 A7 A6 00 00 B6 B7 B8]
  - method3 :[A8 A7 A6 A5 A4 A3 X1 X2]
  <br>#X1=[B8,B6,B4]的壓縮 X2=[B7,B5,B3]的壓縮</br>