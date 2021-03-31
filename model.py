import sqlite3
import pandas as pd

# [ ] Configurar SQLITE para funcionar no projeto

conn = sqlite3.connect('taxon.db')
print ("Opened database successfully")


conn.execute('''CREATE TABLE PLANTS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         FIELD            INT     NOT NULL,
         FIELD        CHAR(50),
         FIELD         REAL);''')

print ("Table created successfully")

#conn.close()

conn.execute("INSERT INTO COMPANY (?,?,?,?,?) \
      VALUES (?, '?', ?, '?', ? )");

conn.commit()
print ("Records created successfully")
conn.close()

# [ ] Implementar uma função de teste para inserir 10milhões de registros

csv_database = create_engine('sqlite:///csv_database.db')
chucksize = 1000000
file = 'file.csv'
i = 0
j = 0

for df in pd.read_csv(file, chucksize=chucksize, iterator=True):
      df = df.rename(columns = {c : c.replace(' ', '') for c in df.columns)}
      df.index += j

      df.to_sql('data_use', csv_database, if_exists='append')
      j = df.index[-1]+1

      print(' index[]'.format(j))

#fazer busca por chave

#retornar alguns ids
df.head()
