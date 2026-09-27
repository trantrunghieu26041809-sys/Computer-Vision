# Bài 11: Tương tác với ảnh bằng Matplotlib

import os
import matplotlib.pyplot as plt
from PIL import Image

# Đường dẫn thư mục chứa ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'
image_path = os.path.join(my_dir, 'anh 1.jpg')

# Đọc ảnh
im = Image.open(image_path)

# Chuyển đổi backend sang tkagg để mở cửa sổ tương tác
plt.switch_backend('tkagg')

# Hiển thị ảnh
plt.imshow(im)
plt.title('Sử dụng công cụ Pan để di chuyển ảnh')

# Sử dụng hàm ginput để chọn điểm trên ảnh 
points = plt.ginput(5)

# In điểm ra 
print(points)

plt.show()

# Vẽ lại các điểm đã chọn bằng dấu * đỏ 
plt.close()

# Vẽ lại
for point in points:
    x, y = point
    plt.plot(x, y, 'r*', markersize=10)
    
# Hiển thị ảnh đã được đánh dấu (lúc này bạn sẽ thấy các ngôi sao đỏ trên ảnh)
plt.show()