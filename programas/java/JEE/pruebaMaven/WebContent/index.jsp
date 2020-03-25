<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Prueba Maven</title>
</head>
<body>

	<h1>Maven Prueba</h1>
	<p>lorem impsu </p>
	
	<c:forEach var="producto" items="${productos}">
	 <p>${producto}</p>
	</c:forEach>

</body>
</html>