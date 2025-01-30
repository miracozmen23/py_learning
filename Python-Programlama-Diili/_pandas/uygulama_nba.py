import pandas as pd

df = pd.read_csv("D:\Python-Programlama-Diili\_pandas/nba.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- Toplam kaç kayıt vardır ?
result = len(df)

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
result = df["Salary"].mean()

# 4- En yüksek maaşı ne kadardır ?
result = df["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ve pozisyonu nedir ?
result = df[df["Salary"] == df["Salary"].max()][["Name","Position"]].iloc[0]

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı 50 kaydını getiriniz.
result = df[((df["Age"] >= 20) & (df["Age"] <=25))][["Name","Team","Age"]].sort_values("Age",ascending=False).head(50)

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = df[df["Name"] == "John Holland"][["Name","Team"]].iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
# result = df.groupby("Team").mean()["Salary"]

# 9- Kaç farklı takım mevcut ?
result = len(df.groupby("Team"))
result = df["Team"].nunique()

# 10- Her takımda kaç oyuncu oynamaktadır ?
result = df["Team"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
# df = df.dropna()
# result = df[df["Name"].str.contains("and")]

df.dropna(inplace=True)

def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]

print(result)
