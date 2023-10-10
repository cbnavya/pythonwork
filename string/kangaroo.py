text="chicken"
out="hen"
sort_text=sorted(text)
sort_out=sorted(out)
# kan=False
for w in sort_out:
    if w in sort_text:
        kan=True
    else:
        kan=False
if kan==True:
    print("its a kangaroo word")
else:
    print("its not a kangaroo word")
