prev=0
current=1
start=1
print(prev)
print(current)
while(start<=8):
    sum=prev+current
    print(sum)
    prev=current
    current=sum
    # (prev,current)=(current=sum)
    start+=1