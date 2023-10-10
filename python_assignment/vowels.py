text=input("enter a character")
vowels=["a","e","i","o","u"]  
for ch in text:
    if ch in vowels:
        print("character is vowel")
    else:
        print("character is not vowel")
