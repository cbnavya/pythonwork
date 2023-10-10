year=int(input("enter a year"))
if(year%100==0 and year%400==0):
    print("its leap year")
elif(year%100!=0 and year%4==0):
    print("its a leap year")
else:
    print("its not a leap year")


# case1:if the year is century year (last two num zero eg:2200)
# case2:if the year is not century year