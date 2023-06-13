import io
from urllib.request import urlopen
from PIL import Image, ImageFont, ImageDraw
url_font = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial.ttf?raw=True'
normal_font = io.BytesIO(urlopen(url_font).read())

url_bold = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial_Bold.ttf?raw=True'
bold_font = io.BytesIO(urlopen(url_bold).read())

normal_font.seek(0)
firstFont = ImageFont.truetype(normal_font, 40)


materia = "materia louca"
nome = "Nome"
data = "25/04/2023"
turma = "quinto ano"
quinzenario = "quinzenario?"
sequencia = "sequencia?"
conteudo = "conteudo"
anotacoes_do_professor = "essa são as anotacoes do professor! "
conceito = "10"
o_que = "o que seria essa tarea"
pra_que = "pra que seria essa tarefa"
como = "como seria essa terafa"

img = Image.open("template.png")
draw = ImageDraw.Draw(img)


img.save("test-template.pdf")