import java.io.File;

/**
 * App
 */
public class App {

  public static void main(String[] args) {

    /*********************************************/
    // Mis objetos para leer y escribir archivos //
    /*********************************************/

    Leer lectura = new Leer();
    Escribir escritura = new Escribir();

    /*************************/
    // Rutas de los archivos //
    /*************************/

    // proceso un archivo nuevo
    File archivoNuevo = escritura.crearArchivo("src/nuevo.txt");

    if (archivoNuevo != null) {
      System.out.println("Se ha creado el archivo " + archivoNuevo.getName() + " en la ruta " + archivoNuevo.getAbsolutePath());
    }

    // proceso un archivo nuevo pero con texto
    File archivoNuevoTexto = escritura.crearArchivoTexto("src/nuevo-con-texto.txt", "Hola Mundo");

    if (archivoNuevoTexto != null) {
      System.out.println("Se ha creado el archivo " + archivoNuevoTexto.getName() + " en la ruta " + archivoNuevoTexto.getAbsolutePath());
    }

    if ( archivoNuevo == null || archivoNuevoTexto == null) {
      return;
    }

    // proceso un archivo que ya debe existir en el proyecto
    File archivoTexto = new File("src/archivo-texto-ya-existente.txt");


    /**********************/
    // Flujo del programa //
    /**********************/

    // Escribo en los archivos el texto del archivo ya exitente
    String texto = lectura.leerArchivo(archivoTexto.getAbsolutePath());
    System.out.println("\n");

    if (escritura.escribirArchivo(archivoNuevo.getAbsolutePath(), texto)) {
      System.out.println("Archivo Nuevo escrito correctamente");
    }

    if (escritura.escribirArchivo(archivoNuevoTexto.getAbsolutePath(), texto)) {
      System.out.println("Archivo Nuevo con Texto escrito correctamente");
    }

  }
}
