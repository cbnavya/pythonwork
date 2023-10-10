# from re import *
# text="ababababcab"
# match=finditer("ab",text)
# count=0
# for m in match:
#     print(m.start(),m.group())
#     count+=1
# print(count)

# check digit
# from re import *
# text="abcdABCD7e9fh"
# Pattern="[0-9]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# check lowercase
# from re import *
# text="abcdABCD7e9fh"
# Pattern="[a-z]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# check uppercase
# from re import *
# text="abcdABCD7e9fh"
# Pattern="[A-Z]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# check all alphabets
# from re import *
# text="abcdABCD7e9fh"
# Pattern="[a-zA-Z]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# check both digits and alphabets
# from re import *
# text="abcdABCD7e9fh"
# Pattern="[a-zA-Z0-9]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# except numbers
# from re import *
# text="abcd#@ABCD7e9fh"
# Pattern="[^0-9]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# only special character
# from re import *
# text="abcd#@ABCD7e9fh"
# Pattern="[^a-zA-Z0-9]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# vowels
# from re import *
# text="abcd#@ABCD7e9fh"
# Pattern="[aeiouAEIOU]"
# match=finditer(Pattern,text)
# for m in match:
#     print(m.start(),m.group())

# consonants
from re import *
text="abcd#@ABCD7e9fh"
Pattern="[^aeiouAEIOU]"
match=finditer(Pattern,text)
for m in match:
    if m.group().isalpha():
        print(m.group())

# another method of consonant
# from re import *
# text="abcd#@ABCD7e9fh"
# Pattern="[^aeiou\W\d]"
# match=finditer(Pattern,text.casefold())
# for m in match:
#     if m.group().isalpha():
#         print(m.group())
