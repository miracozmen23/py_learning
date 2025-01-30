import pandas as pd
import yfinance as yf

# USD/TRY 10 yıllık veriyi çek
data = yf.download("USDTRY=X", start="2014-01-01", end="2024-01-01")

# Gerekli sütunları seç ve temizle
data = data[['Close']].dropna()
data['Return'] = data['Close'].pct_change().fillna(0)

# Dosyayı CSV olarak kaydet
file_path = "USDTRY_10y_data.csv"
data.to_csv(file_path, index=True)
print(f"Veri dosyası kaydedildi: {file_path}")
