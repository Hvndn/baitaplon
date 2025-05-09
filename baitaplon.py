from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import datetime
import schedule

def lay_dulieu():
    print(f"Bắt đầu lúc: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

   
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 15)

    data = []
    page = 1
    while True:
        url = f"https://vieclamdanang.vn/tim-kiem/viec-lam-ban-hang-tai-hai-chau?page={page}&cat=13&dis=1&order=1"
        print(f"Đang thu thập trang {page}: {url}")
        driver.get(url)
        time.sleep(3)

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".box-job-horizontal")))
        except:
            print("Không còn dữ liệu. Dừng lại.")
            break

        listings = driver.find_elements(By.CSS_SELECTOR, ".box-job-horizontal")
        if not listings:
            break

        for listing in listings:
            try:
                title = listing.find_element(By.CSS_SELECTOR, ".job-name a").text.strip()
                company = listing.find_element(By.CSS_SELECTOR, ".job-company").text.strip()

                try:
                    salary = listing.find_element(By.CSS_SELECTOR, "._salary span").text.strip()
                except:
                    salary = ""

                try:
                    job_type = listing.find_element(By.CSS_SELECTOR, ".job-type").text.strip()
                except:
                    job_type = ""

                try:
                    date_posted = listing.find_element(By.CSS_SELECTOR, "._date span").text.strip()
                except:
                    date_posted = ""

                try:
                    deadline = listing.find_element(By.CSS_SELECTOR, "._exp span[style='color:#dd263c']").text.strip()
                except:
                    deadline = ""

                data.append([title, company, salary, job_type, date_posted, deadline])
            except Exception as e:
                print(f"Lỗi khi lấy dữ liệu tin tuyển dụng: {e}")
                continue

        page += 1

    driver.quit()

    df = pd.DataFrame(data, columns=["Tiêu đề", "Công ty", "Mức lương", "Loại hình", "Ngày đăng", "Hạn nộp hồ sơ"])
    today = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    filename = f"vieclamdanang_{today}.csv"
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Đã lưu dữ liệu vào file: {filename}")


schedule.every().day.at("6:00").do(lay_dulieu)




print("Đang chờ đến thời gian được đặt để chạy...")
while True:
    schedule.run_pending()
    time.sleep(60)  # Kiểm tra mỗi phút