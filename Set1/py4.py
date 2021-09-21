num = input("Enter the words separated by , :")
new = num.split(',')
new.sort()
for i in new:
    print(i,end=",")
# print(new)
