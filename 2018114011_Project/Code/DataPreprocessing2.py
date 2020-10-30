import codecs 
for i in codecs.open('../Data/pred-eng-ner'):
	i=i.strip()
	a=i.split("	")
	if a[1] != a[2]:
		print(i)

