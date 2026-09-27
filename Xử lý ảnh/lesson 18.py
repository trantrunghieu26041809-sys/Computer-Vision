# Bài 18: Bộ lọc Gaussian làm mờ ảnh 
# Sử dụng thư viện Scipy làm mờ ảnh 

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

# Chuyển sang ảnh xám 
gray_image = im.convert('L')

# Chuyển ảnh xám về mảng numpy
image_a = np.array(gray_image)

# Làm mờ ảnh xám với bộ lọc Gaussian
# Sigma càng lớn thì ảnh càng mờ 
blurred_image_a = ndimage.gaussian_filter(image_a, sigma=1, mode='constant')
blurred_image_b = ndimage.gaussian_filter(image_a, sigma=3, mode='constant')
blurred_image_c = ndimage.gaussian_filter(image_a, sigma=5, mode='constant')

# Hiển thị ảnh bằng imshow()
plt.figure(figsize=(10, 8)) 

plt.subplot(2, 2, 1)
plt.imshow(image_a, cmap='gray')
plt.title('Anh xam goc')
plt.axis('off') 

plt.subplot(2, 2, 2)
plt.imshow(blurred_image_a, cmap='gray')
plt.title('Sigma = 1')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(blurred_image_b, cmap='gray')
plt.title('Sigma = 3')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(blurred_image_c, cmap='gray')
plt.title('Sigma = 5')
plt.axis('off')


plt.tight_layout()

# Show ảnh 
plt.show()