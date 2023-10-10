f=open("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\fileinput\\data.text","r")
lst=[]  #=>empty list for add the datatext
for line in f:
    lst.append(line.rstrip("\n")) #=>remove (\n)
print(lst)
longest_wrd=max(lst,key=lambda w:len(w))
print(longest_wrd)


#listcomprehesion
# longest_word=max([line.rstrip("\n") for line in f],key=lambda w:len(w))
# print(longest_word)