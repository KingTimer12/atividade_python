from utils import FloatSpinbox, insert
import customtkinter

def component_spinbox(app, text, box):
    label = customtkinter.CTkLabel(app, text=text)
    label.pack(padx=2, pady=3)
    box.pack(padx=20, pady=2)
    box.set(0)

class InsertWin(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x340")
        self.title('Inserir Aluno e Nota')

        self.resizable(False, False)

        self.av1 = FloatSpinbox(self, width=150, step_size=1)
        self.av2 = FloatSpinbox(self, width=150, step_size=1)
        self.av3 = FloatSpinbox(self, width=150, step_size=1)

        self.name = customtkinter.CTkEntry(self, width=150, height=32, placeholder_text="Nome do Aluno")
        self.name.pack(padx=20, pady=10)
        component_spinbox(self, 'Nota AV1', self.av1)
        component_spinbox(self, 'Nota AV2', self.av2)
        component_spinbox(self, 'Nota AV3', self.av3)

        btn = customtkinter.CTkButton(self, text="Registrar", command=self.insert)
        btn.pack(padx=20, pady=10)
    
    def insert(self):
        insert(self.name.get(), [self.av1.get(), self.av2.get(), self.av3.get()])
        self.destroy()

        