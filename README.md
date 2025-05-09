#   Công Cụ Tự Động Thu Thập Thông Tin Việc Làm

Công cụ tự động để thu thập thông tin việc làm từ trang web vieclamdanang.vn và lưu vào file CSV với khả năng lên lịch chạy.

## ✨ Tính năng

- Thu thập chi tiết công việc (tiêu đề, công ty, mức lương, loại hình công việc, ngày đăng, hạn nộp hồ sơ)
- Chạy tự động vào lúc 6:00 sáng hàng ngày
- Xuất dữ liệu vào file CSV hoặc Excel (hiện tại chỉ hỗ trợ CSV)

## 🛠 Cài đặt

### ⚙️ Điều kiện tiên quyết

- Python 3.8+
- Google Chrome đã được cài đặt
- Kết nối internet ổn định

### 🪜 Các bước cài đặt

##### 1.  **Clone repository**

   ```bash
   git clone [https://github.com/yourusername/vieclamdanang-scraper.git](https://github.com/yourusername/vieclamdanang-scraper.git)
   cd vieclamdanang-scraper

   ```
##### 2. **Tạo và kích hoạt môi trường ảo**
```Bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
##### 3. **Cài đặt các thư viện phụ thuộc**
```Bash
pip install -r requirements.txt
```
##### 4. **Chạy Chương Trình**
  Chạy thủ công 
```Bash
python main.py
```
 Chạy theo lịch trình:
Script được cấu hình để chạy tự động vào lúc 6:00 sáng hàng ngày. Để thay đổi lịch trình, hãy chỉnh sửa file main.py:
```
import schedule
import time

def lay_dulieu():
    # Mã thu thập dữ liệu của bạn ở đây
    print("Đang thu thập dữ liệu...")

schedule.every().day.at("06:00").do(lay_dulieu)

while True:
    schedule.run_pending()
    time.sleep(1)
```
 File đầu ra
Dữ liệu đã thu thập sẽ được lưu ở định dạng CSV với dấu thời gian:
```
vieclamdanang_YYYY-MM-DD_HH-MM-SS.csv
```
Các cột mẫu:
```
Tiêu đề (Job Title)
Công ty (Company)
Mức lương (Salary)
Loại hình (Job Type)
Ngày đăng (Posting Date)
Hạn nộp hồ sơ (Application Deadline
```
