all_users=["mohanlal","fahad","unni","mamooty","nivin"]
nivin_friends=["mohanlal","unni","fahad"]
suggestion_lst=[]
for u in all_users:
    if u not in nivin_friends:
        suggestion_lst.append(u)
suggestion_lst.pop(1) #=>index position
print(suggestion_lst)


#mutual frnds
nivin_friends=["mohanlal","unni","fahad"]
fahad_friends=["mohanlal","mamooty","unni"]
mutual_lst=[]
for u in nivin_friends:
    if u in fahad_friends:
        mutual_lst.append(u)
print(mutual_lst)
