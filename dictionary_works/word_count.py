text="good morning good evening"
words=text.split(" ")
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
print(wc)