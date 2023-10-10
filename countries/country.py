from json import load
path="C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\countries\\countries.json"
with open(path,encoding="utf-8") as c:
    country=load(c)
# print(len(country))

# arabic language country
# for c in country:
#     for l in c.get("languages"):
#         if l.get("name")=="Arabic":
#             print(c.get("name"))

high_callingcode=max(country,key=lambda i:i.get("callingCodes"))
# print(high_callingcode)

starts_withc=[c.get("name")for c in country if c.get("name").startswith("C")]
# print(starts_withc)

name_capital=[[c.get("name"),c.get("capital")]for c in country]
# print(name_capital)

country_with_borders=[c for c in country if "borders" in c]
max_border=max(country_with_borders,key=lambda c:len(c.get("borders")))
# print(max_border.get("name"))

india_borders=[c.get("borders")for c in country if c.get("name")=="India"][0]
# print(india_borders)
india_borders_names=[c.get("name")for c in country if c.get("alpha3Code") in india_borders]
# print(india_borders_names)

regions_name={c.get("region")for c in country}
# print(regions_name)

non_independent=[c.get("name")for c in country if c.get("independent")==False]
# print(non_independent)

population_filter=[c.get("name")for c in country if c.get("population") < 400000]
# print(population_filter)

re={}
for c in country:
    region=c.get("region")
    if region in re:
        re[region]+=1
    else:
        re[region]=1
print(re)