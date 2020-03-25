package mx.filiarl.app.controles;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import mx.filiarl.app.interfaces.ITareas;

@Controller
public class IndexController {
	
	@Autowired
	@Qualifier("servicioAlumnoSociales")
	ITareas servicioAlumno;
	
	@PostConstruct
	public void postConstruct() {
		System.out.println("Post inyeccion de dependencias");
	}
	
	@PreDestroy
	public void preDestroy() {
		System.out.println("Pre destroy component Inyectado");
	}
	
	@GetMapping("/")
	public String principal(Model model) {
		model.addAttribute("trabajo", servicioAlumno.trabajo());
		model.addAttribute("titulo", "Practica de DI");
		return "index";
	}
	
}
