import random
import datetime
import string
from random import choice
from string import ascii_uppercase
from faker import Faker

fake = Faker()
Faker.seed(0)

# order_id
id = 11078
order_id = []
for _ in range(500000):
    order_id.append(id)
    id += 1

# product id
product_id = []
for _ in range(500000):
    product_id.append(random.randint(1,77))

# unit_price
unit_price = []
for _ in range(500000):
    unit_price.append(random.randint(100, 30000)/100)

# quantity
quantity = []
for _ in range(1500000):
    quantity.append(random.randint(10,200))

# discount
discount = 0

# Query
new_record = open('order_details.sql', 'a+')
for i in range(500000):
    new_record.write('INSERT INTO ORDER_DETAILS VALUES({0}, {1}, {2}, {3}, {4});\n'.format(order_id[i], product_id[i], unit_price[i], quantity[i], discount))

new_record.close()