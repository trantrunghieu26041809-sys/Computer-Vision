# Bài 12: Giới thiệu thư viện Numpy và các phép tính trên mảng 

import numpy as np

# Tạo mảng 
a=np.array([1, 2, 3])

# In mảng
print(a)

# In ra 1 phần tử bất kì 
element=a[1]
print(element)

# Cách tạo mảng toàn là số 0
a=np.zeros(5)
print(a)

# Cách tạo mảng toàn là số 1 
b=np.ones(5)
print(b)

# Tạo mảng từ 0 đến 100
d=np.arange(101)
print(d)

# Tạo mảng gồm các phần tử với khoảng cách đều nhau 
e=np.linspace(0, 10, num=5)
print(e)

# Xác định kiểu dữ liệu 
f=np.ones(5, dtype=np.int64)
print(f)

# Thêm, xóa và sắp xếp mảng
arr=np.array([3, 1, 2, 4, 5])

# Sắp xếp 
arr=np.sort(arr)
print(arr)

# Sắp xếp ngược
arr=np.sort(arr)[::-1]
print(arr)

# Cách thêm phần tử vào mảng 
arr=np.append(arr, 100)
print(arr)

# Xóa đi 1 vị trí trong mảng 
arr=np.delete(arr, 3)
print(arr)

# Cách sắp xếp mảng 2 chiều 
# Tạo mảng 2 chiều (ma trận)
matrix=np.array([[1, 5, 3], [8, 2, 6], [7, 9, 4]])

# Sắp xếp theo hàng (từ trái sang phải)
sap_xep_theo_hang=np.sort(matrix, axis=1)
print("Sắp xếp theo hàng:\n", sap_xep_theo_hang)

# Sắp xếp theo cột (từ trên xuống dưới)
sap_xep_theo_cot=np.sort(matrix, axis=0)
print("Sắp xếp theo cột:\n", sap_xep_theo_cot)

# Tạo mảng 2 chiều 
arr=np.array([[1, 2, 3], [4, 5, 6]])

# Sử dụng các thuộc tính để lấy thông tin mảng
so_chieu=arr.ndim # Số chiều (2 chiều)
kich_thuoc=arr.size # Kích thước (tổng số phần tử, 6)
hinh_dang=arr.shape # Hinh dang (số hàng * số cột, (2, 3))

print("Số chiều: ", so_chieu)
print("Kích thước: ", kich_thuoc)
print("Hình dáng: ", hinh_dang)

# Chuyển đổi kiểu dữ liệu 
arr=np.array([1, 2, 3, 4, 5, 6])
arr_float=arr.astype(float)
print(arr_float)

# Thay đổi hình dạng của mảng 
arr=np.array([1, 2, 3, 4, 5, 6])
# Đổi ma trận thành 2 hàng và 3 cột
reshaped_arr=arr.reshape(2, 3)
print(reshaped_arr)

# Cắt lát mảng 
arr=np.array([1, 2, 3, 4, 5])
sub_arr=arr[1:4]
print(sub_arr)

sub_arr=arr[::-1]
print(sub_arr)

sub_arr=arr[-2:]
print(sub_arr)

# Cách chuyển thành ma trận chuyển vị 
arr=np.array([[1, 2, 3], [4, 5, 6]])
# Để chuyển vị mảng 
transposed_arr=arr.T
print(transposed_arr)

# Cách gộp nhiều mảng 
arr1=np.array([1, 2, 3])
arr2=np.array([4, 5, 6])
arr=np.concatenate((arr1, arr2))
print(arr)

