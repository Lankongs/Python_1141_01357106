import pandas as pd
import numpy as np
import sys

df = pd.read_csv("aqx_p_488.csv")

aqi = df["aqi"]
pm25 = df["pm2.5_conc"]

def round1(x):
    return round(x, 1)

while True:
    try:
        cmd = input("請輸入功能(1-4):").strip()
    except EOFError:
        break

    if not cmd.isdigit():
        print("Error")
        continue

    cmd = int(cmd)
    if cmd < 1 or cmd > 4:
        print("Error")
        continue

    #AQI統計
    if cmd == 1:
        avg = round1(aqi.mean())
        mx = round1(aqi.max())
        mn = round1(aqi.min())
        std = round1(aqi.std())
        print(f"平均AQI: {avg}, 最高AQI: {mx}, 最低AQI: {mn}, AQI標準差: {std}")

    #2.5統計
    elif cmd == 2:
        avg = round1(pm25.mean())
        mx = round1(pm25.max())
        mn = round1(pm25.min())
        std = round1(pm25.std())
        print(f"平均PM2.5: {avg}, 最高PM2.5: {mx}, 最低PM2.5: {mn}, PM2.5標準差: {std}")

    #縣市平均AQI排名
    elif cmd == 3:
        county_avg = df.groupby("county")["aqi"].mean().round(1)
        county_avg = county_avg.sort_values(ascending=False)

        for c, v in county_avg.items():
            print(f"{c}: {v}")

    # 找出每個縣市 AQI 最高的一筆資料
    elif cmd == 4:
        df_sorted = df.sort_values(by="aqi", ascending=False)
        top = df_sorted.groupby("county").head(1)

        for _, row in top.iterrows():
            county = row["county"]
            site = row["sitename"]
            aqi_v = round1(row["aqi"])
            time = row["datacreationdate"]
            print(county, site, aqi_v, time)
