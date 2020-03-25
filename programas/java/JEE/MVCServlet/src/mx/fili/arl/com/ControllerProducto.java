package mx.fili.arl.com;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/productos")
public class ControllerProducto extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    
    public ControllerProducto() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		List<String> productos = new ArrayList<>();
		productos.add("Leche");
		productos.add("Huevos");
		productos.add("Pan");
		productos.add("Mantequilla");
		productos.add("Harina");
		
		request.setAttribute("productos", productos);
		
		RequestDispatcher rd = request.getRequestDispatcher("/vista.jsp");
		
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}

