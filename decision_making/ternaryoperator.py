num=10
odd_even="even" if num%2==0 else "odd"
print(odd_even)

num1=10
num2=20
largest="num1" if num1>num2 else "num2"
print(largest)

num=15
num_chk="+ve" if num>0 else "-ve"
print(num_chk)

num=55
result="abc" if num%5==0 else "cdc"
print(result)

n1=50
n2=10
result=n1-n2 if n1>n2 else n2-n1
print(result)

num=int(input("enter a number"))
result=num+1 if num>5 else num-1
print(result)

# 2 condition
num=5
result=num+1 if num>5 else num-1 if num<5 else 5
print(result)

leap_yr=int(input("enter year"))
result="leap year" if leap_yr%100==0 and leap_yr%400==0 else "leap year" if leap_yr%100!=0 and leap_yr%4 else "not leap year"
print(result)