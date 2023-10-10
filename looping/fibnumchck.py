num=int(input("enter a number:"))
prev=0
current=1
is_fibo=False
fib_num=0
while(fib_num<=num):
    fib_num=prev+current  
    prev=current          
    current=fib_num      
    if fib_num==num:  
        is_fibo=True
        break
print(is_fibo)