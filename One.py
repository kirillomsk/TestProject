import psycopg2
from selenium import webdriver
from mimesis import Food
from random import randint
from conftest import chromedriver


def get_table():
    res = []
    for i in range(len(driver.find_elements_by_css_selector('tr')) - 1):
        _ = []
        for j in range(3):
            _.append(driver.find_element_by_css_selector(f'tr:nth-child({i + 1}) > td:nth-child({j + 1})').text)
        res.append(tuple(_))
    return res


def add(name, num):
    _ = driver.find_element_by_name(name)
    _.clear()
    _.send_keys(num)


product = Food('ru')
conn = psycopg2.connect(host="127.0.0.1", port='5432', database="postgres", user="postgres", password="123456789")
cur = conn.cursor()

# set table
try:
    cur.execute('CREATE TABLE shopping_list (name text, count text, price text);')
    conn.commit()
except:
    cur.close()
    conn.close()
    print('Таблица уже создана')
    conn = psycopg2.connect(host="127.0.0.1", port='5432', database="postgres", user="postgres", password="123456789")
    cur = conn.cursor()

driver = webdriver.Chrome(chromedriver)
driver.get('https://checkme.kavichki.com/')

table = get_table()
for i in range(len(table)):
    cur.execute(
        f"INSERT INTO shopping_list (name, count, price) VALUES ('{table[i][0]}', '{table[i][1]}', '{table[i][2]}');")
    conn.commit()

for i in range(randint(2, 12)):
    typ = (product.fruit(), randint(1, 30), randint(30, 250))
    driver.find_element_by_id('open').click()
    add('name', typ[0])
    add('count', typ[1])
    add('price', typ[2])
    driver.find_element_by_id('add').click()
added = get_table()
driver.close()

cur.execute('SELECT * FROM shopping_list')
conn.commit()
primary = cur.fetchall()

result = set(added) - set(primary)
for i in result:
    print(i)

cur.close()
conn.close()

