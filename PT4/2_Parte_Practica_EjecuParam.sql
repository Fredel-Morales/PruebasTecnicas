
-- Aquí vamos a ejecutar los parametros --

DECLARE @resol AS INT
DECLARE @promedio AS INT
DECLARE @message AS VARCHAR(50)


EXEC [CasosPorJuez].[uspGetObtenerCasosPorJuez] 
	@i_titularid = -- Escrbir el Id del Titular--
	,@o_resol =  OUTPUT
	,@o_prom =  OUTPUT
	,@o_message = OUTPUT



SELECT @resol AS [PromedioDias], @message AS [Message]
