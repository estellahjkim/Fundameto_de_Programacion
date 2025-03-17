import sqlite3
from utilities import create_db, show, show_file


# Escriba aquí la función solicitada
def export_data(coches, fichero, marca):
    with sqlite3.connect(coches) as conex, open(fichero, "w") as fich:
        cursor = conex.cursor()
        consulta = """
            SELECT matrícula, modelo, año
            FROM coches
            WHERE marca = ?
        """
        valores = [marca]
        result = cursor.execute(consulta, valores)
        for coche in result.fetchall():
            linea = ",".join(coche)
            print(linea, file=fich)


if __name__ == "__main__":
    create_db("concesionario.db")
    print("--- Base de Datos original ---")
    show("concesionario.db")

    bbdd = "concesionario.db"
    file = "concesionario.csv"
    marca = "Toyota"

    export_data(bbdd, file, marca)

    print("\n--- Contenido del fichero resultante ---")
    show_file(file)
