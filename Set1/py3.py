class String:
    def getString(self):
        self.num = input("Enter a string:")
    def printString(self):
        print(self.num)

st = String()
st.getString()
st.printString()