# class bike:
#     def start(self):
#         print("kicker")
#     def breaking(self):
#         print("dumb breaker")
# class herohonda(bike):
#     def start(self):
#         print("self start")
#     def breaking(Self):
#         print("breakers")

# obj=herohonda()
# obj.start()

class Parent:
    vehicles=["duke","swift"]

    def properties(self):
        return self.vehicles
    
class Child(Parent):
    def properties(self):
        self.vehicle=super().properties()
        self.vehicle.append("hunter")
        return self.vehicle
ch=Child()
print(ch.properties())