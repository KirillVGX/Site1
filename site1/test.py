from faker import Faker
from tabulate import tabulate
import sqlite3
 
conn = sqlite3.connect('test.db')
curs = conn.cursor()
 
curs.execute('''
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50), 
    name VARCHAR(50), 
    sex VARCHAR(1), 
    address VARCHAR(100), 
    mail VARCHAR(50), 
    birthdate DATE
)
''')
 
fake = Faker('uk_UA')
 
# table = []
# id = 1
# for _ in range(100):
#     table.append(fake.simple_profile())
#     id += 1
 
# print(tabulate(table, headers='keys', tablefmt="grid"))
 
# print(dir(fake))
 
# curs.execute("DROP TABLE IF EXISTS users")
sql = 'INSERT INTO users (username, name, sex, address, mail, birthdate) VALUES (?, ?, ?, ?, ?, ?)'
 
for _ in range(20):
    data = fake.simple_profile()
    curs.execute(sql, list(data.values()))
 
curs.execute("SELECT * FROM users")
all_data = curs.fetchall()
 
print(tabulate(all_data, tablefmt="grid"))