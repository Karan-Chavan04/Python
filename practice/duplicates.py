a=input("Enter languages: ")
c=a.upper()
b=c.split(" ")
print(b)
skills=[]
for i in b:
    if i not in skills:
        skills.append(i)
    else:
        break
    if i in skills:
        print(i)
    
