# 3 digit   
# num=407
# original=num
# sum=0
# while(num!=0):               
#     last_digit=num%10  #407%10=40.7=7 40
#     num=num//10        #40.7=40
#     cube=(last_digit**3) #cube=7**3
#     sum+=cube  #0+=343=343
# print(sum)
# if(original==sum):
#     print("its armstrong")
# else:
#     print("not armstrong")


# # 4 digit
# num=1634
# original=num
# sum=0
# while(num!=0):
#     last_digit=num%10 
#     num=num//10
#     cube=(last_digit**4)
#     sum+=cube
# print(sum)
# if(original==sum):
#     print("its armstrong")
# else:
#     print("not armstrong")





num=407
original=num
sum=0
while(num!=0):
    last_digit=num%10
    num=num//10
    cube=last_digit**3
    sum=sum+cube
print(sum)
if (sum==original):
     print("its armstrong")
else:
     print("its not armstrong")