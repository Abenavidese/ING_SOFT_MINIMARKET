import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("minimercado.db")
cursor = conn.cursor()

# Obtener nombres de las tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()

print("Tablas encontradas y sus columnas:\n")

for tabla in tablas:
    nombre_tabla = tabla[0]
    print(f"🟦 Tabla: {nombre_tabla}")
    
    # Obtener las columnas de la tabla
    cursor.execute(f"PRAGMA table_info('{nombre_tabla}');")
    columnas = cursor.fetchall()
    
    for col in columnas:
        cid, nombre, tipo, notnull, dflt_value, pk = col
        print(f"   - {nombre} ({tipo}){' [PK]' if pk else ''}")
    
    print()

conn.close()
