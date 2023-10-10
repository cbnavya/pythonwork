# #*args=>accept many numbers(no limit) in tuple format
# def product(*args):
#     res=1
#     for n in args:
#         res=res*n
#     return res
# print(product(1,2,3,4,5,6))


# person details
# def person_details(*args):
#     for v in args:
#         print(v)
# print(person_details("hari","tvm","hr"))

# create a function max_word that will accept any number of parameters and return lengthy string
def max_word(*args):
    len_word=max(args,key=lambda w:len(w))
    return len_word
print(max_word("hello","hi","goodevening"))

