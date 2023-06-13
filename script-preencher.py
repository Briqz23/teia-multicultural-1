import io
from urllib.request import urlopen
from PIL import Image, ImageFont, ImageDraw
url_font = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial.ttf?raw=True'
normal_font = io.BytesIO(urlopen(url_font).read())

url_bold = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial_Bold.ttf?raw=True'
bold_font = io.BytesIO(urlopen(url_bold).read())

normal_font.seek(0)
firstFont = ImageFont.truetype(normal_font, 30)


materia = "materia louca"
nome = "Nome Sobrenome"
dataDD = "25"
dataMM = '04'
dataYY = '2023'
turma = "quinto ano"
quinzenario = "quinzenario?"
sequencia = "sequencia?"
conteudo = "conteudo"
anotacoes_do_professor = "ESSA SÃO AS ANOTACOES DO PROFESSOR! ESTA É UMA STRING DE EXEMPLO QUE SERÁ ING DE EXEMPLO QUE SERÁ QUEBRADA EM PEDAÇOS DE 100 CARACTERES"
conceito = "10"
o_que = "DO PROFESSOR! ESTA É UMA STRING DE EXEMPLO QUE SERÁ ING DE EDE EXEMPLO QUE SERÁ ING DE E"
pra_que = "DO PROFESSOR! ESTA É UMA STRING DE É UMA STRING DE EXEMPLO QUE SERÁ ING DE E"
como = "DO PROFESSOR! ESTA É UMA STRING DE EXEMPLO QUE SERÁ ING DE DE EXEMPLO QUE SERÁ ING DE E"

img = Image.open("template.png")
draw = ImageDraw.Draw(img)

draw.text((220, 310), nome, font=firstFont, fill='black')

draw.text((1240, 310), dataDD, font=firstFont, fill='black')
draw.text((1338, 310), dataMM, font=firstFont, fill='black')
draw.text((1440, 310), dataYY, font=firstFont, fill='black')


draw.text((320, 400), turma, font=firstFont, fill='black')
draw.text((970, 400), quinzenario, font=firstFont, fill='black')
draw.text((1310, 400), sequencia, font=firstFont, fill='black')

draw.text((750, 500), conteudo, font=firstFont, fill='black')
#limitar a 150 caracteres
def quebrar_string(string, length):
    palavras = string.split()
    lista = []
    chunk = ""
    
    for palavra in palavras:
        if len(chunk) + len(palavra) <= length:
            chunk += " " + palavra if chunk else palavra
        else:
            lista.append(chunk)
            chunk = palavra
    
    if chunk:
        lista.append(chunk)
    
    return lista

lista_anotacoes_do_professor = quebrar_string(anotacoes_do_professor, 60)

lista_y = 645

for i in range((len(lista_anotacoes_do_professor))):
  
    draw.text((116, lista_y), lista_anotacoes_do_professor[i], font=firstFont, fill='black')
    lista_y+=50 


lista_o_que = quebrar_string(o_que, 60)
o_que_y = 820
for i in range((len(lista_o_que))):
  
    draw.text((350, o_que_y), lista_o_que[i], font=firstFont, fill='black')
    o_que_y+=50 


lista_pra_que = quebrar_string(pra_que, 60)
pra_que_y = 980
for i in range((len(lista_pra_que))):
  
    draw.text((350, pra_que_y), lista_pra_que[i], font=firstFont, fill='black')
    pra_que_y+=50 


lista_como = quebrar_string(como, 60)
como_y = 1120
for i in range((len(lista_como))):
  
    draw.text((350, como_y), lista_como[i], font=firstFont, fill='black')
    como_y+=50 


img.save("test-template.pdf")