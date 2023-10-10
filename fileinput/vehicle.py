f=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\fileinput\\numbers.txt","r")
numbers=[line.rstrip("\n") for line in f]
for n in numbers:
    if n.startswith("kl"):
        print(n)
# kl_numbers=[n for n in numbers if n.startswith("kl")]
# print(kl_numbers)