num=324
sum=0
while(num!=0):
    last_digit=num%10
    num=num//10
    sum+=last_digit
print(sum)

# num=123
# output=36 (1**3 + 2**3 + 3**3)