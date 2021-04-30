#open
myfile=open("ok.txt","w")
#close
myfile.close()

#read
file=open("Lists.py","r")
cont=file.read()
print(cont)
file.close()
######
file = open("for_loops.py", "r")

for line in file:
    print(line)

file.close()

#write

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

#working with files

try:
    file=open("newfile.txt","r")
    file.read()
except:
    file.close()
###with
with open("Strings.py") as f:
    print(f.read())

