student={"roll":32,"name":"navya","course":"django"}
print(student["course"])
if "total" in student:
    print("present")
else:
    print("not present")
student["grade"]="A"
print(student["grade"])