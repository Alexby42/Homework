import sqlite3
connection = sqlite3.connect('Products.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
''')
texts = [
        'Сбалансированная добавка, насыщенная кислотами Омега 3 с добавлением витаминов A, D3, E',
        'Морской коллаген стимулирует выработку собственного коллагена в организме способствуя омоложению изнутри',
        'Биотин (Витамин В7) преобразовывает белки, жиры и углеводы в энергию',
        'Витамин К2 - относится к активным нутриентам, крайне необходимый в процессах метаболизма',
        'Полноценный комплекс содержащий витамины и минералы в нужной дозировке для взрослого организма'
    ]
products = ['Omega 3+D3','Collagen','Biotin','Vitamin K2','Multivitamines']
prices = ['450', '750', '400', '390', '600']
for prod, text, pr in zip(products, texts, prices):
    cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)', (prod, text, pr))
def get_all_product():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT title FROM Products')
    title_list = cursor.fetchall()
    cursor.execute('SELECT description FROM Products')
    descriptions_list = cursor.fetchall()
    cursor.execute('SELECT price FROM Products')
    prices_list = cursor.fetchall()
    return [title_list, descriptions_list, prices_list]
connection.commit()
connection.close()
