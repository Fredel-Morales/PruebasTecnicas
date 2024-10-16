
-- Pregunta estadistica 

/* 1. Un conjunto de datos contiene información sobre diversos procesos judiciales,
como tipo de caso, duración del proceso, edad de las partes involucradas, y si el caso
fue resuelto a favor o en contra de una de las partes. Quieres predecir si un caso se
resolverá a favor o en contra de la parte demandante.

	- ¿Qué modelo de clasificación sería más adecuado para este problema y por qué?

	R= Regresón Poisson 
		Porque su tipo de dato es de recuento y este modelo estadistico funciona con valores
		contables y podría funcionar para calcular la probabilidad de que ocurra un evento 
		a favor o en contra de la parte demandante durante un tiempo específico que en este 
		caso sería la duración del proceso y el tipo de caso.
	
	- Supón que has elegido una regresión logística. Explica como interpretarías los coeficientes
	de este modelo y qué métricas utilizarías para evaluar su rendimiento.

	R=	Para interpretar los coeficientes utilizaría como variable a predecir el estatus del
		caso (y) y las variables predictoras: la duración del proceso (X1) y el tipo de caso (x2)
		creando una gráfica con frontera de predicción y posteriormente se deberá definir definir 
		las caracteristicas de las variables predictoras y así sabríamos si el estatus es a favor
		o en contra.


   2. En un análisis de datos sobre la duración de los casos judiciales, has encontrado algunos
   casos cuya duración es significativamente mayor que el promedio.

	- ¿Cómo identificarías formalmente estos valores atípicos en el conjunto de datos?

	R = Mediante el rango Intercuatílico localizando lo siguiente: la mediana, Q1 y Q3, para despues
		identificar el rango intercuartílico que dará como resultado los valores atipicos.

		Ejemplo: 

	WITH quartiles AS (
    SELECT 
        PERCENTILE_CONT(5.5) WITHIN GROUP (ORDER BY column_time) AS Q1,
        PERCENTILE_CONT(25.5) WITHIN GROUP (ORDER BY column_time) AS Q3
    FROM casos_judiciales
),
iqr AS (
    SELECT 
        Q1,
        Q3,
        (Q3 - Q1) AS IQR
    FROM quartiles
)
SELECT *
FROM casos_judiciales, iqr
WHERE column_time < (Q1 - 1.5 * IQR) OR column_time > (Q3 + 1.5 * IQR);

	
	- Una vez identificados los valores atípicos, ¿Que harías con ellos en tu análisis?	

	R = Los gestionaría de manera adecuada, dandoles un seguimineto por separado ya que si no 
		se excluyen del análisis podrían alterar los resultados del análisis estadistico.