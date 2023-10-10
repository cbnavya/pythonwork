# kwargs=>dictionary format
def student(**kwargs):
    print(kwargs.get("name"))
student(name="navya",dept="hr",location="kdlr",salary=12000)

# create a function display students and print student name and course
def display_student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))
display_student(name="ayva",course="bca",roll=122,gender="female")