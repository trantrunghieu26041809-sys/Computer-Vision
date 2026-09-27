# Bài 20: Xử lý ảnh hình thái và đếm số lượng đối tượng 

from scipy import ndimage 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os


# Thư mục chứa hình ảnh
dir_path = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

# Đường dẫn đến hình ảnh
image_path = os.path.join(dir_path, 'anh 1.jpg')
print("Đường dẫn file gốc:", image_path)

# Sử dụng Image.open() đọc ảnh
im = Image.open(image_path)

# Chuyển sang ảnh xám và đưa về mảng numpy
gray_image = im.convert('L')
image_a = np.array(gray_image)

# Chuyển sang ảnh nhị phân 
# Điểm nào < 200 sẽ là True (1), lớn hơn hoặc bằng 200 sẽ là False (0)
binary_image = 1 * (image_a < 200)

# Thực hiện opening để loại bỏ nhiễu và nối các đối tượng 
opened_image = ndimage.binary_opening(binary_image, structure=np.ones((9, 5)))

# Đánh nhãn 
labeled_image, num_features =  ndimage.label(binary_image) # Sẽ biết được trong ảnh có bao nhiêu vật thể 

# Tạo lưới subplot với 3 dòng và 1 cột 
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# Show ảnh 
plt.subplot(4, 1, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Ảnh xám")

plt.subplot(4, 1, 2)
plt.imshow(binary_image, cmap='gray')
plt.title("Ảnh nhị phân")

plt.subplot(4, 1, 3)
plt.imshow(binary_image, cmap='gray')
plt.title("Ảnh sau khi opening")

plt.subplot(4, 1, 4)
plt.imshow(labeled_image, cmap='gray')
plt.title(f"Ảnh đã đánh nhãn ({num_features} đối tượng)")

plt.show()