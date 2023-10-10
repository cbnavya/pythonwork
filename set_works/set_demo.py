# lst=[10,20,30,20,30]
# st=set(lst) #=>remove duplicates frm lst
# print(st)  

# st={10,20,30}
# st.add(100) #add to st
# print(st)

#union
# st1={10,20,30}
# st2={11,12,13,14}
# union_set=st1.union(st2)
# print(union_set)

#intersection
# st1={10,20,30,14}
# st2={11,12,13,14}
# intersection_set=st1.intersection(st2)
# print(intersection_set)

#difference
st1={10,20,30,14}
st2={11,12,13,14}
difference_set=st1.difference(st2)
print(difference_set)