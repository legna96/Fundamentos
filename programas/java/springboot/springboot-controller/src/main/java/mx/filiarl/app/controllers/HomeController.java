package mx.filiarl.app.controllers;
import java.util.Arrays;
import java.util.List;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import mx.filiarl.app.models.Usuario;


@Controller
@RequestMapping("/home")
public class HomeController {
	
	/**
	 * inyecta valores del textos properties
	 */
	@Value("${texto.indexcontroller.index.titulo}")
	private String textoIndex;
	@Value("${texto.indexcontroller.perfil.titulo}")
	private String textoPerfil;
	@Value("${texto.indexcontroller.listar.titulo}")
	private String textoListar;
	
	/**
	 * Se agrega un elemento usuarios al modelo
	 * este elemento es visible para cada metodo handler
	 * @return usuarios
	 */
	@ModelAttribute("usuarios")
	public List<Usuario> poblarUsuarios(){
		
		List<Usuario> usuarios = 
				Arrays.asList(
						new Usuario("Andrés", "Guzmán", "andres@correo.com"),
						new Usuario("John", "Doe", "john@correo.com"),
						new Usuario("Jane", "Doe", "jane@correo.com"),
						new Usuario("Tornado", "Roe", "roe@correo.com")
				);
		
		return usuarios;
	}
	
	// Metodos Handlers (manejadores de rutas)

	//mapea para distintas url
	@GetMapping(value={"/index", "/"}) //anotacion detallada
	//@GetMapping({"/index", "/"}) //anotacion no detallada
	public String index(Model model) {
		model.addAttribute("titulo", textoIndex);
		return "index";
	}
	
	// mapea una sola url
	@GetMapping("")
	public String index2(Model model) {
		model.addAttribute("titulo", textoIndex);
		return "index";
	}
	
	@RequestMapping(value="/perfil", method=RequestMethod.GET) //anotacion detallada
	//@RequestMapping("/perfil") //anotacion no detallada. RequestMapping por defecto es tipo GET
	public String perfil(Model model) {
		
		Usuario usuario = new Usuario();
		usuario.setNombre("Andrés");
		usuario.setApellido("Guzmán");
		usuario.setEmail("andres@correo.com");
		
		model.addAttribute("usuario", usuario);
		model.addAttribute("titulo", textoPerfil.concat(usuario.getNombre()));
		
		return "perfil";
	}
	
	@RequestMapping("/listar")
	public String listar(Model model) {
		model.addAttribute("titulo", textoListar);
		return "listar";
	}
	
	/**
	 * RequestMapping a una clase controller se vuele una pre-ruta para cada metodo handler
	 * RequestMapping en metodo handler se vuelve la url ala que se apunta el metodo
	 * RequestMapping es una anotacion generica, se debe indicar el verbo http sino por defecto es GET
	 * GetMapping
	 * PostMapping
	 * PutMapping
	 * DeleteMapping
	 */

}