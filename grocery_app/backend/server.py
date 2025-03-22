from flask import Flask, request, jsonify
from sql_connection import get_sql_connection

import products_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('getUOM', methods=['GET'])
def get_uom():
  response = uom_dao.get_uoms(connection)
  response = jsonify(response)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response


@app.route('/getProducts', methods=['GET'])
def get_products():
  products = products_dao.get_all_products(connection)
  response = jsonify(products)
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/deleteProduct', methods=[POST])
def delete_product():
  return_id = products_dao.delete_product(connection, request.form['product_id'])
  response = jasonify({
  'product_id': return_id
})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

if __name__ == "__main__":
  print("Stating Python Flask Server For Grocery Store Management System")
  app.run(port=5000)