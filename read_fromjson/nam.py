from json import load
path=("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\read_fromjson\\name.json")
with open(path) as f:
    records=load(f)
# print(records) 
names=[f.get("name")for f in records]
print(names)
