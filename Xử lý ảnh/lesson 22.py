# Bài 22: Sử dụng OpenCV để vẽ các hình cơ bản 

import cv2
import numpy as np

def display(title, img):
    cv2.imshow(title, img)
    # Chờ 1 khoảng thời gian
    cv2.waitKey(0)
    # Đóng window
    cv2.destroyAllWindows()

# Tạo 1 ảnh (thử tạo 1 ảnh toàn là số 0)
img = np.zeros((400, 400, 3), dtype = np.uint8)
display("Image", img)

# Vẽ đường thẳng 
cv2.line(img, (50, 50), (350, 50), (0, 0, 255), 2) # Vẽ màu đỏ
display("Image", img)

# Vẽ đường tròn
cv2.circle(img, (100, 100), 50, (0, 255, 0), -1)
display("Image", img)

# Vẽ hình chữ nhật 
cv2.rectangle(img, (30, 30), (370, 70), (255, 0, 0), 2)
display("Image", img)

# Ghi text trên hình ảnh 
content = "Tran Trung Hieu"
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, content, (10, 380), font, 0.6, (255, 255, 255), 2)
display("Image", img)