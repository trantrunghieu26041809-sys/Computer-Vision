# Bài 8: Vẽ các loại biểu đồ bằng Matplotlib

import matplotlib.pyplot as plt

# Dữ liệu
x = [1, 2, 3, 4, 5]
y = [10, 16, 20, 30, 25]

x1 = [1, 2, 3, 4, 5]
y2 = [20, 15, 8, 9, 20]

# Vẽ 2 đường với màu và nhãn khác nhau 
plt.plot(x, y, 'bo-', label = 'Tập dữ liệu 1')
plt.plot(x1, y2, 'ro--', label = 'Tập dữ liệu 2')

# Đặt tiêu đề và tên trục tọa độ
plt.title('Biểu đồ so sánh dữ liệu')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')

# Hiển thị chú thích (legend) và hiển thị biểu đồ
plt.legend()
plt.grid(True)  # Bật lưới để dễ nhìn tọa độ
plt.show()

# Vẽ biểu đồ cột 
categories = ['A', 'B', 'C', 'D', 'E']
values = [15, 10, 25, 12, 18]

plt.bar(categories, values, color = 'g', alpha = 0.6)
plt.title('Biểu đồ so sánh dữ liệu')
plt.xlabel('Danh mục')
plt.ylabel('Giá trị')

plt.legend()
plt.grid(True)  # Bắt lưới để dễ nhìn tọa độ 
plt.show()

# Vẽ biểu đồ hình tròn
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['red', 'green', 'blue', 'yellow']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90) # Có hiển thị số trên biểu đồ 
plt.title('Biểu đồ hình tròn')
plt.show()

# Vẽ biểu đồ phân tán 
x = [1, 2, 3, 4, 5]
y = [10, 16, 20, 30, 25]

plt.scatter(x, y, c = 'r', marker = 'o', label = 'Dữ liệu')
plt.title('Biểu đồ phân tán') # Đặt tiêu đề cho biểu đồ
plt.xlabel('Trục x') # Đặt nhãn cho trục x 
plt.ylabel('Trục y') # Đặt nhãn cho trục y
plt.legend()
plt.show() # Hiển thị biểu đồ 

# Vẽ biểu đồ hộp
data = [15, 18, 22, 30, 35, 45, 50, 55, 65]

plt.boxplot(data)  # Vẽ biểu đồ hộp
plt.title('Biểu đồ hộp')  # Đặt tiêu đề cho biểu đồ
plt.ylabel('Giá trị')  # Đặt nhãn cho trục y
plt.show()  # Hiển thị biểu đồ 

# Vẽ biểu đồ violin
# Tạo dữ liệu: Điểm thi của 3 lớp khác nhau
lop_A = [5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10]
lop_B = [2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8]
lop_C = [6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10]

# Gom dữ liệu vào một list chung
data = [lop_A, lop_B, lop_C]

# Vẽ biểu đồ violin
# Tham số showmeans=True để hiển thị đường trung bình (mean)
plt.violinplot(data, showmeans=True)

# Trang trí biểu đồ 
plt.title('Biểu đồ Violin: Phân bố điểm thi 3 lớp')
plt.xlabel('Lớp học')
plt.ylabel('Điểm thi')

# Thay đổi nhãn của trục X từ số (1, 2, 3) thành tên các lớp
plt.xticks([1, 2, 3], ['Lớp A', 'Lớp B', 'Lớp C'])

# Thêm lưới để dễ nhìn 
plt.grid(True, axis='y', linestyle='--', alpha=0.6)

# Hiển thị biểu đồ 
plt.show()

# Đám mây từ khóa 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Python is an amazing language for data visualization and word clouds."

wordcloud = WordCloud(width=800, height=400).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Biểu đồ đám mây từ văn bản ví dụ')
plt.show()