from re import *
f=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\regularexpression\\data.txt")
rule1="\d{10}"
rule2="[\w]+@gmail.com"
phone_num=[]
email_id=[]
for line in f:
    words=line.rstrip("\n").split()
    for w in words:
        match1=fullmatch(rule1,w)
        match2=fullmatch(rule2,w)
        if match1!=None:
            phone_num.append(w)
        elif match2!=None:
            email_id.append(w)
print(phone_num)
print(email_id)