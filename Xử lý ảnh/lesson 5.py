# Bài 5: Cách xoay ảnh 

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
    # Xoay ảnh 45 độ ngược chiều kim đồng hồ 
    rotated_image = img.rotate(90)
    
    # Hiển thị ảnh đã xoay
    rotated_image.show()
    
    # Transpose ảnh
    transposed_image = img.transpose(Image.Transpose.ROTATE_90)

    # Hiển thị ảnh 
    transposed_image.show()
else:
    print("Không thể đọc được ảnh, vui lòng kiểm tra lại đường dẫn")
    

    