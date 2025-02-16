import praw
import csv
import os 
import json

import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
keywords = ["electric vehicle", "tesla", "ev charging"]

pytrends.build_payload(kw_list=keywords, timeframe="today 12-m")
df = pytrends.interest_over_time()

if 'isPartial' in df.columns:
    df = df.drop(columns=['isPartial'])
    
raw_data_dir = "datasets/raw"
os.makedirs(raw_data_dir, exist_ok=True)

csv_path = os.path.join(raw_data_dir, "google_trends_data.csv")
df.to_csv(csv_path, encoding="utf-8")
print("Data saved to google_trends_data.csv")

# json_data = df.reset_index().to_dict(orient="records")
json_data = df.reset_index()
json_data['date'] = json_data['date'].astype(str)  # Convert Timestamp to string
json_data = json_data.to_dict(orient="records")

def save_to_json(data, filename):
    filepath = os.path.join(raw_data_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Saved: {filepath}")

# google_trends_data = [df]
save_to_json(json_data, "pytrends.json")

# df.to_csv("google_trends_data.csv", encoding="utf-8")

# save_to_json(google_trends_data, "pytrends.json")

trends_df = pd.read_csv("datasets/raw/google_trends_data.csv")
print(trends_df.describe())