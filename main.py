import pymysql

conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="pwdmn"
    )

cursor = conexion.cursor()

consulta = "select * from web;"

cursor.execute(consulta)

datos = cursor.fetchone()

print(datos[1])
