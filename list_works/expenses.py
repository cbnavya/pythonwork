expenses=[12000,13000,14000,15000,20000,22000]
print(expenses[1])
for e in expenses:
    if e > 15000:
        print(e)


#total expenses
expenses=[12000,13000,14000,15000,20000,22000]
total=0
for e in expenses:
    total=total+e
print(total)


#highest expenses
expenses=[12000,13000,14000,15000,20000,22000]
max_exp=0
for e in expenses:
    if e > max_exp:
        max_exp=e
print(max_exp)

#cheapest expense
expenses=[12000,13000,14000,15000,20000,22000]
min_exp=expenses[0]
for e in expenses:
    if e < min_exp: 
        min_exp=e   
print(min_exp)

#sum(),min(),max() => built in functions
expenses=[12000,13000,14000,15000,20000,22000]
total_exp=sum(expenses)
print(total_exp)

min_exp=min(expenses)
print(min_exp)

max_exp=max(expenses)
print(max_exp)