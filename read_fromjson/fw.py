# from json import load
path=("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\read_fromjson\\data.json")
with open(path) as f:
    records=load(f)
print(records)

#print names
from json import load
path=("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\read_fromjson\\data.json")
with open(path) as f:
    records=load(f)
fw_names=[f.get("name") for f in records]
print(fw_names)

# top rating
from json import load
path=("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\read_fromjson\\data.json")
with open(path) as f:
    records=load(f)
top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)

#frontend framework name
from json import load
path=("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\read_fromjson\\data.json")
with open(path) as f:
    records=load(f)
frnt_end_name=[f.get("name") for f in records if f.get("side")=="frontend"]
print(frnt_end_name)

#python framework name
from json import load
path=("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\read_fromjson\\data.json")
with open(path) as f:
    records=load(f)
python_frmwrk=[f.get("name") for f in records if f.get("language")=="python"]
print(python_frmwrk)