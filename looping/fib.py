limit=24
pre=0
current=1
print(pre)
print(current)
for i in range(1,limit+1):
    sum=pre+current  
    pre=current     
    current=sum
    if(sum<=limit):
        print(sum)
    else:
        break