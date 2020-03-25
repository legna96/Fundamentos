package mx.arl96.servlets;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class RegistroJson
 */
@WebServlet("/RegistroJson")
public class RegistroJson extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public RegistroJson() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("utf-8");
		response.setContentType("text/html");
		
		PrintWriter salida = response.getWriter();
		String saludo = "<h1>Get Registro Json</h1>";
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
		
		response.setContentType("application/json");
		response.setCharacterEncoding("utf-8");
		PrintWriter salida = response.getWriter();
		
		String json = "{"
				+ "\"nombre\":\"" + nombre + "\","
				+ "\"edad\":" + edad + ","
				+ "\"sexo\":\"" + sexo + "\","
				+ "\"ocupacion\":\"" + ocupacion + "\""
				+ "}";
		
		System.out.println(json);
		salida.print(json);
		
	}

}
