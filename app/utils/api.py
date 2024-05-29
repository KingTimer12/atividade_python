import requests

def insert(nome: str, notas: list[int]):
    try:
        response = requests.post("http://localhost:5000/notas", json={ 'nome': nome, 'notas': notas })
        return response.json()
    except:
        return None
    
def fetch(nome: str = None):
    try:
        response = requests.get(f"http://localhost:5000/notas{f'?nome={nome}' if nome is not None else ''}")
        return response.json()
    except:
        return None
    
def delete(nome: str = None):
    try:
        response = requests.delete(f"http://localhost:5000/notas{f'?nome={nome}' if nome is not None else ''}")
        return response.json()
    except:
        return None