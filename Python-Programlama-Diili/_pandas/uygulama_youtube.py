import pandas as pd

df = pd.read_csv("D:\Python-Programlama-Diili\_pandas/_videos.csv")

# 1- İlk 10 kaydı getiriniz.
result = df.head(10)

# 2- İkinci 5 kaydı getiriniz.
result = df[5:10]

# 3- Dataset' de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns
result = len(df.columns)

# 4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listeleyiniz.
# (thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description)
df = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1)
result = df

# 5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını bulunuz.
result = df['likes'].mean()
result = df['dislikes'].mean()

# 6- ilk 50 videonun like ve dislike kolonlarını getiriniz.
result = df.head(50)[['title','likes','dislikes']]

# 7- En çok görüntülenen video hangisidir ?
result = df[df['views'].max() == df['views']][['title','views']]

# 8- En düşük görüntülenen video hangisidir?
result = df[df['views'].min() == df['views']][['title','views']]

# 9- En fazla görüntülenen ilk 10 video hangisidir ?
result = df.sort_values('views',ascending=False).head(10)[['title','views']]

# 10- Kategoriye göre beğeni ortalamalarını sıralı şekilde getiriniz.
# result = df.groupby('category_id').mean().sort_values('likes')['likes']

# 11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
# result = df.groupby('category_id').sum().sort_values('comment_count',ascending=False)['comment_count']

# 12- Her kategoride kaç video vardır ?
result = df['category_id'].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df['title_len'] = df['title'].apply(len)
result=df

# 14- Her video için kullanılan tag sayısını yeni kolonda gösteriniz.
df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))

# 15- En popüler videoları listeleyiniz.(like/dislike oranına göre)

def likedislikeoranhesapla(dataset):
    likeslist = list(dataset['likes'])
    dislikeslist = list(dataset['dislikes'])
    
    liste = list(zip(likeslist,dislikeslist))
    
    oranlistesi = []
    
    for like,dislike in liste:
        if (like+dislike == 0):
            oranlistesi.append(0)
        else:
            oranlistesi.append(like/(like+dislike))
    
    return oranlistesi
    
df['begeni_orani'] = likedislikeoranhesapla(df)

print(df.sort_values('begeni_orani',ascending=False).head(50)[['title','likes','dislikes','begeni_orani']])
