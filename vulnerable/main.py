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
                CREATE TABLE usuarios (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        login TEXT NOT NULL,
                        senha TEXT NOT NULL
                );
                """)
    conn.close()


def insertUser(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute(
        f"""SELECT login FROM usuarios WHERE login=\"{username}\";""")
    content = cursor.fetchall()
    if len(content) > 0:
        print("Usuario já registrado!")
        return False
    sql_command = f"""INSERT INTO usuarios(login, senha) VALUES(?,?);"""
    try:
        print(sql_command)
        cursor.execute(sql_command, (username, password))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return False


def selectUser(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    sql_command = f"""SELECT * FROM usuarios WHERE login=\"{username}\" AND senha=\"{password}\";"""
    try:
        cursor.execute(sql_command)
        content = cursor.fetchall()
        if len(content) > 0:
            return True
        else:
            return False
        conn.close()
        return True
    except Exception as e:
        print(e)
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
    print("Usuário registrado com sucesso!")


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
        print("veio")
        input()
        createDataBase()

    resp = -1
    while resp != "0":
        clear()
        resp = menu()
        if resp == "1":
            user, passw = getUserCredential()
            if selectUser(user, passw):
                clear()
                userLogingSuccess()
            else:
                clear()
                userLogingFail()
            break
            input()
        elif resp == "2":
            user, passw = getUserCredential()
            if insertUser(user, passw):
                clear()
                userRegisterSuccess()
            else:
                clear()
                userRegisterFail()
            input()
        else:
            print("Opção inválida!")
            input()
