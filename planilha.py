import tkinter as tk
from tkinter import filedialog


def escolherplanilha():
    # Função para abrir a janela do gerenciador de arquivos
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename()
    return file_path
