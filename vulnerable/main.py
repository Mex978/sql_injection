import sqlite3

if __name__ == '__main__':
    print("Olá!")
    # conectando...
    conn = sqlite3.connect('usuarios.db')
    # definindo um cursor
    cursor = conn.cursor()

    # criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE usuarios (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            senha TEXT NOT NULL
    );
    """)

    print('Tabela criada com sucesso.')
    # desconectando...
    conn.close()
