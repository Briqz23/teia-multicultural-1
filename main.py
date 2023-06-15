import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

def criar():
    # Get the filled text
    o_que_text_value = o_que_text.get("1.0", "end-1c")
    pra_que_text_value = pra_que_text.get("1.0", "end-1c")
    como_text_value = como_text.get("1.0", "end-1c")
    materia_entry_value = materia_entry.get()
    turma_entry_value = turma_entry.get()
    sequencia_entry_value = sequencia_entry.get()
    conteudo_entry_value = conteudo_entry.get()

    # Store the text in a list or perform any other desired action
    filled_text = [o_que_text_value, pra_que_text_value, como_text_value,
                   materia_entry_value, turma_entry_value, sequencia_entry_value,
                   conteudo_entry_value]
    print(filled_text)  # Example: Print the filled text

# Create the main window
window = ThemedTk(theme="breeze")  # Specify the theme name
window.title("Preenchedor de ficha")

frame = ttk.Frame(window)
frame.pack(padx=20, pady=10)

# Saving User Info
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

# Text Boxes
text_frame = ttk.LabelFrame(frame, text="Additional Information")
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

# Create the "CRIAR" button
criar_button = ttk.Button(frame, text="CRIAR", command=criar)
criar_button.grid(row=3, column=0, padx=20, pady=10, sticky="se")

# Grid Configuration
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)
text_frame.grid_columnconfigure(0, weight=1)

window.mainloop()
