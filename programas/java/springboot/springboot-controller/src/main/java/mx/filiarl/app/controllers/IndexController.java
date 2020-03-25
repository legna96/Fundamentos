package mx.filiarl.app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {

	@GetMapping("/")
	public String index() {
		return "forward:/home/index";
	}
	
	/*
	 * forward es el mismo forward de RequestDispatcher
	 * ( redigire al recurso a utilizar para el servlet, en este caso el metodo handler)
	 */
}

