-- ================================================
-- Reto 4. Prueba SQL y Store Procedures
-- Supon que trabajas con una base de datos que almacena informaci�n sobre casos judiciales.
-- La base de datos contiene una tabla llamada Asuntos con los siguientes campos:
-- 1 AsuntoId (BIGINT): Identificador �nico del caso.
-- 2 TipoAsuntoId (VARCHAR): Tipo de caso (por ejemplo: civil, penal, laboral)
-- 3 FechaAlta (DATE): Fecha en que comenz� el caso.
-- 4 FechaResoluci�n (DATE): Fecha en que se resolvi� el caso.
-- 5 TitularId (VARCHAR): Id empleado del juez que llev� a cabo el caso.
-- 6 ResolucionId (INT): Resultado del caso (a favor, en contra, desestimado)
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Fredel Morales>
-- Description:	<Vamos a retornar la informaci�n de la tabla que se nos asign� y a crear  un Store Procedure ---------
-- =============================================
ALTER PROCEDURE [CasosPorJuez].[uspGetObtenerCasosPorJuez]

-- Posteriormente vamos a declarar los parametros tanto para
-- solicitar informaci�n asi como para retornar la informac�n -- 

	@i_titularid		VARCHAR(50)
	,@o_resol			INT = 0				OUTPUT
	,@o_mesagge			VARCHAR(50) = ''	OUTPUT		
	,@o_promedio		INT = 0
AS
BEGIN
	---- Para que me muestre la informaci�n ----
	SELECT
		[cpj].[AsuntoId]
		,[cpj].[TitularId]
		,[cpj].[FechaAlta]
		,[cpj].[FechaResoluci�n]

	FROM 
		[CasosPorJuez].[Asuntos] AS [cpj]
	WHERE
		[cpj].[TitularId] = @i_titularid
		AND [FechaAlta] = @FechaInicio
		AND [FechaResoluci�n] = @FechaFin

	-- Funciones para obtener el promedio Y hacer la condicional para que nos arroje lo siguiente:
	-- Cantidad de casos resueltos
	-- Promedio de d�as y el mensaje de no hay resultados.
	,CASE
		WHEN SELECT COUNT(@o_resol)
			FROM [Asuntos]
			WHERE [ResolucionId] = 'Desestimado' 

		    SELECT DATEDIFF(DAY, [FechaAlta], [FechaResolucion]) AS dias_diferencia
			FROM [Asuntos]

			SELECT 
			DATEDIFF AVG [FechaAlta] + DATEDIFF[FechaResolucion] / dias_diferencia  AS fecha_promedio
			FROM [Asuntos]
	ELSE
			
		 @o_mesagge = 'Sin Resultados'
END
GO
