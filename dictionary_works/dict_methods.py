student={"roll":32,"name":"navya","course":"django"}
print(student.get("salary"))
print("hello")

student={"roll":32,"name":"navya","course":"django"}
for k in student.keys():
    print(k)

student={"roll":32,"name":"navya","course":"django"}
for v in student.values():
    print(v)

student={"roll":32,"name":"navya","course":"django"}
for k,v in student.items():
    print(k,v)