# Gerador de fichas

Projeto feito para a escola Teia Multicultural para auxiliar o trabalho dos professores.


## Gerar o .exe
.

```bash
pip install pyinstaller
pip install Pil
pip install PyPDF2
pip install Tkinter

pyinstaller --noconfirm --onedir --windowed --add-data "PATH/TO/teia-multicultural-1/templates;templates/" --add-data "PATH/TO/teia-multicultural-1/FICHAS;FICHAS/"  "PATH/TO/teia-multicultural-1/script-preencher.py"

```
