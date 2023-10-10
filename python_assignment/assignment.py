#Q1
num=int(input("enter a number"))
if(num<=20):
    print("thank you")
else:
    print("incorrect answer")

#Q2
num=int(input("enter a number"))
if(num<10):
    print("too low")
elif(num>10) and (num<20):
    print("correct")
else:
    print("too high")

#Q3
age=int(input("enter age"))
if(age>=18):
    print("you can vote")
elif(age==17):
    print("you can learn to ride")
elif(age==16):
    print("you can buy a lottery ticket")
else:
    print("you can go for treat")

#Q4
num=int(input("enter a number"))
if num==1:
    print("Thank you")
elif num==2:
    print("Well done")
elif num==3:
    print("correct")
else:
    print("Error message")

#Q5
num=int(input("enter a number"))
if num%2==0 or num%3==0:
    print("its divisible")
else:
    print("not divisible")

#Q6
text=input("enter a character").casefold()
vowels=["a","e","i","o","u"]  
for ch in text:
    if ch in vowels:
        print("character is vowel")
    else:
        print("character is not vowel")

#Q8
num=int(input("enter a number"))
for i in range(num):
    if num%2==0:
        print("even")
        break
    else:
        print("odd")

#Q9
text=input("enter name")
start=0
while(start<3):
    start+=1
    print(text)

#Q10
name=input("enter a name")
number=int(input("enter a number"))
start=0
while(start<number):
    if number<10:
        print(name)
        start+=1
    else:
        print("too high")
        break

#Q12
while True:
    num=int(input("entr the number"))
    if num>5:
        print(f"you latst entered number was ",num)

#Q13
while True:
    num=int(input("enter a number"))
    if num<10:
        print("too low")
    elif num>20:
         print("too high")
    else:
         print("Thank you")
         break
    
#Q14
start=10
end=300
for i in range(10,301,10):
    print(i)

#Q15
start=1
end=5
total=0
while(start<=end):
    total=total+start
    start+=1
    average=total/end
print(round(average))