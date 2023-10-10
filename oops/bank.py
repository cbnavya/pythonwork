from datetime import datetime
class bank:
    bank_name=str
    acc_no=str
    person_name=str
    balance=int
    acc_type=str

    def create(self,bank_name,acc_no,person_name,balance,acc_type):   #self=>clz akathe current objectna pointyan
        self.bank_name=bank_name
        self.acc_no=acc_no
        self.person_name=person_name
        self.balance=balance
        self.acc_type=acc_type
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited {amount} avl bal is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction insufficient")
        else:
             self.balance-=amount
        print(f"your {self.bank_name} has been debited {amount} avl bal is {self.balance}")
    def get_balance(self):
        print(f"your available balance is {self.balance} on {datetime.today()}")
obj1=bank()
obj1.create("sbi","1234","navya",1000,"savings")
obj1.deposit(200)
obj1.withdraw(10000)
obj1.get_balance()
obj2=bank()
obj2.create("sbi","4567","liya",5800,"savings")