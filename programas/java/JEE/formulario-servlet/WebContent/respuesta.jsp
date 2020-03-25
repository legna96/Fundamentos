<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Respuesta</title>
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
	</head>
	<body>
	
	<style>
	
	.contenido {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		height: 100vh;
	}
	
	.contenido h1 {
		font-size: calc(1em + 3vw);
		text-align: center;
		display: block;
	}
	
	.contenido p{
	
		font-size: calc(1em + .8vw);
		line-heigth: 1;
		margin: 0;
	
	}
	
	.contenido span {
		font-size: calc(1em + .8vw);
		font-weight: bold;
	}
	
	</style>
	
		<div class="contenido">
			<h1>Respuesta de Formulario</h1>
			<p><span>Nombre:</span> ${data.getNombre()}</p>
			<p><span>Edad:</span> ${data.getEdad()}</p>
			<p><span>Sexo:</span> ${data.getSexo()}</p>
			<p><span>Ocupacion:</span> ${data.getOcupacion()}</p>
			<a class="btn btn-info" href="http://localhost:8080/formulario-servlet/"> Volver </a>
		</div>		
	 
	</body>
</html>