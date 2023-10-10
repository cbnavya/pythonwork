text="ABBCCDEA"
wc={}
dupli_lst=[]
for ch in text:
    if ch in wc:
        dupli_lst.append(ch)
    else:
        wc[ch]=1
print(dupli_lst[1])