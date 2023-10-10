text="sunil gavaskar had no holds barred remark on Overseas commentators"
vowels=["a","e","i","o","u"]
words=(text.split(" "))
print(words)
for w in words:
    if w[0].casefold() in vowels:
        print(w)