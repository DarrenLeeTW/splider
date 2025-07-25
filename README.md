# Taiwan Stock Exchange Data Fetcher

For the Chinese version of this document, please refer to [README_zh.md](README_zh.md).

## Overview
This project is designed to retrieve daily stock prices and price-to-earnings (P/E) ratios from the Taiwan Stock Exchange (TWSE) based on a specified date. The data fetched is then stored in a database for further analysis and reference.

## Features
- Fetch stock prices and P/E ratios for a specified date.
- Store the retrieved data in a structured database.
- Easy to use and integrate into other financial analysis tools.

## Requirements
- Python 3.x
- Requests library
- SQLite3

## Installation
To set up this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/DarrenLeeTW/splider.git
   ```

2. Install the required dependencies, and input data
   ```bash
   pip install -r requirements.txt
   python get_pe_ratio.py --date YYYYMMDD
   ```

