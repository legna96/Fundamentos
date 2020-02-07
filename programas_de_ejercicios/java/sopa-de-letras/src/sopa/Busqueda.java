package sopa;

import java.util.ArrayList;
import java.util.List;

public class Busqueda {

	 char[][] matriz = {
			{ 'i', 'j', 's', 'i', 'j', 'a', 't', 'a', 'a', 'd', 'e', 'u', 'q', 's', 'u', 'b'}, 
			{ 'e', 'k', 'y', 'c', 'f', 's', 'q', 'c', 'g', 'b', 'u', 'w', 's', 'ñ', 'o', 'p'},
			{ 'j', 'i', 'o', 'g', 'r', 'n', 'o', 'i', 'c', 'a', 'l', 'u', 'm', 'i', 's', 'r'},
			{ 'a', 'a', 'n', 'w', 'a', 'e', 'f', 'g', 'l', 'e', 'x', 'i', 'p', 'h', 'l', 'o'},
			{ 'z', 'b', 'a', 't', 'm', 'k', 'e', 'o', 'e', 'e', 'h', 'i', 'k', 'd', 'n', 'l'},
			{ 'i', 'n', 'i', 'o', 'e', 'p', 'f', 'l', 'n', 'u', 'a', 'p', 'r', 'a', 'r', 'o'}, 
			{ 'd', 'a', 'p', 'ñ', 'c', 'l', 'd', 'l', 'd', 'k', 'j', 'a', 'k', 't', 'z', 'g'},
			{ 'n', 'r', 'o', 'b', 'o', 't', 'i', 'c', 'a', 'a', 'k', 'e', 'l', 'a', 'a', 'w'},
			{ 'e', 'v', 't', 'i', 'u', 'p', 'p', 'g', 'v', 'c', 'h', 'r', 't', 'r', 't', 'm'},
			{ 'r', 'k', 'u', 'r', 'o', 'a', 'b', 'a', 'e', 'v', 'i', 'a', 'l', 'i', 'p', 'o'},
			{ 'p', 'm', 'i', 'n', 'c', 'r', 'q', 'd', 'f', 'n', 'z', 't', 'j', 'i', 'p', 'e'},
			{ 'a', 'n', 'g', 'm', 't', 'e', 'n', 'y', 'k', 's', 'c', 'j', 'e', 'f', 's', 'x'},
			{ 'g', 'd', 'a', 'd', 'i', 'n', 'a', 'm', 'u', 'h', 'e', 'i', 'm', 'n', 'n', 'p'},
			{ 'u', 'n', 's', 'b', 'u', 'z', 'a', 's', 'c', 'i', 'h', 'p', 'a', 'r', 'e', 'y'},
			{ 'i', 'p', 'y', 'o', 't', 'n', 'e', 'i', 'm', 'a', 'n', 'o', 'z', 'a', 'r', 'g'},
			{ 'a', 'c', 'i', 't', 'a', 'm', 'r', 'o', 'f', 'n', 'i', 'o', 'i', 'b', 'r', 't'},};




	public boolean buscarpalabra(String palabra) {

		for (int[] pos : posiblesSolucionesDe(palabra)) {

			// Buscar horizontalmente hacia derecha.
			String palabraEncontrada = palabraEnMatriz(pos, palabra.length(), 0, 1);
			if (palabraEncontrada.equals(palabra))
				return true;

			// Buscar horizontalmente hacia izquierda.
			palabraEncontrada = palabraEnMatriz(pos, palabra.length(), 0, -1);
			if (palabraEncontrada.equals(palabra))
				return true;

			// Buscar verticalmente hacia abajo.
			palabraEncontrada = palabraEnMatriz(pos, palabra.length(), 1, 0);
			if (palabraEncontrada.equals(palabra))
				return true;

			// Buscar verticalmente hacia arriba.
			palabraEncontrada = palabraEnMatriz(pos, palabra.length(), -1, 0);
			if (palabraEncontrada.equals(palabra))
				return true;

			// Buscar diagonal superior derecha.
			palabraEncontrada = palabraEnMatriz(pos, palabra.length(), -1, 1);
			if (palabraEncontrada.equals(palabra))
				return true;

			// Buscar diagonal superior izquierda.
			palabraEncontrada = palabraEnMatriz(pos, palabra.length(), -1, -1);
			if (palabraEncontrada.equals(palabra))
				return true;

			// Buscar diagonal inferior derecha.
			palabraEncontrada = palabraEnMatriz(pos, palabra.length(), 1, 1);
			if (palabraEncontrada.equals(palabra))
				return true;

			// Buscar diagonal inferior izquierda.
			palabraEncontrada = palabraEnMatriz(pos, palabra.length(), 1, -1);
			if (palabraEncontrada.equals(palabra))
				return true;
		}

		return false;
	}

	/*
	 * Retorna indice invertido de las posiciones donde puede resolverse una
	 * palabra buscada.
	 */
	public int[][] posiblesSolucionesDe(String palabra) {
		char primeraLetra = palabra.charAt(0);
		List<int[]> indiceInvertido = new ArrayList<int[]>();

		for (int i = 0; i < matriz.length; i++) {
			for (int j = 0; j < matriz[i].length; j++) {
				if (matriz[i][j] == primeraLetra) {
					indiceInvertido.add(new int[] { i, j }); // Guardar la
																// posicion de
																// la letra en
																// la matriz.
				}
			}
		}
		
		return toArrayInt(indiceInvertido);
	}

	// Transforma un objeto List a un multi arreglo de numeros enteros.
	 
	 int[][] toArrayInt(List<int[]> list) {
		return (int[][]) list.toArray(new int[list.size()][list.get(0).length]);
	}

	
//	  Algoritmo que busca palabras en la matriz
	 
	public String palabraEnMatriz(int[] posInicial, int numeroCaracteres, int moverEnFila, int moverEnColumna) {
		String palabra = "";
		int recorrido = 0, fila = posInicial[0], columna = posInicial[1];

		while ((recorrido < numeroCaracteres) && (fila < matriz.length && columna < matriz.length)
				&& (fila > -1 && columna > -1)) {

			palabra += matriz[fila][columna];
			fila = fila + moverEnFila;
			columna = columna + moverEnColumna;
			recorrido++;
		}

		return palabra;
	}

	public long tiempo(long t_final, long t_inicial){
		return (t_final-t_inicial);
		
	}
	
}
