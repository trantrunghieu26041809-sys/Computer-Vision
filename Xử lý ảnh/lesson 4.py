# Bài 4: Sao chép và cắt dán vùng ảnh 

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
    # 1. Định vị khu vực cắt: (left, upper, right, lower)
    region = (100, 100, 250, 250)

    # 2. Cắt vùng ảnh 
    cropped_image = img.crop(region)
    print("Kích thước vùng cắt:", cropped_image.size)

    # 3. Dán vùng ảnh đã cắt vào vị trí khác trên ảnh gốc
    paste_position = (250, 250)
    img.paste(cropped_image, paste_position)

    # 4. Hiển thị ảnh gốc sau khi đã dán 
    img.show()
else:
    print("Không thể đọc được ảnh, vui lòng kiểm tra lại đường dẫn.")