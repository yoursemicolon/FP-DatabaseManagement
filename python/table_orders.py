import random
import datetime
import string
from random import choice
from string import ascii_uppercase
from faker import Faker

fake = Faker()
Faker.seed(0)

# order_id
id = 831
order_id = []
for _ in range(150000):
    order_id.append(id)
    id += 1

# customer_id
cus_id = ["ALFKI", "ANATR", "ANTON", "AROUT", "BERGS",
            "BLAUS", "BLONP", "BOLID", "BONAP", "BOTTM",
            "BSBEV", "CACTU", "CENTC", "CHOPS", "COMMI",
            "CONSH", "DRACD", "DUMON", "EASTC", "ERNSH",
            "FAMIA", "FISSA", "FOLIG", "FOLKO", "FRANK",
            "FRANR", "FRANS", "FURIB", "GALED", "GODOS",
            "GOURL", "GREAL", "GROSR", "HANAR", "HILAA",
            "HUNGC", "HUNGO", "ISLAT", "KOENE", "LACOR",
            "LAMAI", "LAUGB", "LAZYK", "LEHMS", "LETSS",
            "LILAS", "LINOD", "LONEP", "MAGAA", "MAISD",
            "MEREP", "MORGK", "NORTS", "OCEAN", "OLDWO",
            "OTTIK", "PARIS", "PERIC", "PICCO", "PRINI",
            "QUEDE", "QUEEN", "QUICK", "RANCH", "RATTC",
            "REGGC", "RICAR", "RICSU", "ROMEY", "SANTG",
            "SAVEA", "SEVES", "SIMOB", "SPECD", "SPLIR",
            "SUPRD", "THEBI", "THECR", "TOMSP", "TORTU",
            "TRADH", "TRAIH", "VAFFE", "VICTE", "VINET",
            "WANDK", "WARTH", "WELLI", "WHITC", "WILMK",
            "WOLZA"]

customer_id = []
for _ in range(150000):
    customer_id.append(random.choice(cus_id))

# # employee_id
employee_id = []
for _ in range(150000):
    employee_id.append(random.randint(1,9))

# order_date, required_date, shipped_date
order_date = []
required_date = []
shipped_date = []

start = datetime.date(year=1996, month=1, day=1)
end = datetime.date(year=1998, month=12, day=31)

for _ in range(150000):
    order_date.append(fake.date_between(start_date=start, end_date=end))
    required_date.append(fake.date_between(start_date=start, end_date=end))
    shipped_date.append(fake.date_between(start_date=start, end_date=end))

# ship_via
ship_via = []
for _ in range(150000):
    ship_via.append(random.randint(1,6))

# freight
freight = []
for _ in range(150000):
    freight.append(random.randint(0, 200000)/100)

# ship_name
ship_name = []
for _ in range(150000):
    ship_name.append((fake.company()).replace('\'',''))

# ship_address
ship_address = []
for _ in range(150000):
    ship_address.append((fake.address()).replace('\'',''))

# ship_city
ship_city = []
for _ in range(150000):
    ship_city.append((fake.city()).replace('\'',''))

# ship_region
ship_region = []
for _ in range(150000):
    ship_region.append(''.join(choice(ascii_uppercase) for i in range(2)))

# ship_postal_code
ship_postal_code = []
for _ in range(150000):
    ship_postal_code.append(''.join(choice(string.digits) for i in range(6)))

# ship_country
ship_country = []
for _ in range(150000):
    ship_country.append((fake.country()).replace('\'',''))

# Query
new_record = open('orders_3.sql', 'a+')
for i in range(150000):
    new_record.write('INSERT INTO ORDERS VALUES({0}, \'{1}\', {2}, \'{3}\', \'{4}\', \'{5}\', '
          '{6}, {7}, \'{8}\', \'{9}\', \'{10}\', \'{11}\', \'{12}\', \'{13}\');\n'.format(order_id[i], customer_id[i], employee_id[i],
                                                                                         order_date[i],required_date[i], shipped_date[i],
                                                                                         ship_via[i], freight[i], ship_name[i], ship_address[i],
                                                                                         ship_city[i], ship_region[i], ship_postal_code[i],
                                                                                         ship_country[i]))
new_record.close()