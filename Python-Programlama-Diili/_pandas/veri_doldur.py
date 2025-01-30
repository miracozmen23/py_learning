 # Bir mağazanın satış verilerini içeren bir zaman serisi veri çerçevesi oluşturun. 
 # Verilerde eksik değerler (NaN) ve hatalı veriler (örneğin negatif satış) olabilir. 
 # Verilerdeki eksik değerleri doldurun. Hatalı satış verilerini (negatif satış) düzeltin. 
 # Her ay için toplam satışları hesaplayın.
import pandas as pd
import numpy as np

data = {
    'Tarih': pd.date_range(start='2024-11-15', periods=10, freq='D'),
    'Satış': [100, 150, np.nan, -50, 120, 130, np.nan, 160, 180, 200]
}

df = pd.DataFrame(data)

df['Satış'] = df['Satış'].fillna(df['Satış'].mean())

df['Satış'] = df['Satış'].apply(lambda x: 0 if x < 0 else x)

df ['Ay'] = df['Tarih'].dt.month

aylik_toplam = df.groupby('Ay')['Satış'].sum()

print(df)
print(aylik_toplam)