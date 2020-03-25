<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
<link rel="stylesheet" href="styles.css">
<title>JSP - JSTL</title>
</head>
<body>
	
	<jsp:include page = "menu.jsp" />
	
	<%
	List<String> lista = new ArrayList<String>();
	lista.add("Angel");
	lista.add("Jonha");
	lista.add("Luis");
	lista.add("Karis");
	pageContext.setAttribute("lista", lista);
	System.out.println( lista.toString() );
	%>
	
	<c:forEach items="${lista}" var="item">
    	<p>${item}</p>
	</c:forEach>

</body>
</html>