import pandas as pd

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1 , oranges = s2)

# df = pd.DataFrame(data)

# print(df)

list = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}

# df = pd.DataFrame(list , index = [1,2,3,4] , columns = ["Name","Grade"])

df = pd.DataFrame(dict , index = ["101","202","303","404"]) 

print(df)