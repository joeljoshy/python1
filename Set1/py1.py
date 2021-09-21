dic={}
try:
    n = int(input("Enter the range : "))

    for i in range(1,n+1):
        dic[i] = i*i
    print(f"Dictionary : {dic}")
except:
    print("Enter valid number!!")