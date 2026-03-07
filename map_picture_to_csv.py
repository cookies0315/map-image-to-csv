import cv2
import numpy as np

# 載入圖片
img_path = 'npm2_1F.png'
img = cv2.imread(img_path)

# 偵測紅色點
red_mask = (img[:, :, 2] > 200) & (img[:, :, 0] < 100) & (img[:, :, 1] < 100)

# 偵測藍色點
blue_mask = (img[:, :, 0] > 200) & (img[:, :, 1] < 100) & (img[:, :, 2] < 100)

# 轉換為灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 設定輸出的寬度（可根據需要調整，寬度越大細節越精確）
target_width = 150
aspect_ratio = gray.shape[0] / gray.shape[1]
target_height = int(target_width * aspect_ratio)

# 縮放圖片以適應 ASCII 網格
resized = cv2.resize(gray, (target_width, target_height), interpolation=cv2.INTER_AREA)

# 縮放紅色遮罩
resized_red = cv2.resize(red_mask.astype(np.uint8), (target_width, target_height), interpolation=cv2.INTER_NEAREST)

# 縮放藍色遮罩
resized_blue = cv2.resize(blue_mask.astype(np.uint8), (target_width, target_height), interpolation=cv2.INTER_NEAREST)

# 判定符號：白色區塊(.)，黑色/彩色線條(#)
# 這裡使用 240 作為閾值，接近 255 的純白為 .，其餘為 #
ascii_matrix = np.where(resized > 240, '.', '#')

# 設定每個紅色點交替為 [S] 和 [E]
red_positions = np.where(resized_red == 1)
for i in range(len(red_positions[0])):
    row, col = red_positions[0][i], red_positions[1][i]
    if i % 2 == 0:
        ascii_matrix[row, col] = 'S'
    else:
        ascii_matrix[row, col] = 'E'

# 設定藍色點為數字序列
blue_positions = np.where(resized_blue == 1)
for i in range(len(blue_positions[0])):
    row, col = blue_positions[0][i], blue_positions[1][i]
    ascii_matrix[row, col] = str(i + 1)

# 儲存為 CSV 檔
output_path = 'floor_plan_ascii.csv'
with open(output_path, 'w', encoding='utf-8') as f:
    for row in ascii_matrix:
        f.write(','.join(row) + '\n')

print(f"成功生成 CSV 檔案：{output_path}")
