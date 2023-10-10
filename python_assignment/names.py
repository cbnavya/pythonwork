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
