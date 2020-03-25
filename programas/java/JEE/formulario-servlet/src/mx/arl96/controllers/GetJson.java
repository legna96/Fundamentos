package mx.arl96.controllers;

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
@WebServlet("/getjson")
public class GetJson extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public GetJson() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setContentType("application/json");
		
		String nombre = "Angel";
		int edad = 23;
		String sexo = "Masculino";
		String ocupacion = "Programador";

		PrintWriter salida = response.getWriter();
		
		String json = "{"
				+ "\"nombre\":\"" + nombre + "\","
				+ "\"edad\":" + edad + ","
				+ "\"sexo\":\"" + sexo + "\","
				+ "\"ocupacion\":\"" + ocupacion + "\""
				+ "}";
		
		salida.print(json);
		
	}

}
