source_word="decreased"   
target_word="dress"
wc={}
is_kangaroo=True
for ch in source_word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
for ch in target_word:
    if ch in wc and wc[ch]>0:
        wc[ch]-1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)