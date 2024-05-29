from CTkTable import * # type: ignore
from utils import fetch

import customtkinter

def component_spinbox(app, text, box):
    label = customtkinter.CTkLabel(app, text=text)
    label.pack(padx=2, pady=3)
    box.pack(padx=20, pady=2)
    box.set(0)

class ListWin(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = fetch()
        if result is None:
            return
        height = 200 + (min(len(result)*10, 720))
        self.geometry(f"400x{height}")
        self.title('Informações')

        
        value = [["ID", "Nome", "Situação", "Média", "Notas"]]
        for data in result:
            id = data["id"]
            situacao = "Aprovado" if float(data["media"]) >= 7 else "Reprovado"
            nome = data["nome"]
            notas = ','.join(data["notas"])
            media = data["media"]
            value.append([id, nome, situacao, media, notas])

        table = CTkTable(master=self, row=len(value), column=5, values=value)
        table.pack(expand=True, fill="both", padx=20, pady=20)
    
    def insert(self):
        self.destroy()

        