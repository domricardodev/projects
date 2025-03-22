# Data Access Object

# Importa o módulo mysql.connector, que permite a conexão e interação com um banco de dados MySQL.
import mysql.connector

# Estabelece uma conexão com o banco de dados MySQL.
# Parâmetros:
# - user: o nome do usuário do banco de dados (neste caso, 'root').
# - password: a senha do usuário (neste caso, 'Alpine@187').
# - host: o endereço do servidor do banco de dados (neste caso, '127.0.0.1', que significa localhost).
# - database: o nome do banco de dados que será utilizado (neste caso, 'grocery_store').
cnx = mysql.connector.connect(user='root', password='Alpine@187',
                              host='127.0.0.1',
                              database='grocery_store')

# Cria um cursor. O cursor é um objeto que permite executar comandos SQL no banco de dados
# e recuperar os resultados das consultas.
cursor = cnx.cursor()

# Define a consulta SQL que será executada no banco de dados.
# Neste caso, a consulta seleciona todas as colunas (*) da tabela 'orders_table' no banco de dados 'grocery_store'.
query = "SELECT * FROM grocery_store.uom_table"

# Executa a consulta SQL definida na variável 'query'.
# O comando SQL é enviado ao banco de dados, e o resultado é armazenado no cursor.
cursor.execute(query)

# Itera sobre os resultados retornados pela consulta SQL.
# O cursor contém os dados retornados pela consulta, e o loop 'for' percorre cada linha do resultado.
# Neste caso, cada linha é armazenada na variável 'name' (que pode ser renomeada para algo mais descritivo, como 'row').
for (uom_id, uom_name) in cursor:
    print(uom_id, uom_name) 

# Fecha a conexão com o banco de dados.
# É uma boa prática fechar a conexão após o uso para liberar recursos do servidor.
cnx.close()