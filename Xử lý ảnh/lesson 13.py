# Bài 13: Lấy thông tin cơ bản của ảnh bằng thư viện numpy

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

# Chuyển hình ảnh về array
im_array = np.array(im)

# Kiểm tra kích thước của ảnh 
print(im_array.shape)

# Chuyển đổi sang ảnh xám 
im_array_2 = np.array(im.convert('L'))
print(im_array_2.shape)