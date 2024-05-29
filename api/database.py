import sqlite3 as conn
from os import path, getcwd

dbpath = path.join(getcwd(), "storage", "data.sqlite")

def create_db():
  with conn.connect(dbpath) as cx:
    pessoas_query = """
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(99) NOT NULL
      );
    """
    notas_query = """
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pessoa_id INTEGER NOT NULL,
        nota INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(pessoa_id) REFERENCES pessoas(id) ON DELETE CASCADE
      );
    """
    cursor = cx.cursor()
    cursor.execute(pessoas_query)
    cursor.execute(notas_query)


def insert(data: tuple[str, list[int]]):
  pessoa = fetch_pessoa((data[0],))
  pessoa_id = insert_pessoa((data[0],)) if pessoa is None else pessoa[0]
  data: list[tuple[int, int]] = [(pessoa_id, nota) for nota in data[1]]
  insert_nota(data)

def insert_pessoa(data: tuple):
  with conn.connect(dbpath) as cx:
    query = "INSERT INTO pessoas (nome) VALUES (?);"
    cursor = cx.cursor()
    cursor.execute(query, data)
    return cursor.lastrowid

def insert_nota(data: list[tuple]):
  with conn.connect(dbpath) as cx:
    query = "INSERT INTO notas (pessoa_id, nota) VALUES (?,?);"
    cursor = cx.cursor()
    cursor.executemany(query, data)
    return cursor.lastrowid

def fetch_pessoa(data = ()):
  with conn.connect(dbpath) as cx:
    cursor = cx.cursor()
    query = "SELECT id FROM pessoas WHERE nome = ?;"
    cursor.execute(query, data)
    data = cursor.fetchone()
    return data

def fetch_all_notas():
  with conn.connect(dbpath) as cx:
    query = "SELECT * FROM notas;"
    cursor = cx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def fetch_all_pessoas():
  with conn.connect(dbpath) as cx:
    query = "SELECT * FROM pessoas;"
    cursor = cx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def fetch_all():
  with conn.connect(dbpath) as cx:
    query = """
    SELECT p.id, nome, PRINTF('%.1f', AVG(n.nota)), group_concat(n.nota)
    FROM pessoas p INNER JOIN notas n 
    ON p.id = n.pessoa_id
    GROUP BY p.id
    ORDER BY p.nome
    """
    cursor = cx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return [{
      'id': result[0],
      'nome': result[1],
      'media': result[2],
      'notas': str(result[3]).split(',')
    } for result in data]

def fetch_one(nome: str):
  with conn.connect(dbpath) as cx:
    query = """
    SELECT p.id, nome, PRINTF('%.1f', AVG(n.nota)), group_concat(n.nota)
    FROM pessoas p INNER JOIN notas n 
    ON p.id = n.pessoa_id
    WHERE p.nome = ?
    GROUP BY p.id
    ORDER BY p.nome
    """
    cursor = cx.cursor()
    cursor.execute(query, (nome,))
    data = cursor.fetchone()
    if data is None:
      return {}
    return {
      'id': data[0],
      'nome': data[1],
      'media': data[2],
      'notas': str(data[3]).split(',')
    }

def update(data = ()):
  with conn.connect(dbpath) as cx:
    query = "UPDATE contatos SET nome = ?, telefone = ? WHERE id = ?;"
    cursor = cx.cursor()
    cursor.execute(query, data)

def delete(data: tuple = None) -> bool:
  with conn.connect(dbpath) as cx:
    cursor = cx.cursor()
    if data is None:
      query = "DELETE FROM pessoas;"
      cursor.execute(query)
      query = "DELETE FROM notas;"
      cursor.execute(query)
      return

    query = "SELECT id FROM pessoas WHERE nome = ?;"
    cursor.execute(query, data)
    data = cursor.fetchone()
    if data is None:
      return False

    query = "DELETE FROM pessoas WHERE id = ?;"
    cursor.execute(query, data)

    query = "DELETE FROM notas WHERE pessoa_id = ?;"
    cursor.execute(query, data)
    return True

create_db()
# insert(("Lucas", 10))
# insert(("Pedro", 8))
# delete(("Pedro",))
