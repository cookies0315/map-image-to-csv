# map-image-to-csv

這個專案包含一個 Python 程式，用於將地圖圖像轉換為 CSV 表格。程式會偵測紅色與藍色點，並根據規則將其轉換為特定符號：

- 紅色點交替標示為 `S` 和 `E`。
- 藍色點依數列序編號 。

其他區域則以 `.` 表示白色空白，`#` 表示線條或非白色區域。

## 使用方法

1. 安裝依賴：
   ```bash
   pip install opencv-python numpy
   ```
2. 將欲轉換的圖像放在同一目錄，並修改 `mean_picture_to_csv.py` 中的 `img_path`。
3. 執行程式：
   ```bash
   python mean_picture_to_csv.py
   ```
4. 生成的 `floor_plan_ascii.csv` 將會儲存在同一目錄。

## 授權
請根據需要自行加入授權資訊。

