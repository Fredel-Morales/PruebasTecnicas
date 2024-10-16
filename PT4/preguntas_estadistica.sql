
-- Pregunta estadistica 

/* 1. Un conjunto de datos contiene informaci�n sobre diversos procesos judiciales,
como tipo de caso, duraci�n del proceso, edad de las partes involucradas, y si el caso
fue resuelto a favor o en contra de una de las partes. Quieres predecir si un caso se
resolver� a favor o en contra de la parte demandante.

	- �Qu� modelo de clasificaci�n ser�a m�s adecuado para este problema y por qu�?

	R= Regres�n Poisson 
		Porque su tipo de dato es de recuento y este modelo estadistico funciona con valores
		contables y podr�a funcionar para calcular la probabilidad de que ocurra un evento 
		a favor o en contra de la parte demandante durante un tiempo espec�fico que en este 
		caso ser�a la duraci�n del proceso y el tipo de caso.
	
	- Sup�n que has elegido una regresi�n log�stica. Explica como interpretar�as los coeficientes
	de este modelo y qu� m�tricas utilizar�as para evaluar su rendimiento.

	R=	Para interpretar los coeficientes utilizar�a como variable a predecir el estatus del
		caso (y) y las variables predictoras: la duraci�n del proceso (X1) y el tipo de caso (x2)
		creando una gr�fica con frontera de predicci�n y posteriormente se deber� definir definir 
		las caracteristicas de las variables predictoras y as� sabr�amos si el estatus es a favor
		o en contra.


   2. En un an�lisis de datos sobre la duraci�n de los casos judiciales, has encontrado algunos
   casos cuya duraci�n es significativamente mayor que el promedio.

	- �C�mo identificar�as formalmente estos valores at�picos en el conjunto de datos?

	R = Mediante el rango Intercuat�lico localizando lo siguiente: la mediana, Q1 y Q3, para despues
		identificar el rango intercuart�lico que dar� como resultado los valores atipicos.

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

	
	- Una vez identificados los valores at�picos, �Que har�as con ellos en tu an�lisis?	

	R = Los gestionar�a de manera adecuada, dandoles un seguimineto por separado ya que si no 
		se excluyen del an�lisis podr�an alterar los resultados del an�lisis estadistico.