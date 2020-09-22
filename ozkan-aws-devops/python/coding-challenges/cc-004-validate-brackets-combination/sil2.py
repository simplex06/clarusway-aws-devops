def is_wellformed(data):
    cont=True
    while cont==True:
        cont=False
        for i in ["()","{}","[]"]:
            if i in data:
                cont=True
                data = data.replace(i,"")
    return len(data)==0

print(is_wellformed("(()"))