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

def verifica_limite_v2():
    instrucoes = instrucoes_text.get("1.0", "end")
    num_chars = len(instrucoes)
    num_linebreaks = len(instrucoes.splitlines()) - 1  # Subtract 1 for the last line
    num_lines = num_chars // 65 + num_linebreaks
 
    if num_lines > 18:
        messagebox.showwarning("Limite atingido!", "Foi estimado que você atingiu o limite do primeiro bloco de instruções! Para continuar, use o segund bloco")

        
    
 
    instrucoes2 = instrucoes_text2.get("1.0", "end")
    num_chars2 = len(instrucoes2)
    num_linebreaks2 = len(instrucoes2.splitlines()) - 1  # Subtract 1 for the last line
    num_lines2 = num_chars2 // 65 + num_linebreaks2

    if num_lines2 > 65:
        messagebox.showwarning("Limite de linhas excedido para o segundo bloco de Instruções", "O texto inserido para as instruções da segunda página pode exceder o limite de linhas. Por favor, revise o texto.")

        


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
    instrucoes = instrucoes_text.get("1.0", "end").strip()
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

    wrapped_lines = []
    max_width = 80
    y = 1363
    for line in lines:
        if line.strip():
            wrapped_lines = textwrap.wrap(line, width=max_width)
            for wrapped_line in wrapped_lines:
                draw.text((332, y), wrapped_line, font=firstFont, fill='black')
                y += firstFont.getbbox(wrapped_line)[1] + 35
              # Add extra spacing between wrapped lines
        else:
            y += firstFont.getsize(" ")[1] + 35  # Adjust the vertical spacing for empty lines




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
    """
    for line in lines:
        if line.strip():

            wrapped_lines = textwrap.wrap(line, width=80) 

            for wrapped_line in wrapped_lines:
                draw.text((332, y), wrapped_line, font=firstFont, fill='black')
                y += firstFont.getbbox(wrapped_line)[1] + 35
            
         
    messagebox.showinfo("Sucesso", "Arquivo criado com sucesso! Eles serão armazenados na pasta ABRIR > fichas")
"""
    def wrap_text(text, width):
        return textwrap.wrap(text, width=width)
    
    wrapped_o_que = wrap_text_with_line_breaks(strings[7], 74)

    o_que_y = 820
    for line in wrapped_o_que:
        draw.text((350, o_que_y), line, font=firstFont, fill='black')
        o_que_y += 35

    wrapped_pra_que = wrap_text_with_line_breaks(strings[8], 74)

    pra_que_y = 980
    for line in wrapped_pra_que:
        draw.text((350, pra_que_y), line, font=firstFont, fill='black')
        pra_que_y += 35

    wrapped_como = wrap_text_with_line_breaks(strings[9], 74)

    como_y = 1120
    for line in wrapped_como:
        draw.text((350, como_y), line, font=firstFont, fill='black')
        como_y += 35


    img.save("primeira-pagina.png", dpi=(300, 300))

    return strings

def wrap_text_with_line_breaks(text, width):
    lines = text.split('\n')
    wrapped_lines = []

    for line in lines:
        if line.strip():
            wrapped = textwrap.wrap(line, width=width)
            wrapped_lines.extend(wrapped)
            wrapped_lines.append('sd')  # Add an empty line for each line break

    return wrapped_lines


import textwrap
def criar_segunda_pagina():
    url_font = 'https://github.com/matomo-org/travis-scripts/blob/master/fonts/Arial.ttf?raw=True'
    normal_font = io.BytesIO(urlopen(url_font).read())
    normal_font.seek(0)
    firstFont = ImageFont.truetype(normal_font, 30)

    instrucoes2 = instrucoes_text2.get("1.0", "end-1c")
    lines2 = instrucoes2.split("\n")
    max_width = 80  # Adjust the maximum width based on your requirements

    img = Image.open("templates/other-1.png")
    draw = ImageDraw.Draw(img)
    y = 100
    for line in lines2:
        if line.strip():
            wrapped_lines = textwrap.wrap(line, width=max_width)
            for wrapped_line in wrapped_lines:
                draw.text((350, y), wrapped_line, font=firstFont, fill='black')
                y += firstFont.getbbox(wrapped_line)[1] + 35
             # Add extra spacing between wrapped lines
        else:
            y += firstFont.getsize(" ")[1] + 35  # Adjust the vertical spacing for empty lines


    img.save("segunda-pagina.png", dpi=(300, 300))


