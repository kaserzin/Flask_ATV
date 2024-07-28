import sqlite3



class Atleta:
    def criar():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volei(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                posicao VARCHAR(3) NOT NULL,
                altura REAL NOT NULL);
        """)
        conn.close()

    def novo_atleta(nome, posicao, altura):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO volei(nome, posicao, altura)
            VALUES(?, ?, ?);
        """, (nome, posicao, altura))
        conn.commit()
        conn.close()

    def listar_atleta():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM volei")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'posicao': row[2],
                'altura': row[3],
            })
        conn.close()
        return resultado

    def atualiza_atleta(id, nome, posicao, altura):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE volei
            SET nome=?, posicao=?, altura=?
            WHERE id=?;
        """, (nome, posicao, altura, id))
        conn.commit()
        conn.close()

    def remove_atleta(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM volei
            WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

    def detalha_atleta(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM volei
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
            'posicao': item[2],
            'altura': item[3],
        }

class Time:
    def criar():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS times(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL);
        """)
        conn.close()

    def novo_time(nome):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO times(nome)
            VALUES(?);
        """, (nome,))
        conn.commit()
        conn.close()

    def listar_time():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM times")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
            })
        conn.close()
        return resultado

    def atualiza_time(id, nome):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE times
            SET nome=?
            WHERE id=?;
        """, (nome, id))
        conn.commit()
        conn.close()

    def remove_time(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM times
            WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

    def detalha_time(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM times
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
        }

class Arbitro:
    def criar():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS arbitro(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                documento REAL NOT NULL);
        """)
        conn.close()

    def novo_arbitro(nome, documento):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO arbitro(nome, documento)
            VALUES(?, ?);
        """, (nome, documento,))
        conn.commit()
        conn.close()

    def listar_arbitro():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM arbitro")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
                'documento': row[2],
            })
        conn.close()
        return resultado

    def atualiza_arbitro(id, nome, documento):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE arbitro
            SET nome=?, documento=?
            WHERE id=?;
        """, (nome, documento, id))
        conn.commit()
        conn.close()

    def remove_arbitro(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM arbitro
            WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

    def detalha_arbitro(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM arbitro
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
            'documento': item[2],
        }

class Competição:
    def criar():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS competicao(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL);
        """)
        conn.close()

    def novo_competicao(nome):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO competicao(nome)
            VALUES(?);
        """, (nome,))
        conn.commit()
        conn.close()

    def listar_competicao():
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        values = cursor.execute("SELECT * FROM competicao")
        resultado = []
        for row in values:
            resultado.append({
                'id': row[0],
                'nome': row[1],
            })
        conn.close()
        return resultado

    def atualiza_competicao(id, nome):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE competicao
            SET nome=?
            WHERE id=?;
        """, (nome, id))
        conn.commit()
        conn.close()

    def remove_competicao(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM competicao
            WHERE id=?;
        """, (id,))
        conn.commit()
        conn.close()

    def detalha_competicao(id):
        conn = sqlite3.connect('volei.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM competicao
            WHERE id=?;
        """, (id,))
        item = cursor.fetchone()
        conn.close()
        if item is None:
            return None
        return {
            'id': item[0],
            'nome': item[1],
        }

if __name__ == '__main__':
    Atleta.criar()
    Time.criar()
    Arbitro.criar()
    Competição.criar()