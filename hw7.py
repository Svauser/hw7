import sqlite3
def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection
def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
def insert_products(connection):
    try:
        cursor = connection.cursor()
        products_data = [
            ('Стул 18', 1500.50, 400),
            ('Стол 18', 3000.75, 30),
            ('Кресло 18', 5000.99, 15),
            ('Полка 18', 1400.50, 200),
            ('Шкаф 18', 15000.75, 3),
            ('Тумбочка 18', 500.99, 150),
            ('Стул 410', 1500.50, 600),
            ('Стол 410', 3000.75, 50),
            ('Кресло 410', 5000.99, 15),
            ('Полка 410', 1400.50, 300),
            ('Шкаф 410', 11500.75, 8),
            ('Тумбочка 410', 500.99, 225),
            ('Ковер 1', 5000.99, 22),
            ('Ковер 18', 5000.99, 25),
            ('Ковер 410', 5000.99, 5),

        ]
        cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products_data)
        connection.commit()
        print("Products inserted successfully.")
    except sqlite3.Error as e:
        print(e)
def update_quantity(connection, product_id, new_quantity):
    try:
        cursor = connection.cursor()
        cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))
        connection.commit()
        print("Quantity updated successfully.")
    except sqlite3.Error as e:
        print(e)
def update_price(connection, product_id, new_price):
    try:
        cursor = connection.cursor()
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
        connection.commit()
        print("Price updated successfully.")
    except sqlite3.Error as e:
        print(e)

def delete_product(connection, product_id):
    try:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        connection.commit()
        print("Product deleted successfully.")
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        for product in products:
            print(product)
    except sqlite3.Error as e:
        print(e)

def select_products_by_conditions(connection, limit_price, limit_quantity):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products WHERE price < ? AND quantity > ?', (limit_price, limit_quantity))
        selected_products = cursor.fetchall()
        for product in selected_products:
            print(product)
    except sqlite3.Error as e:
        print(e)

def search_products_by_title(connection, keyword):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + keyword + '%',))
        matching_products = cursor.fetchall()
        for product in matching_products:
            print(product)
    except sqlite3.Error as e:
        print(e)

sql_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price  FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INT NOT NULL DEFAULT 0
)
'''
connection = create_connection('hw.db')
if connection is not None:
    print('Successfully connected to DB!')
    #create_table(connection,sql_create_products_table)
    #insert_products(connection)
    #update_price(connection,1,1555.0)
    #update_quantity(connection,3,18)
    #delete_product(connection,2)
    # select_all_products(connection)
    # search_products_by_title(connection,'Ш')
    select_products_by_conditions(connection,1000,100)






    connection.close
