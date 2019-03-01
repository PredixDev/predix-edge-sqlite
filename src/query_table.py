import sqlite3

sqlite_file = '/var/lib/edge-agent/app/sqlite/data/test.db'    # name of the sqlite database file
table_name1 = 'my_table_1'  # name of the table to be created
table_name2 = 'my_table_2'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Inserting table items 
c.execute('INSERT INTO my_table_1 VALUES (1234)')
c.execute('INSERT INTO my_table_1 VALUES (4321)')
c.execute('INSERT INTO my_table_1 VALUES (2341)')
c.execute('INSERT INTO my_table_1 VALUES (3421)')
c.execute('INSERT INTO my_table_1 VALUES (1423)')


c.execute('SELECT * from my_table_1')
all_tbl_itms = c.fetchall()
print('All entries in database', all_tbl_itms)

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

