all_users=["sachin","dhoni","kohli","rohit","sanju","padikkal"]
sanju_followings=["sachin","padikkal"]
suggestions=list(set(all_users).difference(set(sanju_followings)))
sanju_pos=suggestions.index("sanju")
suggestions.pop(sanju_pos)
print(suggestions)