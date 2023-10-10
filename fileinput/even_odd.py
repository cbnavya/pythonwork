f_read=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\fileinput\\data.text")
odd_write=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\fileinput\\odd.txt","w")
even_write=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\fileinput\\even.txt","w")

for line in f_read:
    num=int(line.rstrip("\n"))
    if num%2==0:
        even_write.write(str(num)+"\n")
    else:
        odd_write.write(str(num)+"\n")