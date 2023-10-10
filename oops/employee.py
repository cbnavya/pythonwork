class employee:
    id:int
    name:str
    department:str
    gender:str

    def create(self,id,name,department,gender):
        self.id=id
        self.name=name
        self.department=department
        self.gender=gender
    def display_emp(self):
        print(self.id,self.name,self.department,self.gender)
    def __str__(self):
        return self.name
emp=employee()
emp.create(100,"navya","hr","female")
emp.display_emp()
print(emp)