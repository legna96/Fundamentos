package mx.filiarl.app.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/variables-en-ruta")
public class EjemploVariablesRutaController {
	
	@GetMapping({"","/"})
	public String index(Model model) {
		model.addAttribute("titulo", "Enviar parámetros de la ruta (@PathVariable)");
		return "variables/index";
	}
	
	@GetMapping("/{texto}")
    public String variables(@PathVariable String texto, Model model) {
		model.addAttribute("titulo", "Recibir parámetros de la ruta (@PathVariable)");
		model.addAttribute("resultado", "El texto enviado en la ruta es: " + texto);
		return "variables/ver";
	}

	@GetMapping("/{texto}/{numero}")
    public String variables(
    		@PathVariable String texto,
    		@PathVariable Integer numero,
    		Model model) {
		
		model.addAttribute("titulo", "Recibir parámetros de la ruta (@PathVariable)");
		model.addAttribute("resultado", "texto: " + texto + " y número: " + numero);
		
		return "variables/ver";
		
	}
	
	
	/*
	 * PathVariable: anotacion para rutas dinamicas
	 */
	
}
