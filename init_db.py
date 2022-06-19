import sqlite3
import json

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

input_dict = json.load(open('pokemon.json'))
# Filter python objects with list comprehensions
for x in input_dict:
    cur.execute("INSERT INTO pokedex (number,name,type_1,type_2,total,hp,attack,defense,sp_atk,sp_def,speed,generation,legendary) VALUES (?, ?)",
            (x["#"],x["Name"],x["Type 1"],x["Type 2"],x["Total"],x["HP"],x["Attack"],x["Defense"],x["Sp. Atk"],x["Sp. Def"],x["Speed"],x["Generation"],x["Legendary"]))
connection.commit()
connection.close()