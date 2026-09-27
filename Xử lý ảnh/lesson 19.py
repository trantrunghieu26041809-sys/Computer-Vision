# Bài 19: Bộ lọc hàm Sobel (Tìm cạnh)
# Thuật toán nhận dạng đường biên (Edge Detection) dùng phương pháp Sobel cho ảnh xám

from scipy import ndimage 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

# Thư mục chứa hình ảnh
dir_path = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Đường dẫn đến hình ảnh
image_path = os.path.join(dir_path, 'anh 1.jpg')
print("Đường dẫn file gốc:", image_path)

# Sử dụng Image.open() đọc ảnh
im = Image.open(image_path)

# Chuyển sang ảnh xám và đưa về mảng numpy
gray_image = im.convert('L')
image_a = np.array(gray_image)

# Tính gradient (đạo hàm) bằng bộ lọc Sobel
# axis = 1: Đạo hàm theo chiều ngang (tìm các đường viền dọc)
gradient_x = ndimage.sobel(image_a, axis=1, mode='constant') 

# axis = 0: Đạo hàm theo chiều dọc (tìm các đường viền ngang)
gradient_y = ndimage.sobel(image_a, axis=0, mode='constant')

# Hiển thị ảnh 
plt.figure(figsize=(8, 10))

# 1. Ảnh xám gốc
plt.subplot(3, 1, 1)
plt.imshow(image_a, cmap='gray')
plt.title('Ảnh xám gốc')
plt.axis('off')

# 2. Gradient hướng X
plt.subplot(3, 1, 2)
plt.imshow(gradient_x, cmap='gray')
plt.title('Gradient hướng X (Tìm cạnh ngang)')
plt.axis('off')

# 3. Gradient hướng Y
plt.subplot(3, 1, 3)
plt.imshow(gradient_y, cmap='gray')
plt.title('Gradient hướng Y (Tìm cạnh dọc)')
plt.axis('off')

plt.tight_layout()
plt.show()