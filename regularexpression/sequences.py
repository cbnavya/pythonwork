from re import *
text="abcd#@ABCD7e9fh"
Pattern="\d" #=>digits
match=finditer(Pattern,text)
for m in match:
    print(m.group(),m.start())

from re import *
text="abcd#@ABCD7e9fh"
Pattern="\D" #=>except digits
match=finditer(Pattern,text)
for m in match:
    print(m.group(),m.start())

from re import *
text="abcd#@ABCD7e9fh"
Pattern="\w" #alpha numeric
match=finditer(Pattern,text)
for m in match:
    print(m.group(),m.start())

from re import *
text="abcd#@ABCD7e9fh"
Pattern="\W" #=>special characters
match=finditer(Pattern,text)
for m in match:
    print(m.group(),m.start())
