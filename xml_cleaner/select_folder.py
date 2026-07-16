from pathlib import Path
import tkinter as tk
from tkinter import filedialog


def selecionar_pasta() -> Path:

    root = tk.Tk()
    root.withdraw()

    pasta = filedialog.askdirectory(
        title="Selecione a pasta contendo os XMLs"
    )

    if not pasta:
        raise Exception("Nenhuma pasta selecionada.")

    return Path(pasta)