def wrap_text(text, max_width, font):
    words = text.split()
    if not words:
        return []
    lines = []
    current_line = words[0]
    for word in words[1:]:
        if font.getsize(current_line + ' ' + word)[0] <= max_width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    return lines

window = ThemedTk(theme="breeze") 
window.title("Preenchedor de ficha")


style = ttk.Style()
style.configure("RoundedEntry.TEntry", borderwidth=0, relief="solid", 
                foreground="black", background="white", font=("Arial", 12))


frame = ttk.Frame(window)
frame.pack(padx=20  )


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


#-----------------------#-----------------------#-----------------------#-----------------------#-----------------------

def validate_input_generico(event, input_widget, max_lines, max_characters):
    if event.keysym == "BackSpace":
        return None
    
    verifica_limite_v2()
    if event.widget == input_widget:
        text = input_widget.get("1.0", "end-1c")
        lines = text.split('\n')
        characters = len(text)

        if len(lines) > max_lines or characters > max_characters:
            if event.keysym == "BackSpace":
                return None  

            messagebox.showinfo("Limite!", "Você chegou ao limite da primeira página. Para dar continuação, use a caixa de texto abaixo.")
            return "break"  

    return None


def validate_paste_generico(event, input_widget, max_characters):
    pasted_text = event.widget.clipboard_get()
    if len(pasted_text) > max_characters:
        messagebox.showinfo("Limite!", "O texto colado excede o limite.")
        return "break"  
    else:
        return None

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

instrucoes_label = ttk.Label(text_frame, text="INSTRUÇÕES (primeira página):", font=("Arial", 12, "bold"))
instrucoes_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")

instrucoes_text = tk.Text(text_frame, height=5, bg="white", wrap = 'word', font=("Arial", 10))
instrucoes_text.grid(row=1, column=4, padx=5, pady=5, sticky="nsew")


instrucoes_label2 = ttk.Label(text_frame, text="INSTRUÇÕES (segunda página):", font=("Arial", 12, "bold"))
instrucoes_label2.grid(row=2, column=4, padx=5, pady=5, sticky="w")

instrucoes_text2 = tk.Text(text_frame, height=5, bg="white", wrap = 'word', font=("Arial", 10))
instrucoes_text2.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

sair_button = tk.Button(button_frame, text="SAIR", command=sair, bg="#ff474c", relief="solid", bd=0)
sair_button.pack(side="left", padx=10)

criar_button = tk.Button(button_frame, text="CRIAR", command=criar_tudo, bg="#90EE90", relief="solid", bd=0)
criar_button.pack(side="left", padx=10)

instrucoes_text.bind("<Key>", lambda event: validate_input_generico(event, instrucoes_text, 40, 1300))
instrucoes_text.bind("<KeyRelease>", lambda event: validate_input_generico(event, instrucoes_text, 40, 1300))
instrucoes_text.bind("<Control-v>", lambda event: validate_paste_generico(event, instrucoes_text, 1300))

instrucoes_text2.bind("<Key>", lambda event: validate_input_generico(event, instrucoes_text2, 65, 4000))
instrucoes_text2.bind("<KeyRelease>", lambda event: validate_input_generico(event, instrucoes_text2,65, 4000))
instrucoes_text2.bind("<Control-v>", lambda event: validate_paste_generico(event, instrucoes_text2, 4000))


como_text.bind("<Key>", lambda event: validate_input_generico(event, como_text, 2, 200))
como_text.bind("<KeyRelease>", lambda event: validate_input_generico(event, como_text, 2, 200))
como_text.bind("<Control-v>", lambda event: validate_paste_generico(event, como_text, 200))

pra_que_text.bind("<Key>", lambda event: validate_input_generico(event, pra_que_text, 2, 200))
pra_que_text.bind("<KeyRelease>", lambda event: validate_input_generico(event, pra_que_text, 2, 200))
pra_que_text.bind("<Control-v>", lambda event: validate_paste_generico(event, pra_que_text, 200))

o_que_text.bind("<Key>", lambda event: validate_input_generico(event, o_que_text, 2, 200))
o_que_text.bind("<KeyRelease>", lambda event: validate_input_generico(event, o_que_text, 2, 200))
o_que_text.bind("<Control-v>", lambda event: validate_paste_generico(event, o_que_text, 200))


frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)
text_frame.grid_columnconfigure(0, weight=1)

window.mainloop()
