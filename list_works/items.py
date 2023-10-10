foods=[
    {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
    {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
    {"id":3,"name":"cb","price":170,"category":"non-veg"},
    {"id":4,"name":"bb","price":190,"category":"non-veg"},
    {"id":5,"name":"fried-rice","price":140,"category":"veg"},
    {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
    {"id":7,"name":"nan","price":70,"category":"veg"},
    {"id":8,"name":"alfham","price":370,"category":"non-veg"},
     
]

# total number of items ?
print(len(foods))
# print name whose category = veg ?
for i in foods:
    if i.get("category")=="veg":
        print(i.get("name"))
# food names available under rs 100 ?
for i in foods: 
    if i.get("price")<100:
        print(i.get("name"))
# costly item ?
costly_items=max(foods,key=lambda f:f.get("price"))
print(costly_items)
# costly non-veg food ?
non_veg_foods=[f for f in foods if f.get("category")=="non-veg"]
costly_nonveg=max(non_veg_foods,key=lambda f:f.get("price"))
print(costly_nonveg)
#print all categories ?
categories={f.get("category") for f in foods}
print(categories)