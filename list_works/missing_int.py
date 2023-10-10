lst=[1,4,2,5,6]
lst.sort()
if(lst[0]!=1):
    print("1 is missing")
else:
    for i in range(0,len(lst)):
        current=lst[i]
        next=lst[i+1]
        diff=next-current
        if diff!=1:
            print(current+1,"is missing")
            break