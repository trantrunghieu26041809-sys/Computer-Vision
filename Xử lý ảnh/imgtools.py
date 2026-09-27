import os
from PIL import Image

def load_image(image_path):
    """
    Đọc ảnh từ đường dẫn cho trước và trả về đối tượng ảnh
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print("Lỗi khi đọc hình ảnh từ:", image_path, " - ", e)
        return None

def get_image_list(folder_path):
    """
    Đọc tất cả ảnh trong thư mục được chỉ định
    """
    image_list = []
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    
    # Kiểm tra xem thư mục có thực sự tồn tại không 
    if not os.path.exists(folder_path):
        print("Thư mục không tồn tại:", folder_path)
        return image_list

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(valid_extensions):
            full_path = os.path.join(folder_path, file_name)
            img = load_image(full_path)
            if img is not None:
                image_list.append(img)
                
    return image_list