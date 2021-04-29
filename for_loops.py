words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

#The for loop can be used to iterate over strings.

str="LTTS AND LNT"
count=0
for s in str:
    if s=="L":
        count=count+1
print(count)

###################
list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break


