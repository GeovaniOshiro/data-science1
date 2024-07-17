import pandas as pd
import tkinter as tk
from tkinter import filedialog  
# import workbook
import openpyxl

def corregar():

   caminho = filedialog.askopenfilename(filetypes=[('Arquivos Excel', '*.xlsx'), ('Todos os arquivos', '*.*')])
   if caminho:
     file = openpyxl.load_workbook(caminho)
     planilha = file.active 
     lista = []
 
     for n in planilha.iter_rows(values_only=True):
         n_linhas = '\t'.join(str(celula) for celula in n) 
         lista.append(n_linhas)
         texto = "\n".join(lista)
         text.delete('1.0', tk.END)
         text.insert(tk.END, texto)

janela = tk.Tk()


btn = tk.Button(janela, text='carregar',command= corregar)
btn.grid(pady=30)

text = tk.Text(janela, width=100, height=50)
text.grid(pady=20, padx=20)

janela.mainloop()
