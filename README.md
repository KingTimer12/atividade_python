# Introdução

Esse repositório utiliza python como sua linguagem principal. Para pessoas preguiçosas, há um script em perl que cria o venv, instala as dependências e cria o diretório sqlite para o armazenamento.

Esse pequeno programa é separado em duas partes: API, uma simples RestAPI com create, read e delete utilizando Flask, e App, a GUI criada com CustomTkinter. Para que o App funciona corretamente, é necessário que API esteja rodando em conjunto. Não haverá script para isso.

O script, já mencionado anteriormente, está totalmente em português e com comentários deixados por mim, para aqueles que forem desconfiados e até paranóicos ter um pouco de paz. Se não for o suficiente, então vá estudar Perl ou apenas não use o script, sua presença é apenas para uma etapa: inicialização. Sem o script terá que criar um diretório storage com o arquivo: `data.sqlite`, além de criar o `venv` na mão.

# Bibliotecas
1. Flask: um framework bem conhecido e utilizado para criação de RestAPIs. Há também o FlaskCors que serve para adicionar cors a aplicação, sua presença é importante, pois existe alguns navegadores que não conseguem fazer uma requisição sem sua presença, por exemplo: Mozilla.
2. CustomTkinter: ele é vendido como a forma mais moderna do tkinter e de fato é, trazendo funcionalidades novas para aplicações GUI em Python. Seu uso, entretanto, nesse projeto foi apenas por erro meu, que esqueceu de fazer uma instalação na máquina, isso impediu o uso do tkinter, contudo foi resolvido e como já estava com CustomTkinter instalada, aproveitei para usa-lo mesmo. Essa biblioteca usa o tkinter como base, adicionando pequenas customizações gerais, como a facilidade de poder trocar o tema da aplicação.

# Instalação

## Com Perl:
1. Baixe perl em sua máquina, caso não tenha.
2. Execute o comando:
```bash
perl setup.pl
```

## Sem Perl:
1. Crie o diretório `storage`.
2. Logo em seguida o arquivo `data.sqlite`.
3. Use o comando python, por exemplo: `python3 -m venv venv`.
4. Ative o venv.
5. Instale as dependências executando o comando: `pip install -r requirements.txt`.