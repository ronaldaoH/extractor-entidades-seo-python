import textrazor

def takeSecond(elem):
    return elem[1]

textrazor.api_key = "XXXX"
client = textrazor.TextRazor(extractors=["entities"])

entidades_lista =[] 
response = client.analyze_url("https://ronaldao.com")
for entity in response.entities():
    entidades_lista.append([entity.id, entity.confidence_score])

entidades_lista.sort(key=takeSecond, reverse=True)

for entidades in entidades_lista:
	print(entidades)

with open('OUTPUT_ENTIDADES.txt', 'w') as f:
	f.write("ENTIDAD , CONFIDENCIA" + '\n')
	for item in entidades_lista:
		f.write("%s\n" % str(item).replace("[","").replace("]",""))