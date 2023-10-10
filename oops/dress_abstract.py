class Dress:
    data=[
        {"id":1,"model":"jeans","size":"xl","color":"black","price":1120},
        {"id":2,"model":"top","size":"s","color":"red","price":999},
        {"id":3,"model":"skirt","size":"xxl","color":"black","price":1110},
        {"id":4,"model":"kurtis","size":"xl","color":"yellow","price":1090},
        {"id":5,"model":"frock","size":"l","color":"pink","price":1111},
    ]

    def get(self,*args,**kwargs):
        return self.data
    def retrieve(self,*args,**kwargs):
        id=kwargs.get("id")
        drs=[dr for dr in self.data if dr.get("id")==id]
        return drs
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
    def destroy(self,*args,**kwargs):
        id=kwargs.get("id")
        des=[dr for dr in self.data if dr.get("id")==id].pop()
        self.data.remove(des)
obj=Dress()
print(obj.destroy(id=2))
# obj.create(id=6,model="shorts",size="xs",color="blue",price=789)
print(obj.get())
# print(obj.retrieve(id=2))

