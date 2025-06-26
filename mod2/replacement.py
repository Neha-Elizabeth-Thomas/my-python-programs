replacement={"I":"You","we":"you","me":"you"}

str=input("Enter: ")
words=str.split()

def change(word):
    return replacement.get(word,word)
reply=list(map(change,words))
"""reply=[]
for word in words:
    reply.append(replacement.get(word,word))
"""
print(" ".join(reply))