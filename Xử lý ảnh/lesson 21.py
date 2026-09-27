# Bài 21: Giới thiệu thư viện OpenCV và các thao tác cơ bản

import cv2
import numpy as np


file_path = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh\anh 1.jpg'

# Dùng numpy đọc file dưới dạng byte thô, sau đó đưa cho OpenCV giải mã
img_array = np.fromfile(file_path, np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

# Tách kênh màu
b, g, r = cv2.split(img)

# Chuyển đổi hệ màu
# Dùng hàm cvtColor để ép ma trận màu (BGR) hòa trộn lại thành 1 màu xám
gray_image= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hiển thị hình ảnh 
cv2.imshow("Ảnh gốc (Color)", img)

# Hiển thị từng kênh màu
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

# Chờ 1 khoảng thời gian 
cv2.waitKey(0) # 0 là chờ vĩnh viễn
cv2.destroyAllWindows()

# Cách chuyển đổi ảnh sang màu khác
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("gray_image", gray_image)
cv2.imshow("img_2", img_2)

# Chờ 1 khoảng thời gian 
cv2.waitKey(0) # 0 là chờ vĩnh viễn
cv2.destroyAllWindows()

height, width, z = img.shape
quater_h = height // 2
quater_w = width // 2

# Màu xanh lá (Blue=0, Green=255, Red=0)
green_color = (0, 255, 0)

# Copy ảnh gốc sang biến mới (Đặt tên rõ ràng để không nhầm)
img_colored = img.copy()

# Cú pháp: ma_trận[từ_hàng_0_đến_quater_h, từ_cột_0_đến_quater_w]
img_colored[0:quater_h, 0:quater_w] = green_color

# Hiển thị kết quả 
cv2.imshow("Ảnh gốc (Color)", img)
cv2.imshow("Ảnh to 1/4 màu xanh", img_colored)

# Chờ và dọn dẹp bộ nhớ
cv2.waitKey(0) 
cv2.destroyAllWindows()