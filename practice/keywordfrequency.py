text = input("Enter String: ")
words = text.upper().split(" ")
dictt = {}
for word in words:
    if word not in dictt:
        dictt[word] = 1
    else:
        dictt[word] += 1
print(dictt)