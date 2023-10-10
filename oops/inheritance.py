# inheritance=>child class aquired methods and properties of parent class
class parent:
    mob="oppoa52"
    vehicle="duke"

    def mobile(self):
        print(self.mob)
    def bike(self):
        print(self.vehicle)


class child(parent):
    pass
obj=child()
obj.mobile()
obj.bike()