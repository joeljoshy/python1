#Username
mail = (input("Enter your email : "))
pos = mail.index('@')
username = mail[:pos]
print("Username : ",username)

