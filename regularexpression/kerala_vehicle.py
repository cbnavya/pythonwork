from re import *
vehicle_num=input("enter num")
rule="(KL)[0-9]{2}[A-Z]{1,2}\d{4}"
match=fullmatch(rule,vehicle_num)
print("invalid" if match==None else "valid")