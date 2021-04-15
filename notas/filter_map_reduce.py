# filter
my_list = [1,4,5,6,9,13,19,21]
#                   funcion de filtrado, la lista a filtrar
odd = list(filter(lambda x:x%2 != 0, my_list))
print(odd)

#map
my_list= [1,2,3,4,5]
print([i**2 for i in my_list])
#           funcion a aplicar en cada elemento, lista
powed = list(map(lambda x:x**2,my_list))
print(powed)

#reduce
my_list=[2,2,2,2,2]
all_multiplied=1
for i in my_list:
    all_multiplied *= i

print(all_multiplied)

from functools import reduce
#                       funcion para recucir, lista
#                       1.- a = my_list[0], b = my_list[1]
#                       2.- a = a*b,        b = my_list[2]

all_multiplied= reduce(lambda a,b: a*b, my_list)
print(all_multiplied)