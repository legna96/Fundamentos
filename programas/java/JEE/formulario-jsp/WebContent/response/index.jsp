<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>  
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Formulario JSP</title>
</head>
<body>

	<h1>Respuesta del Formulario Jsp</h1>
	
	<% 
		String nombre = request.getParameter("nombre");
		int edad = Integer.valueOf(request.getParameter("edad"));
		String sexo = request.getParameter("sexo");
		String ocupacion = request.getParameter("ocupacion");
	%>
	
	<p>Nombre: <%= nombre %></p>
	<p>Edad: <%= edad %> </p>
	<p>Sexo: <%= sexo %></p>
	<p>Ocupacion: <%= ocupacion %> </p>

</body>
</html>