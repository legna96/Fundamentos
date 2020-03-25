<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Formulario</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>

<style>

form {
	border: 1px solid #ccc;
	padding: 20px;
	margin: 20px auto;
	margin-bottom: 10px;
	border-radius: 10px;
}

.form-row {
	margin: 10px auto;
}

h1 {
	font-size: calc(1em + 3vw);
	text-align: center;
	display: block;
}

</style>


<body>
	<div class="container">
		<div class="row">
			<form class="col-12 col-md-4" action="registro" method="post">
				<h1>Formulario</h1>
				<hr>
				<div class="form-row">
				    <div class="col-12 col-md-3">
						<label>Nombre:</label>
				    </div>
				    <div class="col-12 col-md-9">
						<input type="text" class="form-control" name="nombre" required/>				      
				    </div>
				</div>
				<div class="form-row">
				    <div class="col-12 col-md-3">
						<label>Edad:</label>
				    </div>
				    <div class="col-12 col-md-4">
						<input type="number" class="form-control" min="18" max="50" name="edad" required/>				      
				    </div>
				</div>
				<div class="form-row">
				    <div class="col-12 col-md-3">
						<label>Sexo:</label>
				    </div>
				    <div class="col-12 col-md-9">
						<div class="form-check">
						  <input class="form-check-input" type="radio" name="sexo" value="Masculino" checked>
						  <label class="form-check-label">
						    Masculino
						  </label>
						</div>
						<div class="form-check">
						  <input class="form-check-input" type="radio" name="sexo" value="Femenino">
						  <label class="form-check-label">
						    Femenino
						  </label>
						</div>			      
				    </div>
				</div>
				<div class="form-group">
					<label>Ocupacion:</label>
					<select class="form-control" name="ocupacion" required>
						<option>Programador</option>
						<option>Estudiante</option>
					</select>
				</div>
				<input type="submit" value="Enviar" class="btn btn-success btn-block" />
			</form>
		</div>
	</div>
</body>
</html>