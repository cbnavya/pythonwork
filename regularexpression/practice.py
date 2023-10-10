from re import *
f=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\regularexpression\\practice.txt")
rule1="[a-z]{5}\d{1}"
rule2="[a-z]"
name=[]
initial=[]
for line in f:
    text=line.rstrip("\n").split()
    for t in text:
        match1=fullmatch(rule1,t)
        match2=fullmatch(rule1,t)
        if match1!=None:
            name.append(t)
        elif match2!=None:
            initial.append(t)
print(name)
print(initial)