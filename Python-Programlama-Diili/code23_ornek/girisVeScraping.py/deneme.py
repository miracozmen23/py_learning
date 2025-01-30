import yfinance as yf
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Varlık verilerini yfinance'dan yükleme (Bitcoin)
asset_data = yf.download('BTC-USD', start='2023-01-01', end='2023-12-31')

# Kapanış fiyatlarını al
close_prices = asset_data['Close']

# Z-skor dönüşümü uygulama
z_scores = stats.zscore(close_prices)

# Dağılım grafiği (Histogram) çizdirme
plt.figure(figsize=(12, 6))
plt.hist(z_scores, bins=30, color='skyblue', edgecolor='black')
plt.title('Z-Skor Dönüşümü Sonrası Bitcoin Kapanış Fiyatlarının Dağılımı')
plt.xlabel('Z-Skor')
plt.ylabel('Frekans')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Çarpıklık hesaplama ve gösterme
skewness = stats.skew(z_scores)

# Eğer skewness bir dizi ise, ilk elemanı alalım
if isinstance(skewness, np.ndarray):
    skewness = skewness[0]

# Ortalama değerini alırken tek bir sayıya dönüştür
z_scores_mean = np.mean(z_scores)

# Ortalama üzerinde bir çizgi çizdir ve çarpıklık değeri ile etiketle
plt.axvline(z_scores_mean, color='red', linestyle='dashed', linewidth=1.5, label='Çarpıklık: {:.2f}'.format(skewness))
plt.legend()
plt.show()

# Çarpıklık hakkında yorum
if skewness > 0:
    print("Pozitif çarpıklık: Dağılım sağa doğru uzun bir kuyruk gösteriyor.")
elif skewness < 0:
    print("Negatif çarpıklık: Dağılım sola doğru uzun bir kuyruk gösteriyor.")
else:
    print("Simetrik dağılım: Dağılım neredeyse simetrik.")
