<%@ page import = "mx.filiArl.calculos.*" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Web de Prueba</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<h1>Import de jsp (menu.jsp)</h1>

<jsp:include page = "menu.jsp" />


<h3>expresion jsp</h3>

<%= getSuma(5,7) %>

<h3>multiples lineas jsp</h3>
<% 

	for(int i=0; i<5; i++){
		out.print("<p>"+ getSuma(i,i+1) + "</p>");
		out.print("<button class='btn btn-success' onclick=alert(" + i + ")>valor de i</button>");
	}
%>

<h3>codigo java en jsp</h3>

<%!

 int getSuma(int num1, int num2){
	return num1 + num2;
 }

%>

<p> La resta de 7 - 5 = <%= Operaciones.resta(7,5) %></p>

</body>
</html>