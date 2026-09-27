# Bài 17: Giới thiệu về thư viện Scipy
# Giải hệ phương trình tuyến tính 

from scipy import integrate
from scipy import linalg
import numpy  as np

# Định nghĩa hệ phương trình tuyến tính 
A = np.array([[2, 1], [3, 2]])
B = np.array([5, 7])

# Giải hệ phương trình tuyến tính 
x = linalg.solve(A, B)

# In kết quả 
print("Kết quả: ", x)

# Tính tích phân của 1 hàm số 
# Định nghĩa hàm f(x)=x^2
def my_function(x):
    return x**2

# Tính tích phân của f(x) từ 0 đến 1
integral = integrate.quad(my_function, 0, 1)
print("Tích phân từ 0 đến 1 là: ", integral)

# Tính giá trị riêng và vector riêng của ma trận 
A = np.array([[2, 1], [3, 2]])
evals, evecs = linalg.eig(A)
print("Giá trị riêng: ", evals)
print("Vector riêng: ", evecs)