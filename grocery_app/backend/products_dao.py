# Data Access Object

from sql_connection import get_sql_connection

def get_all_products(connection):
    # O cursor é um objeto que permite executar comandos SQL e recuperar os resultados.
    # Ele age como uma "ponte" entre o Python e o banco de dados
    cursor = connection.cursor()

    # Define a consulta SQL que será executada no banco de dados.
    # Neste caso, a consulta seleciona todas as colunas (*) da tabela 'uom_table' no banco de dados 'grocery_store'.
    query = "SELECT products_table.product_id, products_table.name, products_table.uom_id, products_table.price_per_unit, uom_table.uom_name FROM grocery_store.products_table inner join grocery_store.uom_table on products_table.uom_id=uom_table.uom_id;"

    # Executa a consulta SQL definida na variável 'query'.
    # O comando SQL é enviado ao banco de dados, e o resultado é armazenado no cursor.
    cursor.execute(query)

    response = []

    # Itera sobre os resultados retornados pela consulta SQL.
    # O cursor contém os dados retornados pela consulta, e o loop 'for' percorre cada linha do resultado.
    # Neste caso, cada linha é armazenada na variável 'uom_id, uom_name' (que pode ser renomeada para algo mais descritivo, como 'row').
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
        {
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name,
        }
    ) 

    # Fecha a conexão com o banco de dados.
    # É uma boa prática fechar a conexão após o uso para liberar recursos do servidor.

    return response

if __name__=='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))