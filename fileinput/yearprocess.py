fread=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\fileinput\\years.txt","r")
fwrite=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\fileinput\\lpyear.txt","w")
for line in fread:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0:
        fwrite.write(str(year)+"\n")
    elif year%100!=0 and year%4==0:
        fwrite.write(str(year)+"\n")