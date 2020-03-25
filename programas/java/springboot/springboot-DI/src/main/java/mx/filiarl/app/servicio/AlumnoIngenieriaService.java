package mx.filiarl.app.servicio;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

import mx.filiarl.app.interfaces.ITareas;

@Component("servicioAlumnoIngeniera")
@Primary
public class AlumnoIngenieriaService implements ITareas {

	@Override
	public String trabajo() {
		return "Entrega algun proyecto";
	}

}
