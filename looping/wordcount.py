# text="photosynthesis"
# v_count=0
# c_count=0
# for ch in text:
#     if ch in ["a","e","i","o","u"]:
#         v_count+=1
#     else:
#         c_count+=1
# print("vowel count",v_count)
# print("consonant count",c_count)


text="photosynthesis is"
v_count=0
c_count=0
for ch in text:
    if ch in ["a","e","i","o","u"]:
        v_count+=1
    elif ch !=" ":
        c_count+=1
print("vowel count",v_count)
print("consonant count",c_count)