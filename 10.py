#program 10

class Father:
    def fatherwork(self):
        print("I work as a software engineer")

class Mother:
    def motherwork(self):
        print("I work as a Data Analyst")

class Child(Father, Mother):
    pass

c1=Child()
c1.fatherwork()
c1.motherwork()
