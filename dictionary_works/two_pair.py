lst=[2,3,5,7,4]
sum=8
lst.sort()
low=0
upper=len(lst)-1
while(low<upper):
    curr_sum=lst[low]+lst[upper]
    if curr_sum==sum:
        print("pairs",lst[low],lst[upper])
        #break
        low+=1  #=>get one or more pair
    elif curr_sum < sum:
        low+=1
    else:
        upper-=1