import sqlite3
import os
import npyscreen


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def createDataBase():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("""
                CREATE TABLE usuarios (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        login TEXT NOT NULL,
                        senha TEXT NOT NULL
                );
                """)

    print('Tabela criada com sucesso.')
    conn.close()


def insertUser(cursor, username, password):
    sql_command = f"""
        INSERT INTO usuarios(login, senha) 
        VALUES({username}, {password})"""
    try:
        cursor.execute(sql_command)
        return True
    except Exception as e:
        return False


def selectUser(cursor, username, password):
    sql_command = f"""
        SELECT * 
        FROM usuarios 
        WHERE login={username} AND senha={password}"""
    try:
        cursor.execute(sql_command)
        return True
    except Exception as e:
        return False


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


def userLogingFail():
    print("Usuário e/ou Senha inválido(s)")


def userRegisterSuccess():
    print("Usuário logado com sucesso!")


def userRegisterFail():
    print("Ocorreu algum erro no processo!")


def menu():
    print("#=========================#")
    print("| 1 - Login               | ")
    print("| 2 - Register            | ")
    print("#=========================#")
    resp = input("Digite uma opçao>> ")
    return resp


if __name__ == '__main__':
    if not dataBaseExists():
        createDataBase()
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    resp = -1
    while resp != "0":
        clear()
        resp = menu()
        if resp == "1":
            user, passw = getUserCredential()
            if selectUser(cursor, user, passw):
                userLogingSuccess()
            else:
                userLogingFail()
            break
            input()
        elif resp == "2":
            user, passw = getUserCredential()
            if insertUser(cursor, user, passw):
                userRegisterSuccess()
            else:
                userRegisterFail()
            input()
        else:
            print("Opção inválida!")
            input()

    conn.close()
