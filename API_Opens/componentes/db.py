import psycopg2

def migracion_datos(datos):
	conexion = psycopg2.connect(database = "Opens", user = "opensrale", password = "rale2022", host = "localhost", port = "5432")
	cursor = conexion.cursor()
	sql = 'INSERT INTO "Email"(nombre,fecha,asunto,cuerpo) VALUES (%s,%s,%s,%s)'
	insert = str(datos[0]),str(datos[1]),str(datos[2]),str(datos[3])
	cursor.execute(sql,insert)
	conexion.commit()

def consulta_cuerpo():
	conexion = psycopg2.connect(database = "Opens", user = "opensrale", password = "rale2022", host = "localhost", port = "5432")
	cursor = conexion.cursor()
	sql = 'SELECT cuerpo FROM "Email"'
	cursor.execute(sql)
	data_cuerpo = []
	for sentencia in cursor:
		data_cuerpo.extend(sentencia)
	conexion.close()
	return data_cuerpo

def consulta_destinatario():
	conexion = psycopg2.connect(database = "Opens", user = "opensrale", password = "rale2022", host = "localhost", port = "5432")
	cursor = conexion.cursor()
	sql = 'SELECT nombre FROM "Email"'
	cursor.execute(sql)
	data_from = []
	for sentencia in cursor:
		data_from.extend(sentencia)
	conexion.close()
	return data_from

def consulta_plantilla():
        conexion = psycopg2.connect(database = "Opens", user = "opensrale", password = "rale2022", host = "localhost", port = "5432")
        cursor = conexion.cursor()
        sql = 'SELECT *  FROM "Plantilla"'
        cursor.execute(sql)
        plantilla = []
        for sentencia in cursor:
                plantilla.extend(sentencia)
        conexion.close()
        return plantilla
