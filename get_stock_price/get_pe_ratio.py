import sqlite3
import requests
import csv
from io import StringIO
from datetime import datetime

date = datetime.now().strftime("%Y%m%d")
url = f"https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date={date}&select"
response = requests.get(url)
if response.status_code != 200:
    print("無法獲取數據，響應代碼：", response.status_code)
    exit()
f = StringIO(response.text)
reader = csv.reader(f, delimiter=',')

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
''')

# 跳過前兩行（標題和欄位名）
next(reader)
next(reader)

for row in reader:
    if len(row) >= 7:
        cursor.execute('''
            INSERT OR REPLACE INTO stocks 
            (id, name, dividend_yield, dividend_year, pe_ratio, pb_ratio, financial_statement) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
conn.commit()
conn.close()
