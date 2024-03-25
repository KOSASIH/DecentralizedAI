import sqlite3

# Connect to the database
conn = sqlite3.connect('resources/financial_database.db')

# Create a table
conn.execute('CREATE TABLE stocks (symbol text, price real)')

# Insert some data
conn.execute('INSERT INTO stocks (symbol, price) VALUES (?, ?)', ('IBM', 143.23))
conn.execute('INSERT INTO stocks (symbol, price) VALUES (?, ?)', ('AAPL', 173.43))

# Commit the changes and close the connection
conn.commit()
conn.close()
