num = (input("Enter the numbers separated by , :"))
new = num.split(',')
lst = []
for i in new:
    lst.append(int(i))
print(lst)
sm = min(filter(lambda i:i%2 != 0,lst))
print("Smallest odd number:",sm)
