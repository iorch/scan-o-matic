from clarifai.client import ClarifaiApi
from flask import jsonify
import MySQLdb
import os

clarifai_api = ClarifaiApi() # assumes environment variables are set.
photosdir = os.path.dirname(os.path.realpath(__file__)) + "/fotos/"

def get_nutri_facts(lst):
	db = MySQLdb.connect(host="192.168.99.100", port=32768 ,user="root",db="scanomatic" )
	cursor = db.cursor()
	sql = "SELECT * FROM alimentos \
		   WHERE Alimento='%s' OR  Alimento='%s' \
		   OR Alimento='%s' " %(str(lst[0]), str(lst[1]), str(lst[2]))
	try:
	   	cursor.execute(sql)
	   	results = cursor.fetchall()
	   	for row in results:
	   		res = {
	      	'Alimento': row[1],
	      	'Calorias': row[2],
	      	'Grasas_total': row[3],
	      	'Acidos_grasos_saturados': row[4],
	     	'Acidos_grasos_poliinsaturados': row[5],
	     	'Acidos_grasos_monoinsaturados': row[6],
	    	'Colesterol': row[7],
	   	   	'Sodio': row[8],
	      	'Potasio': row[9],
	      	'Carbohidratos': row[10],
	      	'Fibra': row[11],
	 	    'Azucares': row[12],
	      	'Proteinas': row[13],
	     	'Hierro': row[14],
	      	'Calcio': row[15],
	      	'Magnesio': row[16],
		    'VitaminA': row[17],
	      	'VitaminB6': row[18],
	      	'VitaminB12': row[19],
		    'VitaminC': row[20],
	      	'VitaminD': row[21],
	      	'VitaminE': row[22],
	      	'VitaminF': row[23]
			}
	except:
		print "No pudimos encontrar tu alimento."
	db.close()
	return res

def is_healthy(res):
	nutri = {}
	nutri["Alimento"] = res['Alimento']
	if res['Calorias'] < 80:
		nutri['Calorias'] = 1
	else :
		nutri['Calorias'] = 0
	if res['Grasas_total'] < 0.5:
		nutri['Grasas_total'] = 1
	else:
		nutri['Grasas_total'] = 0
	if ( res['VitaminB6'] + res['Potasio'] + res['VitaminF'] + res['VitaminD'] + res['VitaminE']+ res['VitaminC'] + res['VitaminA'] + res['VitaminB12'] + res['Sodio'] + res['Hierro'] + res['Magnesio'] + res['Calcio'] ) > 200:
		nutri["Vitaminas"] = 1
	else:
		nutri["Vitaminas"] = 0
	if res['Proteinas'] > 0.55:
		nutri['Proteinas'] = 1
	else:
		nutri['Proteinas'] = 0
	return nutri


alimento = raw_input("Dame un alimento de la carpeta fotos:")

try:
	result = clarifai_api.tag_images(open(photosdir + alimento, 'rb'))
	mylist = result['results'][0]['result']['tag']['classes']
	res = get_nutri_facts(mylist)
	hly = is_healthy(res)
	print hly
except:
	print "Error con la foto."


