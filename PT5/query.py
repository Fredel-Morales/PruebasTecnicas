#------------- Fredel Morales Jimenez-----------------------------
#--------- Reto 5: Servidor ElasticSearch ---------------------------
#--- El primer paso para este reto es importar la librería ElasticSearch 
# añadiendo de igual manera el servidor de donde tomaremos los datos del indice --------------

from elasticsearch import Elasticsearch

es = Elasticsearch ("http://38.348.39.19:9200")


#--------------Para construir la consulta ----------------------


query = {
    "query": {
        "bool": {
            "must": [
                {
                    "term": {
                        "tipo": "civil" #--- Aquí haremos nuestro primer filtro 
                        #ingresando el "tipo" de juicio, es este caso "civil" ------
                    }
                },
                {
                    "term": {
                        "estado": "activo" #--- Como "estado" es un documento que pertenece al 
                        #mismo indice, lo filtraremos de la misma manera mediante termino -----
                    }
                }
            ],
            "filter": {
                "nested": {
                    "path": "documentos", #---- "documentos" es un documento anidado por lo que 
                    #procederemos a filtrar primero mediante path ---------
                    "query": {
                        "bool": {
                            "must": [
                                {
                                    "term": {
                                        "tipo_documentos": "sentencia" #-------- "tipo_documentos" 
                                        #pertenece a "documentos" por lo que podemos filtrar mediante termino ---
                                    }
                                },
                                {
                                    "range": {
                                        "fecha": {
                                            "gte": "2022-01-01"
                                              # ---- "gte" significa el inicio de una fecha, y al estar 
                                              # bajo "range" nos arrojara hasta la fecha actual y de igual manera 
                                              # pertenece a "documentos".
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }
    },
    "size": 100  # ---- Limitaremos a 100 resultados la busqueda de juicios de "tipo" "civil" ----
}

# ------ Para realizar la búsqueda del indice "juicios" -----------------
response = es.search(index="juicios", body=query)

# ----- como paso final imprimiremos los resultados -----------------
for hit in response['hits']['hits']:
    print(hit['_source'])
