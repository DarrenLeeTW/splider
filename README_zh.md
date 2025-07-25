# 台灣證券交易所資料抓取工具

## 概述
此專案用於抓取台灣證券交易所（TWSE）每日的股價與本益比等資訊，並將結果存入本地 SQLite 資料庫，以便後續分析使用。

## 功能特色
- 根據指定日期取得股價與本益比資料
- 將取得的資料以結構化方式存入資料庫
- 可與其他金融分析工具整合

## 環境需求
- Python 3.x
- requests 套件
- SQLite3

## 安裝與使用
1. 下載此專案：
   ```bash
   git clone https://github.com/DarrenLeeTW/splider.git
   ```
2. 安裝相依套件並輸入日期執行：
   ```bash
   pip install -r requirements.txt
   python get_pe_ratio.py --date YYYYMMDD
   ```

以上指令會下載指定日期的 TWSE 資料並寫入 `twse_data.db` 檔案。

