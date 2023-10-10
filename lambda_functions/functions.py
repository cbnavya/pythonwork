sub=lambda n1,n2:n1-n2
print(sub(10,5))

cube=lambda n:n**3
print(cube(5))

add=lambda n1,n2:n1+n2
print(add(4,2)) 

max_two=lambda n1,n2:n1 if n1>n2 else n2
print(max_two(10,20))

num=lambda n:"even" if n%2==0 else "odd"
print(num(1))

get_len=lambda w:len(w)
print(get_len("hello"))

smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(10,4))