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

def criar_tudo():
    strings = criar_primeira_pagina()
    criar_segunda_pagina()

    pdf_files = ['primeira-pagina.png', 'segunda-pagina.png']

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
    
    file_name = f"FICHA-{strings[1]}-{datetime.now().strftime('%d-%m_%Hh%M')}.pdf"
    output_path = os.path.join(output_folder, file_name)


    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    os.startfile(output_path)

def criar_primeira_pagina():

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
    lines = instrucoes.splitlines()

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
        if line.strip():

            wrapped_lines = textwrap.wrap(line, width=85) 

            for wrapped_line in wrapped_lines:
                draw.text((332, y), wrapped_line, font=firstFont, fill='black')
                y += firstFont.getbbox(wrapped_line)[1] + 35
            y+=35
        y += 35  
    messagebox.showinfo("Sucesso", "Arquivo criado com sucesso! Eles serão armazenados na pasta ABRIR > fichas")

    def wrap_text(text, width):
        return textwrap.wrap(text, width=width)

    wrapped_o_que = wrap_text(strings[7], 74)

    o_que_y = 820
    for line in wrapped_o_que:
        draw.text((350, o_que_y), line, font=firstFont, fill='black')
        o_que_y += 35

    wrapped_pra_que = wrap_text(strings[8], 74)

    pra_que_y = 980
    for line in wrapped_pra_que:
        draw.text((350, pra_que_y), line, font=firstFont, fill='black')
        pra_que_y += 35

    wrapped_como = wrap_text(strings[9], 74)

    como_y = 1120
    for line in wrapped_como:
        draw.text((350, como_y), line, font=firstFont, fill='black')
        como_y += 35




    img.save("primeira-pagina.png", dpi=(300, 300))

    return strings



def criar_segunda_pagina():
    url_font = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial.ttf?raw=True'
    normal_font = io.BytesIO(urlopen(url_font).read())
    normal_font.seek(0)
    firstFont = ImageFont.truetype(normal_font, 30)

    instrucoes2 = instrucoes_text2.get("1.0", "end")
    wrapped_instrucoes = textwrap.wrap(instrucoes2, width=50)
    lines = instrucoes2.splitlines()

    img = Image.open("templates/other-1.png")
    draw = ImageDraw.Draw(img)
    y=100
    wrapped_instrucoes = textwrap.wrap(instrucoes2, width=50)

    for line in lines:
        if line.strip():  
            wrapped_lines = textwrap.wrap(line, width=85)

            for wrapped_line in wrapped_lines:
                draw.text((332, y), wrapped_line, font=firstFont, fill='black')
                y += firstFont.getbbox(wrapped_line)[1] + 35
        y+=35
    y+=35
    
    img.save("segunda-pagina.png", dpi=(300, 300))



# Crie a janela principal
window = ThemedTk(theme="breeze") 
window.title("Preenchedor de ficha")


style = ttk.Style()
style.configure("RoundedEntry.TEntry", borderwidth=0, relief="solid", 
                foreground="black", background="white", font=("Arial", 12))


frame = ttk.Frame(window)
frame.pack(padx=20  )

# Informações do usuário
user_info_frame = ttk.LabelFrame(frame, text="")
user_info_frame.grid(row=1, column=0, padx=20, pady=(10,20))

etapa_label = ttk.Label(user_info_frame, text="Etapa:", font=("Arial", 12, "bold"))
etapa_label.grid(row=0, column=0, padx=5, pady=5)
etapa_combobox = ttk.Combobox(user_info_frame, values=["Descobrir", "Definir", "Desenvolver", "Entregar"], state="readonly")
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

def validate_input_como(event):
    text = como_text.get("1.0", "end-1c")  
    if len(text) > CHARACTER_LIMIT:
        
        truncated_text = text[:CHARACTER_LIMIT]
        como_text.delete("1.0", "end-1c")  
        como_text.insert("1.0", truncated_text)  
    return True


