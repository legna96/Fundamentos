package mx.arl96.models;

public class Form {

	private String nombre;
	private int edad;
	private String sexo;
	private String ocupacion;
	
	
	public Form(String nombre, int edad, String sexo, String ocupacion) {
		this.nombre = nombre;
		this.edad = edad;
		this.sexo = sexo;
		this.ocupacion = ocupacion;
	}


	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public int getEdad() {
		return edad;
	}


	public void setEdad(int edad) {
		this.edad = edad;
	}


	public String getSexo() {
		return sexo;
	}


	public void setSexo(String sexo) {
		this.sexo = sexo;
	}


	public String getOcupacion() {
		return ocupacion;
	}


	public void setOcupacion(String ocupacion) {
		this.ocupacion = ocupacion;
	}
	
	
	@Override
	public String toString() {
		return "Form [nombre=" + nombre + ", edad=" + edad + ", sexo=" + sexo + ", ocupacion=" + ocupacion + "]";
	}
	
}
