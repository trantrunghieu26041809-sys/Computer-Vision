# Bài 7: Giới thiệu thư viện Matplotlib

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image

# Đường dẫn thư mục chứa ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Nối đuòng dẫn tới chính xác file ảnh cụ thể 
image_path = os.path.join(my_dir, 'anh 1.jpg')

# Đọc ảnh và hiển thị 
im = Image.open(image_path)

# Show ảnh bằng Matplotlib
plt.imshow(im)
plt.axis('on') # Bật hệ tọa độ Pixel
plt.show()

# Vẽ đồ thị cơ bản  
x = [1, 2, 3, 4, 5]
y = [10, 16, 20, 30, 25]

plt.plot(x, y, color = 'red')
plt.title('Ví dụ vẽ biểu đồ')
plt.axis('on')
plt.show()

# Vẽ trên hình ảnh 
# Đọc ảnh và hiển thị 
im = Image.open(image_path)
x = [100, 100, 400, 400]
y = [200, 300, 200, 300]
plt.imshow(im) # Hiển thị hình ảnh  
plt.plot(x, y, 'bo--') # Đánh dấu các điểm 

# Show ảnh sau khi vẽ lên 
plt.show()


