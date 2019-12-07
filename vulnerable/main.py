import sqlite3
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def createDataBase():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        login TEXT NOT NULL,
                        senha TEXT NOT NULL
                );
                """)
    conn.commit()
    conn.close()


def insertUser(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT login FROM usuarios WHERE login=\"{username}\";
    """)
    content = cursor.fetchall()
    if len(content) > 0:
        raise Exception("Usuario já registrado!")
    sql_command = f"""
        INSERT INTO usuarios(login, senha) VALUES(\'{username}\', \'{password}\');
    """
    try:
        cursor.executescript(sql_command)
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()


def selectUser(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    sql_command = f"""
    SELECT * FROM usuarios WHERE login=\"{username}\" AND senha=\"{password}\";
    """
    try:
        cursor.execute(sql_command)
        content = cursor.fetchall()
        if len(content) <= 0:
            raise Exception("Usuário e/ou Senha inválido(s)")
        else:
            return False
        conn.close()
    except Exception as e:
        raise e


def dataBaseExists():
    if "usuarios.db" in os.listdir():
        return True
    else:
        return False


def getUserCredential():
    u = input("Username>> ")
    p = input("Password>> ")
    return u, p


def userLogingSuccess():
    print("Usuário logado com sucesso!")


def userRegisterSuccess():
    print("Usuário registrado com sucesso!")


def menu():
    print("#=========================#")
    print("| 1 - Login               | ")
    print("| 2 - Register            | ")
    print("#=========================#")
    resp = input("Digite uma opçao>> ")
    return resp


if __name__ == '__main__':
    if not dataBaseExists():
        print("veio")
        input()
    createDataBase()

    resp = -1
    while resp != "0":
        clear()
        resp = menu()
        if resp == "1":
            user, passw = getUserCredential()
            try:
                selectUser(user, passw)
                clear()
                userLogingSuccess()
                break
            except Exception as e:
                clear()
                print(e)
            input()
        elif resp == "2":
            user, passw = getUserCredential()
            try:
                insertUser(user, passw)
                clear()
                userRegisterSuccess()
            except Exception as e:
                clear()
                print(e)
            input()
        else:
            print("Opção inválida!")
            input()
