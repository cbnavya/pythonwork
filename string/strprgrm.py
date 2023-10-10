name="python is a scripting language"
# string=sequence of characters
# print(name.casefold())        =>upper to lower
# print(name.capitalize())      =>first letter to convert upper to lower
# print(name.count("l"))        =>count of character
# print(name.startswith("lu"))  =>start with specified character it is true
# print(name.endswith("ar"))    =>ends with specified character it is true
# print(name.isalpha())         =>check given characters are alphabet
# print(name.isdigit())         =>check given character is digit
# print(name.isalnum())         =>including alphabet and number
# print(name.strip("\n"))       =>remove specified string
# print(name.rstrip("\n"))      =>remove from right side
# print(name.lstrip("l"))       =>remove from left side
# print(name.index("l"))        =>return first occur index position
words=(name.split(" "))         
print(words)
for w in words:
    print(w)