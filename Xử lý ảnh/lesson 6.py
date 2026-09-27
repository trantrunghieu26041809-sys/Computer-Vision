# Bài 6: Cách chuyển đổi ảnh màu và ảnh xám 

import os
from PIL import Image
from imgtools import load_image

# Đường dẫn thư mục chứa ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Nối đường dẫn tới chính xác file ảnh cụ thể 
image_path = os.path.join(my_dir, 'anh 1.jpg')

# Đọc ảnh an toàn qua hàm load_image
img = load_image(image_path)

# Show ảnh gốc
img.show()

# Chuyển từ ảnh RGB sang ảnh xám
gray_image = img.convert("L")

# Show ảnh xám 
gray_image.show()

# Phân RGB thành 3 tầng màu khác nhau 
red_band, green_band, blue_band = img.split()

# Show 3 tầng màu
red_band.show()
green_band.show()
blue_band.show()

# Cách để trộn ảnh 
merged_image =  Image.merge("RGB", (red_band, green_band, blue_band))

# Show ảnh đã trộn 
merged_image.show()
