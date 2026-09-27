# Bài 9: Lược đồ ảnh xám (Lược đồ Histogram)

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Đường dẫn thư mục chứa ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Nối đường dẫn tới chính xác file ảnh cụ thể 
image_path = os.path.join(my_dir, 'anh 1.jpg')

# Đọc ảnh và hiển thị 
im = Image.open(image_path)

# Chuyển sang ảnh xám 
im_gray = im.convert('L')

# Show ảnh xám 
im_gray.show()

# Biến ảnh thành mảng 
im_array = np.array(im_gray)

# Show mảng 
print(im_array)

# Tạo hình vẽ mới 
plt.figure()
plt.hist(im_array.flatten(), bins = 128)
plt.title('Biểu đồ Histogram của ảnh')
plt.xlabel('Giá trị của pixel')
plt.ylabel('Số lượng')
plt.show()