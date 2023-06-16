import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

# Crie a janela principal
window = ThemedTk(theme="breeze")  # Especifique o nome do tema
window.title("Preenchedor de ficha")

frame = ttk.Frame(window)
frame.pack(padx=20, pady=10)

# Informações do usuário
user_info_frame = ttk.LabelFrame(frame, text="")
user_info_frame.grid(row=1, column=0, padx=20, pady=10)

materia_label = ttk.Label(user_info_frame, text="Matéria", font=("Arial", 12, "bold"))
materia_label.grid(row=0, column=0, padx=5, pady=5)
materia_entry = ttk.Entry(user_info_frame)
materia_entry.grid(row=0, column=1, padx=5, pady=5)

turma_label = ttk.Label(user_info_frame, text="Turma/Ano", font=("Arial", 12, "bold"))
turma_label.grid(row=1, column=0, padx=5, pady=5)
turma_entry = ttk.Entry(user_info_frame)
turma_entry.grid(row=1, column=1, padx=5, pady=5)

sequencia_label = ttk.Label(user_info_frame, text="Sequência", font=("Arial", 12, "bold"))
sequencia_label.grid(row=0, column=2, padx=5, pady=5)
sequencia_entry = ttk.Entry(user_info_frame)
sequencia_entry.grid(row=0, column=3, padx=5, pady=5)

conteudo_label = ttk.Label(user_info_frame, text="Conteúdo", font=("Arial", 12, "bold"))
conteudo_label.grid(row=1, column=2, padx=5, pady=5)
conteudo_entry = ttk.Entry(user_info_frame)
conteudo_entry.grid(row=1, column=3, padx=5, pady=5)

etapa_label = ttk.Label(user_info_frame, text="Etapa", font=("Arial", 12, "bold"))
etapa_label.grid(row=2, column=0, padx=5, pady=5)
etapa_combobox = ttk.Combobox(user_info_frame, values=["Definir", "Investigar", "Desenvolver", "Descobrir"])
etapa_combobox.grid(row=2, column=1, padx=5, pady=5)

numero_atividade_label = ttk.Label(user_info_frame, text="Número de Atividade", font=("Arial", 12, "bold"))
numero_atividade_label.grid(row=2, column=2, padx=5, pady=5)
numero_atividade_entry = ttk.Entry(user_info_frame)
numero_atividade_entry.grid(row=2, column=3, padx=5, pady=5)

quinzenario_label = ttk.Label(user_info_frame, text="Quinzenário", font=("Arial", 12, "bold"))
quinzenario_label.grid(row=3, column=0, padx=5, pady=5)
quinzenario_entry = ttk.Entry(user_info_frame)
quinzenario_entry.grid(row=3, column=1, padx=5, pady=5)

# Caixas de texto
text_frame = ttk.LabelFrame(frame, text="Informações Adicionais")
text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

o_que_label = ttk.Label(text_frame, text="O QUE:", font=("Arial", 12, "bold"))
o_que_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

o_que_text = tk.Text(text_frame, height=2)
o_que_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

pra_que_label = ttk.Label(text_frame, text="PRA QUÊ?", font=("Arial", 12, "bold"))
pra_que_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

pra_que_text = tk.Text(text_frame, height=2)
pra_que_text.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

como_label = ttk.Label(text_frame, text="COMO?", font=("Arial", 12, "bold"))
como_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

como_text = tk.Text(text_frame, height=2)
como_text.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

# Crie o botão "CRIAR"
criar_button = ttk.Button(frame, text="CRIAR", command=criar)
criar_button.grid(row=3, column=0, padx=20, pady=10, sticky="se")

# Configuração da grade
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)
text_frame.grid_columnconfigure(0, weight=1)

window.mainloop()
