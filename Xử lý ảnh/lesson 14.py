# Bài 14: Biến đổi ảnh xám (biến đổi mức độ sáng tối của ảnh)

import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Đường dẫn thư mục chứa ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'
image_path = os.path.join(my_dir, 'anh 1.jpg')

# Đọc ảnh và hiển thị 
im = Image.open(image_path)

# Chuyển đổi hình ảnh thành mảng (dùng float để chống tràn bộ nhớ khi bình phương)
image_array = np.array(im.convert('L'), dtype=float)

# Biến đổi ảnh xám theo yêu cầu 
inverted_image = 255 - image_array # Invert ảnh bằng cách lấy 255 - giá trị pixel
squared_image = image_array ** 2 # Bình phương giá trị pixel
clamped_image = np.clip(image_array, 100, 200) # Giới hạn giá trị pixel trong khoảng 100-200

# Hiển thị hình ảnh gốc và hình ảnh đã biến đổi với khoảng trắng
fig, axs = plt.subplots(2, 2, figsize = (10, 10))
fig.subplots_adjust(wspace = 0.3, hspace = 0.3)

# Ô thứ 1: Hàng 0, Cột 0
axs[0, 0].imshow(image_array, cmap = 'gray')
axs[0, 0].set_title('Hình ảnh gốc')

# Ô thứ 2: Hàng 0, Cột 1
axs[0, 1].imshow(inverted_image, cmap = 'gray')
axs[0, 1].set_title('Ảnh âm bản (Inverted)')

# Ô thứ 3: Hàng 1, Cột 0
axs[1, 0].imshow(squared_image, cmap = 'gray')
axs[1, 0].set_title('Bình phương (Squared)')

# Ô thứ 4: Hàng 1, Cột 1
axs[1, 1].imshow(clamped_image, cmap = 'gray')
axs[1, 1].set_title('Giới hạn độ sáng (Clamped)')

plt.show()