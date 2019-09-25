import codecs
for i in codecs.open('../Data/pred-eng-ner'):   ###and ../Data/pred-hin-ner
	i=i.strip()
	i=i.split("	")
	if len(i) == 4:
		print(i[0] + i[1] + "	" + i[2] + "	" + i[3]);
	else:
		 print(i[0] + "	" + i[1] + "	" + i[2]);

