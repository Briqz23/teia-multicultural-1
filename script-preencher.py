import io
from PyPDF2 import PdfMerger
from urllib.request import urlopen
from PIL import Image, ImageFont, ImageDraw
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import PyPDF2
from ttkthemes import ThemedTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

def validate_numbers(text):
    return text.isdigit()

def sair():
    window.destroy()


def criar():

    url_font = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial.ttf?raw=True'
    normal_font = io.BytesIO(urlopen(url_font).read())

    url_bold = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial_Bold.ttf?raw=True'
    bold_font = io.BytesIO(urlopen(url_bold).read())
    bold_font.seek(0)
    normal_font.seek(0)
    materiaFont = ImageFont.truetype(bold_font, 40)
    firstFont = ImageFont.truetype(normal_font, 30)

    numero_atv = numero_atividade_entry.get()
    etapa = etapa_combobox.get()
    materia = materia_entry.get()
    turma = turma_entry.get()
    quinzenario = quinzenario_entry.get()
    sequencia = sequencia_entry.get()
    conteudo = conteudo_entry.get()

    o_que = o_que_text.get("1.0", "end-1c")
    pra_que = pra_que_text.get("1.0", "end-1c")
    como = como_text.get("1.0", "end-1c")
    strings = [numero_atv, etapa, materia, turma, quinzenario, sequencia, conteudo, o_que, pra_que, como]
    
    strings_upper = [s.upper() for s in strings]
    if etapa == "Definir":
        img = Image.open("templates/DEFINIR-1.png")
    elif etapa == "Descobrir":
        img = Image.open("templates/DESCOBRIR-1.png")
    elif etapa == "Desenvolver":
        img = Image.open("templates/DESENVOLVER-1.png")
    else:
        img = Image.open("templates/ENTREGAR-1.png")




    draw = ImageDraw.Draw(img)

    #numero_atv
    draw.text((1150, 225), strings_upper[0], font=firstFont, fill='black')
    #matéria
    W = 1700
    _, _, w, h = draw.textbbox((0, 130), strings_upper[2], font=materiaFont)
    draw.text(((W-w)/2, 130), strings_upper[2], font=materiaFont, fill='white')

    #turma
    draw.text((320, 410), strings_upper[3], font=firstFont, fill='black')
    #quinzenário
    draw.text((970, 418), strings_upper[4], font=firstFont, fill='black')
    #sequencia
    draw.text((1310, 418), strings_upper[5], font=firstFont, fill='black')
    #conteúdo
    draw.text((750, 510), strings_upper[6], font=firstFont, fill='black')

    messagebox.showinfo("Sucesso", "Arquivo criado com sucesso!")

    #limitar a 150 caracteres no front
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


    lista_o_que = quebrar_string(strings_upper[7],65)
    o_que_y = 820
    for i in range((len(lista_o_que))):
    
        draw.text((350, o_que_y), lista_o_que[i], font=firstFont, fill='black')
        o_que_y+=50 


    lista_pra_que = quebrar_string(strings_upper[8],65)
    pra_que_y = 980
    for i in range((len(lista_pra_que))):
    
        draw.text((350, pra_que_y), lista_pra_que[i], font=firstFont, fill='black')
        pra_que_y+=50 


    lista_como = quebrar_string(strings_upper[9],65)
    como_y = 1120
    for i in range((len(lista_como))):
    
        draw.text((350, como_y), lista_como[i], font=firstFont, fill='black')
        como_y+=50 
## combinar pdfs

    img.save("test-template.pdf")
    
    #Create a list with the file paths
    pdf_files = ['test-template.pdf', 'templates/other.pdf']
    
    pdf_writer = PyPDF2.PdfWriter()
    # Merge the PDF files
    for file_path in pdf_files:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
    output_path = 'combined.pdf'

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
        
# Crie a janela principal
window = ThemedTk(theme="breeze") 
window.title("Preenchedor de ficha")


