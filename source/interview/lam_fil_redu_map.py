import functools
import operator
import itertools
list1 = [1,2,3,4,9,10,11,121,122,140,900]
list_string = ['1', '2', '3']
#print(type(list_string[0]))

# # lamda with filter
# #ex1
# list2 = list(filter(lambda x:(x<9),list1))
# print(list2)
# # ex2
# list3 = list(filter(lambda x:(x%2==0), list1))
# print(list3)


#  lamda with map
list2 = (map(lambda x:(x**2), list1))
print(list(list2))

# list_int = list(map(lambda x:int(x), list_string))
# print(list_int)
# print(type(list_int[0]))


# reduce with lamda
# list_reduce = [1,2,3,4,5,4]
# list1 = [10,2,100, 0, -1, 1001, 20000, 1999]
#
# # output = functools.reduce(lambda x,y: x/y, list_reduce)
# # print(output)
#
# largest = functools.reduce(lambda a,b: a if a<b else b, list1)
# print(largest)


# reduce with operator

#
# lis = [ 1 , 3, 5, 6, 2, ]
#
# sum = functools.reduce(operator.add, lis)
# print(sum)

# accumulate funtion

lis = [ 1, 3, 4, 10, 4 ]

print ("The summation of list using accumulate is :",end="")
print (list(itertools.accumulate(lis,lambda x,y : x+y)))

print(functools.reduce(lambda x,y:(x+y), lis))