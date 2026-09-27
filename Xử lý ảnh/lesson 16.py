# Bài 16: Tạo ảnh mới bằng cách tính trung bình từ nhiều ảnh 

import numpy as np
from PIL import Image
import glob
import os

def average_images(image_list):
    # Đọc ảnh đầu tiên để tạo mảng cơ sở 
    total_array = np.array(Image.open(image_list[0]), 'f')
    count = 1
    
    # Duyệt qua các ảnh còn lại trong danh sách 
    for image_path in image_list[1:]:
        try:
            image_array = np.array(Image.open(image_path), 'f')
            total_array += image_array
            count = count + 1
        except Exception as e:
            print(f"Skip {image_path} - Lỗi: {e}")
            
    # Tính trung bình
    average_array = total_array / count
    
    # Chuyển đổi kết quả trung bình thành định dạng ảnh 
    average_image = Image.fromarray(average_array.astype('uint8'))
    
    return average_image

# ==========================================
# PHẦN XỬ LÝ ĐƯỜNG DẪN VÀ CHẠY HÀM
# ==========================================

folder_path = r'E:\Computer vision\computer vision\Xử lý ảnh\Thư viện ảnh'

image_list = glob.glob(os.path.join(folder_path, '*.[jJ][pP][gG]')) + \
             glob.glob(os.path.join(folder_path, '*.[pP][nN][gG]'))

# Kiểm tra và thực thi
if len(image_list) > 0:
    print(f"Tìm thấy {len(image_list)} ảnh. Đang xử lý...")
    
    # Gọi hàm tính trung bình
    result_image = average_images(image_list)
    
    # Hiển thị ảnh kết quả lên màn hình
    result_image.show()
    
    save_path = os.path.join(folder_path, 'ket_qua_trung_binh.jpg')
    result_image.save(save_path)
    print(f"Đã lưu ảnh kết quả tại: {save_path}")
    
else:
    print("Không tìm thấy file ảnh nào!")