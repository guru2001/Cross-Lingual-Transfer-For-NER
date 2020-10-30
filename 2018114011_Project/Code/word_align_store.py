import codecs
d={}
for i in codecs.open('../Data/al.actual.ti.final'):
        i=i.strip()
        i=i.split(" ")
        # print(i[2])
        if float(i[2]) > 0.6 and float(i[2])<1 and i[2] != "NULL":
                d[i[0]]=i[1]
for i in codecs.open('../Data/temp'):
        i=i.strip()
        i=i.split("	")
        # print(i)    
        if i[0] in d:           
                 a=d[i[0]].lower()
                 print(a,end="	")
                 print(i[1])
        else:   
                print("NULL",end="	")
                print(i[1])
