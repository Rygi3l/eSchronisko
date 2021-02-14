import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

#query = 'CREATE TABLE employees (ID int, name varchar(255), surname varchar(255), role varchar(100))'

# query = 'CREATE TABLE animals (ID int, imie varchar(255), species varchar(100), breed varchar(100), vaccinated bool, date_of_admission_to_the_shelter date, reserved bool)'

# query = 'CREATE TABLE adoptions (ID_adoption int, ID_animal int, name varchar(255), species varchar(100), date_of_adoption date)'

# query = 'CREATE TABLE reservations (ID_reservation int, ID_animal int, name varchar(255), species varchar(100), date_of_reservation date)'

# query = 'INSERT INTO animals VALUES ("1", "Borys", "Pies", "Owczarek Niemiecki", "1", "2020-05-13", "0")'

#query = 'ALTER TABLE employees RENAME COLUMN ID TO ID_employee'

#query = 'INSERT INTO reservations VALUES ("1", "1", "Borys", "Pies", "2020-06-10")'

#max_query = 'SELECT MAX (ID_reservation) FROM reservations'

#result = c.execute(max_query).fetchall

#query = result[0]+1

#query = f'INSERT INTO reservations VALUES({chuj}, "2", "Tadek", "Kot", "2020-07-23")'

#query = 'CREATE TABLE lost_notice (ID INT, message TEXT, name VARCHAR(255), date DATETIME)'

#query = 'CREATE TABLE trial_walk (ID INT, name VARCHAR(255), ID_animal INT, phone VARCHAR(50), date DATETIME)'

"""


* query = 'SELECT * FROM psy'
results = c.execute(query)
for result in results:
    print(result)


"""

c.execute(query)
conn.commit()
conn.close()
