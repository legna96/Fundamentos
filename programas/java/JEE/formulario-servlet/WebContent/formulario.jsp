<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Formulario</title>
</head>
<body>

	<form action="Registro" method="post">
		<h1>Formulario Registro html</h1>
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
	
	<form action="RegistroJson" method="post">
		<h1>Formulario Registro Json</h1>
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