<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Formulario</title>
</head>
<body>

	<!--  No responde a rutas: uri 'response' no funciona  -->
	<form action="response/index.jsp" method="post">
		<h1>Formulario Jsp</h1>
		<label>Nombre:</label>
		<input type="text" name="nombre" required/>
		<br>
		<label>Edad:</label>
		<input type="number" min="18" max="50" name="edad" required/>
		<br>
		<label>Sexo:</label>
		<input type="radio" name="sexo" value="Masculino" checked > M
		<input type="radio" name="sexo" value="Femenino"> F
		<br>
		<label>Ocupacion:</label>
		<select name="ocupacion" required>
			<option>Programador</option>
			<option>Estudiante</option>
		</select>
		<br>
		<input type="submit" value="Enviar" />
	</form>

</body>
</html>