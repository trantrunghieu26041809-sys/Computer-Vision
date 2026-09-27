# Bài 23: OpenCV và đo FPS thực tế trên video

import cv2
import numpy as np
import time 

# Đọc video từ file
my_video = cv2.VideoCapture(r"e:\1790471105016_188805257701572517_4642818165762297173.mp4")

cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)

font = cv2.FONT_HERSHEY_COMPLEX
font_color = (255, 255, 255)
font_scale = 1
font_thicknes = 2

# Đặt mốc thời gian ban đầu ở ngoài vòng lặp
prev_time = 0

while True:
    ret, frame = my_video.read()
    
    if not ret:
        break
    
    # Bấm giờ hiện tại (khi một khung hình bắt đầu được xử lý)
    current_time = time.time()
    
    # Tính FPS: 1 chia cho khoảng thời gian giữa 2 vòng lặp liên tiếp
    # Cộng thêm 1e-6 (một số cực nhỏ) để phòng ngừa lỗi Toán học chia cho 0
    fps = 1 / (current_time - prev_time + 1e-6) 
    
    # Cập nhật lại mốc thời gian để làm chuẩn cho vòng lặp tiếp theo
    prev_time = current_time 
    
    # Ghi số lượng fps 
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 50), font, font_scale, font_color, font_thicknes)
    
    cv2.imshow("Video Player", frame)
    
    if cv2.waitKey(10) == ord("q"):
        break


my_video.release()
cv2.destroyAllWindows()