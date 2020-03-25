import java.io.FileReader;
import java.io.IOException;

/**
 * Leer
 */
public class Leer {

  public String leerArchivo(String pathFile) {

    try {

      String cadena = "";
      FileReader entrada = new FileReader(pathFile);

      int c = -1000;

      while (c != -1) {
        c = entrada.read();
        cadena += (char) c;
      }

      entrada.close();
      return cadena;
    }

    catch (IOException e) {
      return "Error al leer archivo";
    }
  }

}
