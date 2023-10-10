class student:
    id:int
    name:str
    age:int
    course:str

    def __init__(self,id,name,age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course

    def display_details(self):
        print(self.name,self.course) 

    def __str__(self):          #__str__=> oru objectnta string representation
        return self.name
    
std=student(123,"navya",20,"bca")
std.display_details()
print(std)