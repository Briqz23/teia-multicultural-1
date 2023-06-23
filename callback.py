import tkinter as tk
from tkinter import ttk

def validate_input(event):
    text = como_text.get("1.0", "end-1c")  # Get the text from the widget
    if len(text) > character_limit:
        # Truncate the text to the character limit
        truncated_text = text[:character_limit]
        como_text.delete("1.0", "end-1c")  # Clear the widget
        como_text.insert("1.0", truncated_text)  # Insert the truncated text
    return True

def set_character_limit(limit):
    global character_limit
    character_limit = limit

window = tk.Tk()

character_limit = 10  # Set the default character limit

text_frame = ttk.Frame(window)
text_frame.pack()

como_label = ttk.Label(text_frame, text="COMO?", font=("Arial", 12, "bold"))
como_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

como_text = tk.Text(text_frame, height=2, bg="white", wrap='word', font=("Arial", 10))
como_text.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

submit_button = ttk.Button(text_frame, text="Submit")
submit_button.grid(row=6, column=0, padx=5, pady=5)

def submit_input():
    text = como_text.get("1.0", "end-1c")
    print("Submitted text:", text)

submit_button.config(command=submit_input)

# Bind the key press and key release events to the validation function
como_text.bind("<KeyPress>", validate_input)
como_text.bind("<KeyRelease>", validate_input)

window.mainloop()
