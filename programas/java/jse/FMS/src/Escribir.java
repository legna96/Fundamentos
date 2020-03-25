import java.io.FileWriter;
import java.io.IOException;
import java.io.File;

/**
 * Escribir
 */
public class Escribir {

  public File crearArchivo(String pathFile) {

    try {

      File archivo = new File(pathFile);

      if (archivo.exists()) {
        System.err.println("Error: el archivo " + archivo.getName() + " ya existe. Por favor eliminalo y vuelve a ejecutar");
        return null;
      }

      FileWriter escritura = new FileWriter(pathFile);
      escritura.close();
      return archivo;

    } 
    
    catch (IOException e) {
      System.err.println("Error al crear archivo");
      return null;
    }

  }

  public File crearArchivoTexto(String pathFile, String texto){

    try {

      File archivo = new File(pathFile);

      if (archivo.exists()) {
        System.err.println("Error: el archivo " + archivo.getName() + " ya existe. Por favor eliminalo y vuelve a ejecutar");
        return null;
      }

      FileWriter escritura = new FileWriter(pathFile);

      for (int i = 0; i < texto.length(); i++) {
        escritura.write(texto.charAt(i));
      }

      escritura.close();
      return new File(pathFile);

    }

    catch (IOException e) {
      System.err.println("Error al crear archivo con texto");
      return null;
    }

  }

  public boolean escribirArchivo(String pathFile, String texto){

    try {

      FileWriter archivo = new FileWriter(pathFile, true);

      for (int i = 0; i < texto.length(); i++) {
        archivo.write(texto.charAt(i));
      }

      archivo.close();
      return true;

    }

    catch (IOException e) {
      System.err.println("Error al escribir archivo");
      return false;
    }

  }

}
