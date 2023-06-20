#SEM TTKBOOSTRAP
import io
import textwrap
from urllib.request import urlopen
from PIL import Image, ImageFont, ImageDraw
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import PyPDF2
from ttkthemes import ThemedTk
from datetime import datetime
import os


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
    instrucoes = instrucoes_text.get("1.0", "end")
    wrapped_instrucoes = textwrap.wrap(instrucoes, width=50)
    lines = instrucoes.split('\n')

    strings = [numero_atv, etapa, materia, turma, quinzenario, sequencia, conteudo, o_que, pra_que, como, instrucoes]
    
    
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
    draw.text((1154, 225), strings[0], font=firstFont, fill='black')
    #matéria
    W = 1700
    _, _, w, h = draw.textbbox((0, 130), strings[2], font=materiaFont)
    draw.text(((W-w)/2, 130), strings[2], font=materiaFont, fill='white')

    #turma
    draw.text((320, 410), strings[3], font=firstFont, fill='black')
    #quinzenário
    draw.text((980, 418), strings[4], font=firstFont, fill='black')
    #sequencia
    draw.text((1310, 418), strings[5], font=firstFont, fill='black')
    #conteúdo
    draw.text((750, 510), strings[6], font=firstFont, fill='black')
    #instrucoes
    
    y=1363
    for line in lines:
        wrapped_lines = textwrap.wrap(line, width=100) 

        for wrapped_line in wrapped_lines:
            draw.text((332, y), wrapped_line, font=firstFont, fill='black')
            y += firstFont.getbbox(wrapped_line)[1] + 35

    y += 35  
    messagebox.showinfo("Sucesso", "Arquivo criado com sucesso! Eles serão armazenados na pasta ABRIR > fichas")
    


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


    lista_o_que = quebrar_string(strings[7],60)
    o_que_y = 820
    for i in range((len(lista_o_que))):
    
        draw.text((350, o_que_y), lista_o_que[i], font=firstFont, fill='black')
        o_que_y+=35


    lista_pra_que = quebrar_string(strings[8],60)
    pra_que_y = 980
    for i in range((len(lista_pra_que))):
    
        draw.text((350, pra_que_y), lista_pra_que[i], font=firstFont, fill='black')
        pra_que_y+=35


    lista_como = quebrar_string(strings[9],60)
    como_y = 1120
    for i in range((len(lista_como))):
        
        draw.text((350, como_y), lista_como[i], font=firstFont, fill='black')
        como_y+=35



    img.save("test-template.png", dpi=(300, 300))

    pdf_files = ['test-template.png', 'templates/other-1.png']

    pdf_writer = PyPDF2.PdfWriter()

    for file_path in pdf_files:
        if file_path.endswith('.pdf'):
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
        elif file_path.endswith('.png'):
            image = Image.open(file_path)
            pdf_path = f"{file_path}.pdf"
            image.save(pdf_path, "PDF", resolution=200)  
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
            os.remove(pdf_path)

    current_date = datetime.now().strftime("%d_%m_%Y")
    output_folder = "ABRIR/fichas"
    file_name = f"FICHA-{strings[1]}-{datetime.now().strftime('%Y-%m-%d')}.pdf"
    output_path = os.path.join(output_folder, file_name)


    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    os.startfile(output_path)


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

etapa_label = ttk.Label(user_info_frame, text="Etapa:", font=("Arial", 12, "bold"))
etapa_label.grid(row=0, column=0, padx=5, pady=5)
etapa_combobox = ttk.Combobox(user_info_frame, values=["Definir", "Descobrir", "Desenvolver", "Entregar"], state="readonly")
etapa_combobox.grid(row=0, column=1, padx=5, pady=5)

numero_atividade_label = ttk.Label(user_info_frame, text="Número de Atividade:", font=("Arial", 12, "bold"))
numero_atividade_label.grid(row=0, column=2, padx=5, pady=5)
numero_atividade_entry = ttk.Entry(user_info_frame, font=("Arial", 10))
numero_atividade_entry.grid(row=0, column=3, padx=5, pady=5)

materia_label = ttk.Label(user_info_frame, text="Matéria:", font=("Arial", 12, "bold"))
materia_label.grid(row=1, column=0, padx=5, pady=5)
materia_entry = ttk.Entry(user_info_frame, font=("Arial", 10))
materia_entry.grid(row=1, column=1, padx=5, pady=5)

turma_label = ttk.Label(user_info_frame, text="Turma/Ano:", font=("Arial", 12, "bold"))
turma_label.grid(row=1, column=2, padx=5, pady=5)
turma_entry = ttk.Entry(user_info_frame, font=("Arial", 10))
turma_entry.grid(row=1, column=3, padx=5, pady=5)

sequencia_label = ttk.Label(user_info_frame, text="Sequência:", font=("Arial", 12, "bold"))
sequencia_label.grid(row=2, column=0, padx=5, pady=5)
sequencia_entry = ttk.Entry(user_info_frame, font=("Arial", 10))
sequencia_entry.grid(row=2, column=1, padx=5, pady=5)

conteudo_label = ttk.Label(user_info_frame, text="Conteúdo:", font=("Arial", 12, "bold"))
conteudo_label.grid(row=2, column=2, padx=5, pady=5)
conteudo_entry = ttk.Entry(user_info_frame, font=("Arial", 10))
conteudo_entry.grid(row=2, column=3, padx=5, pady=5)

quinzenario_label = ttk.Label(user_info_frame, text="Quinzenário:", font=("Arial", 12, "bold"))
quinzenario_label.grid(row=3, column=0, padx=5, pady=5)
quinzenario_entry = ttk.Entry(user_info_frame, font=("Arial", 10))
quinzenario_entry.grid(row=3, column=1, padx=5, pady=5)

# Caixas de texto
text_frame = ttk.LabelFrame(frame, text="Informações Adicionais")
text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

o_que_label = ttk.Label(text_frame, text="O QUE?", font=("Arial", 12, "bold"))
o_que_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

o_que_text = tk.Text(text_frame, height=2, bg="white", font=("Arial", 10), wrap='word')
o_que_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

pra_que_label = ttk.Label(text_frame, text="PRA QUÊ?", font=("Arial", 12, "bold"))
pra_que_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

pra_que_text = tk.Text(text_frame, height=2, bg="white", wrap = 'word', font=("Arial", 10))
pra_que_text.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

como_label = ttk.Label(text_frame, text="COMO?", font=("Arial", 12, "bold"))
como_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

como_text = tk.Text(text_frame, height=2, bg="white", wrap = 'word', font=("Arial", 10))
como_text.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

instrucoes_label = ttk.Label(text_frame, text="INTRUÇÕES:", font=("Arial", 12, "bold"))
instrucoes_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")

instrucoes_text = tk.Text(text_frame, height=8, bg="white", wrap = 'word', font=("Arial", 10))
instrucoes_text.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

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
