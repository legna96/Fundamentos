package mx.filiarl.app.servicio;

import org.springframework.stereotype.Component;

import mx.filiarl.app.interfaces.ITareas;

@Component("servicioAlumnoSociales")
public class AlumnoSocialesService implements ITareas{

	@Override
	public String trabajo() {
		return "Entrega un reporte escrito";
	}

}
