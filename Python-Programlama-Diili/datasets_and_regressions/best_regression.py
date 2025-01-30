import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import yfinance as yf

# 10 yıllık USD/TRY verisini indir
data = yf.download("USDTRY=X", start="2014-01-01", end="2024-01-01")
data = data[['Close']].dropna()  # Kapanış fiyatlarını al ve eksik değerleri temizle
data['Return'] = data['Close'].pct_change().fillna(0)  # Günlük yüzdesel değişim

# Regresyon modeli için özellik ve hedef değişkenleri oluştur
X = np.arange(len(data)).reshape(-1, 1)  # Zaman indeksini özellik olarak kullan
y = data['Close'].values  # Hedef değişken: kapanış fiyatı

# Eğitim ve test veri setini ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Farklı regresyon algoritmalarını tanımla
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.01),
    "Decision Tree": DecisionTreeRegressor(max_depth=5),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Support Vector Regressor": SVR(kernel='rbf', C=1.0, epsilon=0.1)
}

# Modelleri eğit, MSE ve R² hesapla
results = {}
r2_scores = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    results[name] = mse
    r2_scores[name] = r2

# Sonuçları yazdır
print("Model Performansları:")
for name in models.keys():
    print(f"{name}: MSE = {results[name]:.4f}, R² = {r2_scores[name]:.4f}")

# Grafik çizimi: MSE ve R²'nin kıyaslanması
fig, ax = plt.subplots(1, 2, figsize=(16, 8))

# MSE Bar Chart
ax[0].barh(list(results.keys()), list(results.values()), color='skyblue')
ax[0].set_title("MSE Kıyaslaması", fontsize=16)
ax[0].set_xlabel("MSE Değeri", fontsize=12)

# R² Bar Chart
ax[1].barh(list(r2_scores.keys()), list(r2_scores.values()), color='lightgreen')
ax[1].set_title("R² Kıyaslaması", fontsize=16)
ax[1].set_xlabel("R² Değeri", fontsize=12)

plt.tight_layout()
plt.show()
