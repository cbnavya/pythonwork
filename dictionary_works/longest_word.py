# text="hello good hello morning"
# words=text.split(" ")
# longest_word=max(words,key=lambda w:len(w))
# print(longest_word)


# min_word=min(words,key=lambda w:len(w))
# print(min_word)


text="hi i am navya good goodmorning"
words=text.split()
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)