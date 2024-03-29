cloths=[
    {"name":"lproundneckshirt","brand":"lp","varients":[
        {"size":"m","color":"red","price":2300},
        {"size":"l","color":"green","price":2300},
        ]
    },
    {"name":"lphalfsleeves","brand":"lp","varients":[
        {"size":"m","color":"red","price":1300},
        {"size":"xl","color":"green","price":1000},
        ]
    },
    {"name":"indianterrainshirt","brand":"it","varients":[
        {"size":"l","color":"white","price":1400},
        {"size":"xl","color":"green","price":2400},
        ]
    },
    {"name":"vanhusenlinen","brand":"vh","varients":[
        {"size":"m","color":"black","price":2300},
        {"size":"l","color":"green","price":2300},
        {"size":"xl","color":"pink","price":2500},
        ]
    },
]

#print shirt names available under 1300
for c in cloths:
    for v in c.get("varients"):
        if v.get("price")<1200:
            print(c.get("name"))

#print red shirts
for c in cloths:
    for v in c.get("varients"):
        if v.get("color")=="red":
            print(c.get("name"))