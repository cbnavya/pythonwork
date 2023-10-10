from re import *
variable=input("enter variable")
rule="[klm][369][\w]*"
match=fullmatch(rule,variable)
print("invalid" if match==None else "valid")