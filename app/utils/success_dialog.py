import customtkinter

class SuccessDialog(customtkinter.CTkToplevel):
    def __init__(self, message: str, geometry: str, title: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(geometry)
        self.title(title)

        self.resizable(False, False)

        label = customtkinter.CTkLabel(self, text=message)
        label.pack(padx=2, pady=3)

        btn = customtkinter.CTkButton(self, text="Certo", command=self.okay)
        btn.pack(padx=20, pady=10)
    
    def okay(self):
        self.destroy()

        