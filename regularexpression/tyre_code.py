from re import *
tyre_num=input("enter number")
rule="\d{3}/\d{2}[R]\d{2}/\d{2,3}[A-Z?]"
match=fullmatch(rule,tyre_num)
print("invalid" if match==None else "valid")