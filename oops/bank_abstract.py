from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def fundtransfer():
        pass
    @abstractmethod
    def balanceenquiry():
        pass
    @abstractmethod
    def transactionhistory():
        pass
class gpay(bank):
    def fundtransfer(self):
        print("your fund is transferred")
    def balanceenquiry(self):
        print("here is your balance enquiry")
    def transactionhistory(self):
        print("your transaction history")
obj=gpay()
obj.balanceenquiry()
obj.fundtransfer()