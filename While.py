i=1
while i<=5:
    print(i)
    i=i+1

print("finished")

# *****multiple conditions inside while loop*****
x=1
while x<10:
    if x%2 == 0:
        print(str(x)+"even")
    else:
        print(str(x)+"odd")
    x=x+1

# Break
# To end a while loop prematurely, the break statement can be used.
i=0
while True:
    print(i)
    i=i+1
    if i>5:
        print("Breaking")
        break
print("Finished")

#Continue

i=1
while i<=5:

    i=i+1
    if i==3:
        print("skipping 3")
        continue
print(i)
print("finished")



