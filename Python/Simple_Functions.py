def capitalizename(s):
    l=s.split(" ")
    for i in range(0,len(l)):
        l[i]=l[i].capitalize()
    name=" ".join(l)
    return name
