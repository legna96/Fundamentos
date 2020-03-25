package mx.arl96.controllers;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import mx.arl96.models.Form;

/**
 * Servlet implementation class Registro
 */
@WebServlet("/registro")
public class Registro extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Registro() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * configura salida para escribe Html bruto
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("utf-8");
		response.setContentType("text/html");
		
		PrintWriter salida = response.getWriter();
		String saludo = "<h1> Get Registro, revisa el servlet del formulario</h1>";
		salida.println(saludo);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		request.setCharacterEncoding("utf-8");
	    
		String nombre = request.getParameter("nombre");
		int edad = Integer.valueOf(request.getParameter("edad"));
		String sexo = request.getParameter("sexo");
		String ocupacion = request.getParameter("ocupacion");
		
		Form form = new Form(nombre,edad,sexo,ocupacion);
		request.setAttribute("data", form);
		
		RequestDispatcher rd = request.getRequestDispatcher("respuesta.jsp");
		rd.forward(request, response);
		
	}

}
