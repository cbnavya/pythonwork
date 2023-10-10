text="ABCDA"
wc={}
for ch in text:
    if ch in wc:
        print("print first recursive character",ch)
        break
    else:
        wc[ch]=1