my_tuple = "one", "two", "three"
print(my_tuple[0])

#list slices
list1=[2,4,6,1,8,9,19]
print(list1[2:5])
print(list1[2:6:2])

#list comprehension
cubes=[i**3 for i in range(7)]
print(cubes)

nums = [i*2 for i in range(10)]
print(nums)

#####
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)