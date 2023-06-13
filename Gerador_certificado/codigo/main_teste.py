import io
from urllib.request import urlopen
from PIL import Image, ImageFont, ImageDraw
url_font = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial.ttf?raw=True'
normal_font = io.BytesIO(urlopen(url_font).read())

url_bold = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial_Bold.ttf?raw=True'
bold_font = io.BytesIO(urlopen(url_bold).read())

month = 'maio'
day = '3'
name = secondBlock = 'Vitor guirão soller '
social_name = None
code = 'CODE123'
title = 'cURSO - Aplicacaoda manufatua aditaiva para industria - casos de sucesso ganhos cuidadso a serem tomados e melhores práticas.'
text_date = '22 de maio de 2023'
duration_text = '90 minutos'

firstBlockA = 'O'
firstBlockB = 'Instituto Mauá de Tecnologia confere'
firstBlockC = 'a'

SecondBlock = str()
if social_name != None:
    SecondBlock = social_name
else:
    SecondBlock = name


thirdBlock_a = "o presente certificado, por ter participado da:"
thirdBlock_b = title
ThirdBlock_c1 = "realizada no dia "
ThirdBlock_c2 = text_date
ThirdBlock_d = "na Semana Mauá de Inovação e Liderança e Empreendedorismo,"
ThirdBlock_e1 = "com duração de " 
ThirdBlock_e2 = duration_text


FourthBlock = "São Caetano do Sul, 21 de maio de 2023."
            # fontes e fontsize a serem definidos
normal_font.seek(0)
firstFont = ImageFont.truetype(normal_font, 40)

bold_font.seek(0)
firstFontbd = ImageFont.truetype(bold_font, 40)


secondFont = ImageFont.truetype(bold_font, 60)


thirdFont = ImageFont.truetype(normal_font, 40)

thirdFontbd = ImageFont.truetype(bold_font, 40)

fourthFont = ImageFont.truetype(normal_font, 40)



#diretório "geral" / não-relativo
img = Image.open("/home/briqz23/Documents/git_repos/teia-multicultural-1/Gerador_certificado/codigo/certificado-smile-2023[1].png")
draw = ImageDraw.Draw(img)

#Largura e altura do certificado
W, H = (2667, 1500)
spc = 8

# obs: y=0 é a altura no meio da imagem
#Capturar largura e altura do primeiro bloco de texto
#espaçamento do espaço é spc = 4

_, _, w, h = draw.textbbox((0, 300), firstBlockA, font=firstFont)
w1 = w +spc
_, _, w, h = draw.textbbox((0, 300), firstBlockB, font=firstFontbd)
w2 = w1 + w + spc
_, _, w, h = draw.textbbox((0, 300), firstBlockC, font=firstFont)
w3 = w2 + w




#coeficiente k de disposição dos textos ao longo do eixo y:

yk = H/646


#plotar primeiro bloco de texto
#alteração pra /3 pra aumentar o espaçamento
draw.text(((W-w3)/2, ((H-h)/2.5)), firstBlockA, font=firstFont, fill='black')
draw.text((((W-w3)/2)+w1, (H-h)/2.5), firstBlockB, font=firstFontbd, fill='black')
draw.text((((W-w3)/2)+w2, (H-h)/2.5), firstBlockC, font=firstFont, fill='black')



#Capturar largura e altura do primeiro bloco de texto
_, _, w, h = draw.textbbox((0, 80*yk), secondBlock, font=secondFont)
#plotar primeiro bloco de texto
draw.text(((W-w)/2, (H-h)/2), secondBlock, font=secondFont, fill='black')

#Capturar largura e altura do primeiro bloco de texto
_, _, w, h = draw.textbbox((5, -68*yk), thirdBlock_a , font=thirdFont)
#plotar primeiro bloco de texto
draw.text(((W-w)/2, (H-h)/2), thirdBlock_a , font=thirdFont, fill='black')

#Capturar largura e altura do primeiro bloco de texto
_, _, w, h = draw.textbbox((0, (-110)*yk), thirdBlock_b, font=thirdFontbd)
#plotar primeiro bloco de texto
draw.text(((W-w)/2, (H-h)/2), thirdBlock_b, font=thirdFontbd, fill='black')
h_terceira_linha = (H-h)/2

#"realizado no dia + {dia}"

_, _, w, h = draw.textbbox((0, 300), ThirdBlock_c1, font=thirdFont)
w1 = w +spc
_, _, w, h = draw.textbbox((0, 300), ThirdBlock_c2, font=thirdFontbd)
w2 = w1 + w
draw.text(((W-w2)/2, (h_terceira_linha+50)), ThirdBlock_c1, font=thirdFont, fill='black')
draw.text((((W-w2)/2)+w1, (h_terceira_linha+50)), ThirdBlock_c2, font=thirdFontbd, fill='black')

_, _, w, h = draw.textbbox((0, (-200)*yk), ThirdBlock_d, font=thirdFont)
#plotar primeiro bloco de texto
draw.text(((W-w)/2, (H-h)/2), ThirdBlock_d, font=thirdFont, fill='black')


#"com duração de + {duracao}"
_, _, w, h = draw.textbbox((0, 300), ThirdBlock_e1 , font=thirdFont)
w1 = w +spc
_, _, w, h = draw.textbbox((0, 300), ThirdBlock_e2, font=thirdFontbd)
w2 = w1 + w

draw.text(((W-w2)/2, (h_terceira_linha+155)), ThirdBlock_e1, font=thirdFont, fill='black')
draw.text((((W-w2)/2)+w1,(h_terceira_linha+155)), ThirdBlock_e2, font=thirdFontbd, fill='black')



#Capturar largura e altura do primeiro bloco de texto
_, _, w, h = draw.textbbox((0, -320*yk), FourthBlock, font=fourthFont)
#plotar primeiro bloco de texto
draw.text(((W-w)/2, (H-h)/1.8), FourthBlock, font=fourthFont, fill='black')

img.save("test.pdf")