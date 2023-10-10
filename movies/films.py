from json import load
path=("C:\\Users\\navya\\OneDrive\\Desktop\\python_work\\movies\\mdb.json")
with open(path,encoding="utf-8") as f:
    movies=load(f)
print(len(movies))

#print all movie name
# movie_name=[m.get("title")for m in movies]
# print(movie_name)

#print movie title released in 2005
# released_in_2005=[m.get("title")for m in movies if m.get("year")=="2005"]
# print(released_in_2005)

# print movie titles whose genre="comedy"
# genre_comedy=[m.get("title") for m in movies if "Comedy" in m.get("genres")] 
# print(genre_comedy)

# lengthy movie
# lengthy_movie=max(movies,key=lambda i:int(i.get("runtime")))
# print(lengthy_movie)

# print all genres
# all_genres={g for m in movies for g in m.get("genres")}
# print(all_genres)

# comedy movies released in 2015
# comedy_movie=[m.get("title")for m in movies if m.get("year")=="2015" and "Comedy" in m.get("genres")]
# print(comedy_movie)

#high
# wc={}
# for m in movies:
#     year=m.get("year")
#     if year in wc:
#         wc[year]+=1
#     else:
#         wc[year]=1
# print(wc)
# highest=(max(wc.values()))
# print(highest)

# adventure film
# adv_film=[m.get("title")for m in movies if "Adventure" in m.get("genres")]
# print(adv_film)
adv_film2=[m.get("title")for m in movies if m.get("year")=="1986" and "Adventure" in m.get("genres")] 
print(adv_film2)