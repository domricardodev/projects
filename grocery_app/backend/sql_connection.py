
# Importa o módulo mysql.connector, que permite a conexão e interação com um banco de dados MySQL.
import mysql.connector

# Definindo variavel global de conexão
__cnx = None

def get_sql_connection():
    # Estabelece uma conexão com o banco de dados MySQL.
    # Parâmetros:
    # - user: o nome do usuário do banco de dados (neste caso, 'root').
    # - password: a senha do usuário (neste caso, 'Alpine@187').
    # - host: o endereço do servidor do banco de dados (neste caso, '127.0.0.1', que significa localhost).
    # - database: o nome do banco de dados que será utilizado (neste caso, 'grocery_store').

    global __cnx

    if __cnx is None:
      __cnx = mysql.connector.connect(user='root', password='Alpine@187',
                                host='127.0.0.1',
                                database='grocery_store')
    return __cnx