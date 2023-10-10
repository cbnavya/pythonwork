# "a+" =>one or more occurance of a
# "a*" =>zero or more occurance of a
# "a?" =>minimum one

# from re import *
# text="aabbaaccdaaa"
# Pattern="a+" #=>one or more occurance of a
# match=finditer(Pattern,text)
# for m in match:
#     print(m.group(),m.start())

from re import *
text="aabbaaccdaaa"
Pattern="a*" #=>zero or more occurance of a
match=finditer(Pattern,text)
for m in match:
    print(m.group(),m.start())

# from re import *
# text="aabbaaccdaaa"
# Pattern="a?" #=>minimum one
# match=finditer(Pattern,text)
# for m in match:
#     print(m.group(),m.start())

# from re import *
# phone=input("enter phone number")
# rule="\d{10}" 
# match=fullmatch(rule,phone)
# if match==None:
#     print("invaild")
# else:
#     print("valid")