def validate_input_pra_que(event):
    text = pra_que_text.get("1.0", "end-1c")  
    if len(text) > CHARACTER_LIMIT:
        
        truncated_text = text[:CHARACTER_LIMIT]
        pra_que_text.delete("1.0", "end-1c")  
        pra_que_text.insert("1.0", truncated_text)  
    return True


def validate_input_o_que(event):
    text = o_que_text.get("1.0", "end-1c")  
    if len(text) > CHARACTER_LIMIT:
        
        truncated_text = text[:CHARACTER_LIMIT]
        o_que_text.delete("1.0", "end-1c")  
        o_que_text.insert("1.0", truncated_text)  
    return True


#---------------------------------------------------------------------------------

MAX_LINES_INSTRUCOES = 7
CHARACTER_LIMIT= 600
# dsdsdsd 
def validate_input_instrucoes(event):
    lines = instrucoes_text.get("1.0", "end-1c").split('\n')
    characters = len(instrucoes_text.get("1.0", "end-1c"))
    current_line = int(instrucoes_text.index("insert").split('.')[0])

    if len(lines) > MAX_LINES_INSTRUCOES or characters > CHARACTER_LIMIT:
        
        if len(lines) > MAX_LINES_INSTRUCOES:
            instrucoes_text.delete(f"{current_line}.0", "end")

        
        if characters > CHARACTER_LIMIT:
            instrucoes_text.delete("end-2c")

        
        instrucoes_text.config(state="disabled")
        messagebox.showinfo("Limite!", "Você chegou ao limite da primeira página. Para dar continuação, use a caixa de texto abaixo.")

    else:
        instrucoes_text.config(state="normal")  

    return True

def validate_paste_instrucoes(event):
    pasted_text = event.widget.selection_get(selection="CLIPBOARD")
    lines = instrucoes_text.get("1.0", "end-1c").split('\n')
    characters = len(instrucoes_text.get("1.0", "end-1c"))
    total_lines = len(lines) + pasted_text.count('\n')
    total_characters = characters + len(pasted_text)

    if total_lines > MAX_LINES_INSTRUCOES or total_characters > CHARACTER_LIMIT:
        # Display a warning message
        messagebox.showinfo("Limit Exceeded", "Pasted text exceeds the line or character limit.")
        return "break"  # Prevent the paste operation

    # Perform the regular input validation
    validate_input_instrucoes(event)
#-----------------------#-----------------------#-----------------------#-----------------------#-----------------------
MAX_LINES_INSTRUCOES_SECOND_PAGE = 24
CHARACTER_LIMIT_SECOND_PAGE = 1400
# dsdsdsd 
def validate_input_instrucoes_second_page(event):
    lines = instrucoes_text2.get("1.0", "end-1c").split('\n')
    characters = len(instrucoes_text2.get("1.0", "end-1c"))
    current_line = int(instrucoes_text2.index("insert").split('.')[0])

    if len(lines) > MAX_LINES_INSTRUCOES_SECOND_PAGE or characters > CHARACTER_LIMIT_SECOND_PAGE:
        
        if len(lines) > MAX_LINES_INSTRUCOES_SECOND_PAGE:
            instrucoes_text2.delete(f"{current_line}.0", "end")

        
        if characters > CHARACTER_LIMIT_SECOND_PAGE:
            instrucoes_text2.delete("end-2c")

        
        instrucoes_text2.config(state="disabled")
        messagebox.showinfo("Limite!", "Você chegou ao limite da primeira página. Para dar continuação, use a caixa de texto abaixo.")

    else:
        instrucoes_text2.config(state="normal")  

    return True