style = ttk.Style()
style.configure("RoundedEntry.TEntry", borderwidth=0, relief="solid", 
                foreground="black", background="white", font=("Arial", 12))


frame = ttk.Frame(window)
frame.pack(padx=20, pady=10)

# Informações do usuário
user_info_frame = ttk.LabelFrame(frame, text="")
user_info_frame.grid(row=1, column=0, padx=20, pady=10)

etapa_label = ttk.Label(user_info_frame, text="Etapa", font=("Arial", 12, "bold"))
etapa_label.grid(row=0, column=0, padx=5, pady=5)
etapa_combobox = ttk.Combobox(user_info_frame, values=["Definir", "Descobrir", "Desenvolver", "Entregar"], state="readonly")
etapa_combobox.grid(row=0, column=1, padx=5, pady=5)

numero_atividade_label = ttk.Label(user_info_frame, text="Número de Atividade", font=("Arial", 12, "bold"))
numero_atividade_label.grid(row=0, column=2, padx=5, pady=5)
numero_atividade_entry = ttk.Entry(user_info_frame)
numero_atividade_entry.grid(row=0, column=3, padx=5, pady=5)

materia_label = ttk.Label(user_info_frame, text="Matéria", font=("Arial", 12, "bold"))
materia_label.grid(row=1, column=0, padx=5, pady=5)
materia_entry = ttk.Entry(user_info_frame)
materia_entry.grid(row=1, column=1, padx=5, pady=5)

turma_label = ttk.Label(user_info_frame, text="Turma/Ano", font=("Arial", 12, "bold"))
turma_label.grid(row=1, column=2, padx=5, pady=5)
turma_entry = ttk.Entry(user_info_frame)
turma_entry.grid(row=1, column=3, padx=5, pady=5)

sequencia_label = ttk.Label(user_info_frame, text="Sequência", font=("Arial", 12, "bold"))
sequencia_label.grid(row=2, column=0, padx=5, pady=5)
sequencia_entry = ttk.Entry(user_info_frame)
sequencia_entry.grid(row=2, column=1, padx=5, pady=5)

conteudo_label = ttk.Label(user_info_frame, text="Conteúdo", font=("Arial", 12, "bold"))
conteudo_label.grid(row=2, column=2, padx=5, pady=5)
conteudo_entry = ttk.Entry(user_info_frame)
conteudo_entry.grid(row=2, column=3, padx=5, pady=5)

quinzenario_label = ttk.Label(user_info_frame, text="Quinzenário", font=("Arial", 12, "bold"))
quinzenario_label.grid(row=3, column=0, padx=5, pady=5)
quinzenario_entry = ttk.Entry(user_info_frame)
quinzenario_entry.grid(row=3, column=1, padx=5, pady=5)

# Caixas de texto
text_frame = ttk.LabelFrame(frame, text="Informações Adicionais")
text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

o_que_label = ttk.Label(text_frame, text="O QUE:", font=("Arial", 12, "bold"))
o_que_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

o_que_text = tk.Text(text_frame, height=2, bg="white")
o_que_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

pra_que_label = ttk.Label(text_frame, text="PRA QUÊ?", font=("Arial", 12, "bold"))
pra_que_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

pra_que_text = tk.Text(text_frame, height=2, bg="white")
pra_que_text.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

como_label = ttk.Label(text_frame, text="COMO?", font=("Arial", 12, "bold"))
como_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

como_text = tk.Text(text_frame, height=2, bg="white")
como_text.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")


button_frame = tk.Frame(window)
button_frame.pack(pady=10)

sair_button = tk.Button(button_frame, text="SAIR", command=sair, bg="#ff474c", relief="solid", bd=0)
sair_button.pack(side="left", padx=10)

criar_button = tk.Button(button_frame, text="CRIAR", command=criar, bg="#90EE90", relief="solid", bd=0)
criar_button.pack(side="left", padx=10)




frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)
text_frame.grid_columnconfigure(0, weight=1)

window.mainloop()

