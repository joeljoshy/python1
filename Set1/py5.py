tp = (1,2,3,4,5,6,7,8,9,10)
new_tp=[]
for i in tp:
    if i%2==0:
        new_tp.append(i)
print(tuple(new_tp))