def validate_paste_instrucoes_second_page(event):
    pasted_text = event.widget.selection_get(selection="CLIPBOARD")
    lines = instrucoes_text2.get("1.0", "end-1c").split('\n')
    characters = len(instrucoes_text2.get("1.0", "end-1c"))
    total_lines = len(lines) + pasted_text.count('\n')
    total_characters = characters + len(pasted_text)

    if total_lines > MAX_LINES_INSTRUCOES_SECOND_PAGE or total_characters > CHARACTER_LIMIT_SECOND_PAGE:
        # Display a warning message
        messagebox.showinfo("Limit Exceeded", "Pasted text exceeds the line or character limit.")
        return "break"  # Prevent the paste operation

    # Perform the regular input validation
    validate_input_instrucoes_second_page(event)

#-----------------------#-----------------------#-----------------------#-----------------------#-----------------------





def set_character_limit(limit):
    global CHARACTER_LIMIT
    CHARACTER_LIMIT = limit

 
text_frame = ttk.LabelFrame(frame, text="Informações Adicionais")
text_frame.grid(row=2, column=0, padx=20, pady=(10,5), sticky="nsew")

o_que_label = ttk.Label(text_frame, text="O QUE?", font=("Arial", 12, "bold"))
o_que_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

o_que_text = tk.Text(text_frame, height=3, bg="white", font=("Arial", 10), wrap='word')
o_que_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

pra_que_label = ttk.Label(text_frame, text="PRA QUÊ?", font=("Arial", 12, "bold"))
pra_que_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

pra_que_text = tk.Text(text_frame, height=3, bg="white", wrap = 'word', font=("Arial", 10))
pra_que_text.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

como_label = ttk.Label(text_frame, text="COMO?", font=("Arial", 12, "bold"))
como_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

como_text = tk.Text(text_frame, height=4, bg="white", wrap = 'word', font=("Arial", 10))
como_text.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

instrucoes_label = ttk.Label(text_frame, text="INTRUÇÕES (primeira página):", font=("Arial", 12, "bold"))
instrucoes_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")

instrucoes_text = tk.Text(text_frame, height=5, bg="white", wrap = 'word', font=("Arial", 10))
instrucoes_text.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")
instrucoes_text.bind("<Key>", validate_input_instrucoes)
instrucoes_text.bind("<KeyRelease>", validate_input_instrucoes)
instrucoes_text.bind("<Control-v>", validate_paste_instrucoes)

instrucoes_label2 = ttk.Label(text_frame, text="INTRUÇÕES (segunda página):", font=("Arial", 12, "bold"))
instrucoes_label2.grid(row=2, column=4, padx=5, pady=5, sticky="w")

instrucoes_text2 = tk.Text(text_frame, height=5, bg="white", wrap = 'word', font=("Arial", 10))
instrucoes_text2.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")
instrucoes_text2.bind("<Key>", validate_input_instrucoes_second_page)
instrucoes_text2.bind("<KeyRelease>", validate_input_instrucoes_second_page)
instrucoes_text2.bind("<Control-v>", validate_paste_instrucoes_second_page)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

sair_button = tk.Button(button_frame, text="SAIR", command=sair, bg="#ff474c", relief="solid", bd=0)
sair_button.pack(side="left", padx=10)

criar_button = tk.Button(button_frame, text="CRIAR", command=criar_tudo, bg="#90EE90", relief="solid", bd=0)
criar_button.pack(side="left", padx=10)


instrucoes_text.bind("<KeyPress>", validate_input_instrucoes)
instrucoes_text.bind("<KeyRelease>", validate_input_instrucoes)

instrucoes_text2.bind("<KeyPress>", validate_input_instrucoes_second_page)
instrucoes_text2.bind("<KeyRelease>", validate_input_instrucoes_second_page)


como_text.bind("<KeyPress>", validate_input_como)
como_text.bind("<KeyRelease>", validate_input_como)

pra_que_text.bind("<KeyPress>", validate_input_pra_que)
pra_que_text.bind("<KeyRelease>", validate_input_pra_que)

o_que_text.bind("<KeyPress>", validate_input_o_que)
o_que_text.bind("<KeyRelease>", validate_input_o_que)


frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)
text_frame.grid_columnconfigure(0, weight=1)

window.mainloop()
