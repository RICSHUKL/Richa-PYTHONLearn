import copy

# # this is aliasing
#
#list_single = [[1, 'x', 'y'], 2, 3, 4, 5]
#
# list1 = list_single
#
# print(list1)
#
# print(list_single)
#
# list_single[0][0] = 'x'
#
# print(list1)
#
# print(list_single)
#
# print(list1 is list_single)
# print( id(list1) == id(list_single) )


# this example of shallow copy which faster
a = [1, 2, [3,10,11], 4, 5]

b = copy.copy(a)

print(a)
print(b)
print(a is b)
a[0] = 'x'
b[0] = 'a'
a[2][0] = 'check'
b[2][1] = 'this'
print('this is a',a)
print('this is b', b)


# deep copy which slow and work on nested data
# a = [1, 2, [3,10,11], 4, 5]
#
# b = copy.deepcopy(a)
#
# print(a)
# print(b)
# print(a is b)
# a[0] = 'x'
# b[0] = 'a'
# a[2][0] = 'check'
# b[2][1] = 'this'
# print('this is a',a)
# print('this is b', b)
