nums=[3,2,5]
nums.append(4)
print(nums)

numbs=[1,4,6,7]
print(len(numbs))


#The insert method is similar to append,
# except that it allows you to insert a new item at any position in the list, as opposed to just at the end.

words=["python","love"]
words.insert(1,"is")
print(words)

letters=['p','q','r','s','p','s']
print(letters.index('q'))
letters.remove('s')
print(letters)
letters.reverse()
print(letters)
print(max(letters))
print(min(letters))
print(letters.count('p'))