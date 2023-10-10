# from re import *
# variable=input("enter variable")
# rule="[a-zA-Z][a-zA-Z0-9]*"
# match=fullmatch(rule,variable)
# print("valid" if match!=None else "invalid")


from re import *
variable=input("enter variable")
rule="[klm][369][\w]*"
match=fullmatch(rule,variable)
print("invalid" if match==None else "valid")