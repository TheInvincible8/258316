# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#
print("{0}{1}{0}".format("abra", "cad"))
####
a = "{x}, {y}".format(x=5, y=12)
print(a)

#String Functions:

#join - joins a list of strings with another string as a separator.
#replace - replaces one substring in a string with another.
#startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
#To change the case of a string, you can use lower and upper.
#The method split is the opposite of join turning a string with a certain separator into a list.


print(", ".join(["spam","eggs","ok"]))
print("Hello me".replace("me","you"))
print("ok boomer".startswith("ok"))
print("ok boomer".endswith("boomer"))
print("HELLO SIR".lower())
print("ok sir".upper())
print("My, name, is, pankaj".split(", "))

#numeric functions
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

#####
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)