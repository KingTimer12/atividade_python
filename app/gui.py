import customtkinter
from win import InsertWin, ListWin
from utils import fetch, delete, SuccessDialog

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Controle de Notas")
        self.geometry(f"{300}x{200}")

        self.resizable(False, False)

        self.toplevel_window = None
        self.dialog = None

        self.init_buttons()
    
    def init_buttons(self):
        self.insert_btn = customtkinter.CTkButton(self, text="Inserir", command=self.insert_event)
        self.insert_btn.grid(row=1, column=10, padx=80, pady=10)

        self.list_btn = customtkinter.CTkButton(self, text="Listar", command=self.list_event)
        self.list_btn.grid(row=2, column=10, padx=80, pady=10)

        self.fetch_btn = customtkinter.CTkButton(self, text="Extrair", command=self.export_event)
        self.fetch_btn.grid(row=3, column=10, padx=80, pady=10)

        self.fetch_btn = customtkinter.CTkButton(self, text="Limpar", command=self.delete_event)
        self.fetch_btn.grid(row=4, column=10, padx=80, pady=10)

    def insert_event(self):
        if self.dialog and self.dialog.winfo_exists():
            return
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = InsertWin(self)
        else:
            self.toplevel_window.focus()

    def list_event(self):
        if self.dialog and self.dialog.winfo_exists():
            return
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ListWin(self)
        else:
            self.toplevel_window.focus()

    def export_event(self):
        if self.dialog and self.dialog.winfo_exists():
            return
        if self.toplevel_window is not None and self.toplevel_window.winfo_exists():
            self.toplevel_window.destroy()
        result = fetch()
        if result is None:
            return
        with open("export.txt", "w+") as file:
                for data in result:
                    id = data["id"]
                    media = "Aprovado" if float(data["media"]) >= 7 else "Reprovado"
                    nome = data["nome"]
                    notas = ','.join(data["notas"])
                    file.write(f"{id};{nome};{media};[{notas}]\n")
        self.dialog = SuccessDialog(message="Informações extraídas com sucesso!", geometry="280x100", title="Extraído com sucesso")
    
    def delete_event(self):
        if self.dialog and self.dialog.winfo_exists():
            return
        if self.toplevel_window is not None and self.toplevel_window.winfo_exists():
            self.toplevel_window.destroy()
        delete()
        self.dialog = SuccessDialog(message="Banco de dados limpado com sucesso!", geometry="280x100", title="Limpado com sucesso")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()