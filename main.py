import sqlite3


conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor() #objeto mensageiro

#cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, titular TEXT NOT NULL, saldo FLOAT NOT NULL, cpf TEXT NOT NULL UNIQUE)""")

cursor.execute("""INSERT INTO contas_bancarias(titular, saldo, cpf) VALUES ('joao', 6000, '3409303')""")

contas = cursor.fetchall()

cursor.execute("SELECT titular, saldo FROM contas_bancarias")
#cursor.execute("DELETE FROM contas_bancarias WHERE id = 2")

for conta in contas:
    titular, saldo = conta
    print(f"""
id: {id}
titular: {titular}
saldo: {saldo}
""")

conexao.commit()