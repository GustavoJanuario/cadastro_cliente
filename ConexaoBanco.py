import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='#G121526g', database='login')
    print('Banco de dados acessado com sucesso!')
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print('Banco de dados não existe!')
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuário ou senha não encontrados!')
    else:
        print(error)
else:
    db_connection.close()