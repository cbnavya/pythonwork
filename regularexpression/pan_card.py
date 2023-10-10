from re import *
pancard=input("enter number")
rule="[A-Z]{3}[PFACHT][A-Z]\d{4}[A-Z?]"
match=fullmatch(rule,pancard)
print("invalid" if match==None else "valid")