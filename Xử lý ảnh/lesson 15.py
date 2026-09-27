# Bài 15: Cân bằng lược đồ ảnh xám 

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def histogram_equalization(image, nbr_bins=256):
    # Đảm bảo hình ảnh đầu vào là ảnh xám
    if image.mode != 'L':
        image = image.convert('L')
        
    # Chuyển đổi hình ảnh thành mảng NumPy
    image_array = np.array(image)
    
    # Tính toán histogram của ảnh
    histogram, bins = np.histogram(image_array, bins=nbr_bins, range=(0, 256), density=True)
    
    # Tính toán hàm phân phối tích lũy (CDF - Cumulative Distribution Function)
    cdf = histogram.cumsum()
    cdf = 255 * cdf / cdf[-1]
    
    # Lấy giá trị mới cho từng pixel dựa trên CDF
    image_equalized = np.interp(image_array, bins[:-1], cdf)
    
    # Chuyển đổi mảng kết quả thành hình ảnh
    equalized_image = Image.fromarray(image_equalized.astype('uint8'))
    
    return equalized_image

# Đường dẫn thư mục chứa ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Nối đường dẫn tới chính xác file ảnh cụ thể 
image_path = os.path.join(my_dir, 'anh 1.jpg')

# Đọc ảnh
im = Image.open(image_path)

# Chuyển qua ảnh xám 1 lần rồi dùng luôn cho tiện
im_gray = im.convert('L')

# Áp dụng cân bằng lược đồ ảnh xám 
equalized_image = histogram_equalization(im_gray)

# Tạo 1 lưới 2x2 để hiển thị hình ảnh và biểu đồ
plt.figure(figsize = (15, 10))

# 1. Hiển thị hình ảnh gốc 
plt.subplot(2, 2, 1)
plt.imshow(im_gray, cmap = 'gray')
plt.title('Hình ảnh gốc (Chưa cân bằng)')

# 2. Vẽ biểu đồ Histogram của ảnh gốc
plt.subplot(2, 2, 2)
plt.hist(np.array(im_gray).flatten(), bins=128, range=(0, 256), color='gray')
plt.title('Biểu đồ Histogram - Hình ảnh gốc')

# 3. Hiển thị hình ảnh đã cân bằng 
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap = 'gray')
plt.title('Hình ảnh đã cân bằng (Equalized)')

# 4. Vẽ biểu đồ Histogram của ảnh đã cân bằng 
plt.subplot(2, 2, 4)
plt.hist(np.array(equalized_image).flatten(), bins=128, range=(0, 256), color='gray')
plt.title('Biểu đồ Histogram - Đã cân bằng')

# Hiển thị toàn bộ cửa sổ
plt.show()