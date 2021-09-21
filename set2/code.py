a = ['Alice','Bob','Charls']
length = len(a)
if length == 0:
    print("Nobody likes this")
elif length == 1:
    print(f"{a[0]} likes this")
elif length == 2:
    print(f"{a[0]} and {a[1]} likes this")
elif length == 3:
    print(f"{a[0]}, {a[1]} and {a[2]} likes this")
else:
    print(f"{a[0]}, {a[1]} and {len(a[2:])} others likes this")