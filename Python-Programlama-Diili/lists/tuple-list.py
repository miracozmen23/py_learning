my_list = [1,2,3]
my_tuple = (1,2,3,1)      # değiştirelemez

print(type(my_list))
print(type(my_tuple))

my_list[0] = 2
# my_tuple[0] = 2         #hata verir

my_list.append(3)
my_tuple.count(1)
print(my_list)
print(my_tuple.count(1))

my_tuple2 = tuple([2,3,4]) #Listeden tupleye tür dönüşümü
my_list2 = list((2,3,4))   #Tupleden listeye tür dönüşümü

print(type(my_tuple2))
print(type(my_list2))