#----------------- Fredel Morales Jimenez ---------------------------
#----------- Reto 3 : Construir un API ----------------------------
# NOTA: Los archivos y la infomación para esta actividad fueron tomados de la fuente:
# "https://www.inegi.org.mx/programas/ccpv/2020/#datos_abiertos"

#----------------- El primer paso será importar las bibliotecas y asignar 
# nuestra variable a Flask, que en este caso es "app"---------------

from flask import Flask, request, jsonify, send_file
import pandas as pd

app = Flask(__name__)

#----- En la siguiente línea haremos la petición de la ruta del archivo,
#es importante que su formato sea "CSV" y tener el archivo en la misma carpeta------

#-- Cambiaremos el nombre del archivo .CSV de acuerdo a la "entidad_federativa" que requiramos --
CSV_FILE_PATH = '{entidad_federativa}.csv'  

#------- Posteriormente se muestra el Endpoint "POST" que nos proporcionará la
#descarga de los archivos --------
@app.route('/ejercicio//{entidad_federativa}/descarga', methods=['POST'])
def descarga():
    data = request.json
    formato = data.get('formato')

#--- Esta función nos servirá para detectar si el formato del archivo es incorrecto y
# de ser así nos retornará un mensaje con la advertencia ---

    if formato not in ['csv', 'json']:
        return jsonify({'error': 'Formato no válido'}), 400

#--- También se requiere de una condicional "if" - "elif" para que nos retorne el documento ---
    if formato == 'csv':
        return send_file(CSV_FILE_PATH, mimetype='text/csv', as_attachment=True)
    elif formato == 'json':
        df = pd.read_csv(CSV_FILE_PATH)
        return jsonify(df.to_dict(orient='records'))

#--- Esta función nos se mostrará el Endpoint "GET" que nos proporcionará los
#estadisticos del documento de la "entidad_federativa" que requiramos --------
@app.route('/ejercicio/{entidad_federativa}/estadisticos/', methods=['GET'])
def estadisticos():
    df = pd.read_csv(CSV_FILE_PATH)
   
    # -- La sigueinte funcion es para declarar las estadísticas que necesitemos de acuerdo 
    # a la estructura de nustro documento y de la información que necesitemos----
    estadisticas = {

        #--- En este caso para el analisis de mis documentos lo que necesito es lo siguiente: ---
        'total_registros': len(df),
        'columnas': list(df.columns),
        'tipos_datos' : df.dtypes.to_dict(),
        'estadisticas_descriptivas': df.describe().to_dict()
    }
    return jsonify(estadisticas)

if __name__ == '__main__':
    app.run(debug=True)
