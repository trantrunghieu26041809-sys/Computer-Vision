# Bài 3: Cách thay đổi kích thước ảnh 

import os
from PIL import Image
from imgtools import load_image

# Đường dẫn thư mục chứa ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Nối đường dẫn tới chính xác file ảnh cụ thể 
image_path = os.path.join(my_dir, 'anh 1.jpg')

# Đọc ảnh an toàn qua hàm load_image
img = load_image(image_path)

if img is not None:
    # Kích thước ban đầu
    print("Kích thước ban đầu:", img.size)
    
    # Đặt kích thước tối đa mà mình mong muốn
    max_size = (300, 300)
    
    # Thu nhỏ ảnh 
    img.thumbnail(max_size)
    
    # In kích thước thực tế sau khi tính toán theo tỷ lệ gốc
    print("Kích thước sau khi thumbnail:", img.size)
    
    # Hiển thị ảnh thu nhỏ 
    img.show()
