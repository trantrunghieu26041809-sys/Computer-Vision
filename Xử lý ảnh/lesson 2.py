# Bài 2: Cách đọc nhiều file ảnh trong thư mục 

from PIL import Image
from imgtools import get_image_list

# Thư mục chứa hình ảnh 
my_dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Gọi hàm đọc nhiều ảnh 
imgs = get_image_list(my_dir)
print("Số lượng ảnh tìm thấy:", len(imgs))

# Hiển thị và in thông tin từng ảnh 
for img in imgs:
    print("Kích thước ảnh:", img.size)
    img.show()