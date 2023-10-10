#method overloading=>same method name diff number of parameters
class calculator:
    def add(self,n1,n2):
        return n1+n2
    
    def add(self,n1,n2,n3):
        return n1+n2+n3
    
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
obj=calculator()
print(obj.add(10,20))