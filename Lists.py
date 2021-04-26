List1=['pankaj',3,'ok']
print(List1)

List2=[2,4,[5,7,8],10]
print(List2)
num=3
Things=["hello",0,[1,2,num,4.56]]
print(Things[1])
print(Things[2])
print(Things[2][2])

#listOperations
Items=[7,7,7,7]
Items[2]=6
print(Items)


nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

#To check if an item is in a list, the in operator can be used.
#It returns True if the item occurs one or more times in the list, and False if it doesn't.

words=["pankaj","egg","ltts"]
print("ltts" in words)


numbs = [10, 9, 8, 7, 6, 5]
numbs[0] = numbs[1]-5
if 4 in numbs:
  print(numbs[3])
else:
  print(numbs[4])

ok=[3,2,1]
print(not 5 in ok)