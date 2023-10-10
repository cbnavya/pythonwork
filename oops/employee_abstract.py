class Employee:
    data=[
        {"id":1,"name":"jhon","dept":"hr","salary":34000},
        {"id":2,"name":"hari","dept":"it","salary":24000},
        {"id":3,"name":"ravi","dept":"qa","salary":64000},
        {"id":4,"name":"vijay","dept":"hr","salary":74000},
        {"id":5,"name":"tom","dept":"it","salary":24000},
        {"id":6,"name":"vipin","dept":"qa","salary":14000},
        
    ]

#return all employee records list
    def get(self,*args,**kwargs):  #get=>list
         return self.data
    def retrieve(self,*args,**kwargs):
         id=kwargs.get("id")
         records=[emp for emp in self.data if emp.get("id")==id]
         return records
    def create(self,*args,**kwargs):
         self.data.append(kwargs)
    def destroy(self,*args,**kwargs):
         id=kwargs.get("id")
         des=[e for e in self.data if e.get("id")==id].pop()
         self.data.remove(des)
    def update(self,id=None,*args,**kwargs):
         id=id
         obj=[emp for emp in self.data if emp.get("id")==id].pop()
         obj.update(kwargs)
         print("record updated")
obj=Employee()
obj.update(id=2,name="navya",salary=34500)
print(obj.retrieve(id=2))
# obj.destroy(id=4)
# print(obj.get())
# print(obj.retrieve(id=2))
# obj.create(id=7,name="navya",dept="hr",salary=56000)
# print(obj.get())