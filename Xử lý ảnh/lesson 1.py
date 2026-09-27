# Bài 1: Cách đọc và lưu ảnh 

# Import lớp Image
from PIL import Image

# Thư mục chứa hình ảnh
dir = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Đường dẫn đến hình ảnh 
image_path = dir + r'\anh 1.jpg'
print("Đường dẫn file gốc:", image_path)

# Sử dụng Image.open() để đọc ảnh 
img1 = Image.open(image_path)

# In thông tin của ảnh 
print("Định dạng ảnh: ", img1.format)
print("Kích thước ảnh: ", img1.size)
print("Hệ màu (mode): ", img1.mode)

# Lưu ảnh để chuyển đổi định dạng
new_img1_path = dir + r'\new_1.jpg'
new_img1_png_path = dir + r'\new_1.png'

img1.save(new_img1_path)
img1.save(new_img1_png_path)
print("Đã lưu và chuyển đổi định dạng thành công!")

# Hiển thị ảnh sau khi đã xử lý xong 
img1.show()

# Đóng tập tin
img1.close()