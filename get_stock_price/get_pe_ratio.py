import sqlite3  # 用於存取 SQLite 資料庫
import requests  # 發送 HTTP 請求
import csv
from io import StringIO
from datetime import datetime

# 取得今天日期並格式化為 YYYYMMDD
date = datetime.now().strftime("%Y%m%d")

# 組合查詢 TWSE 本益比資料的網址
url = f"https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={date}&select"

# 送出 GET 請求取得資料
response = requests.get(url)
if response.status_code != 200:
    # 若取得失敗印出錯誤代碼並結束
    print("無法獲取數據，響應代碼：", response.status_code)
    exit()

# 將 CSV 文字轉為檔案物件並建立讀取器
f = StringIO(response.text)
reader = csv.reader(f, delimiter=',')

# 連線到本地資料庫並取得游標
conn = sqlite3.connect('twse_data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS stocks (
        id TEXT PRIMARY KEY,
        name TEXT,
        dividend_yield REAL,
        dividend_year INTEGER,
        pe_ratio REAL,
        pb_ratio REAL,
        financial_statement TEXT
    )
''')  # 建立 stocks 資料表（若不存在）

# 跳過前兩行（標題和欄位名稱）
next(reader)
next(reader)

# 逐行讀取 CSV，並將資料寫入資料庫
for row in reader:
    if len(row) >= 7:
        cursor.execute('''
            INSERT OR REPLACE INTO stocks
            (id, name, dividend_yield, dividend_year, pe_ratio, pb_ratio, financial_statement)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
# 將變更寫入並關閉連線
conn.commit()
conn.close()
