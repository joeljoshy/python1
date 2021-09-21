class Circle:
    def radius(self,r):

        self.r = r

    def area(self):
        print("Area = ",3.14*(self.r**2))

ar = Circle()
ar.radius(8)
ar.area()