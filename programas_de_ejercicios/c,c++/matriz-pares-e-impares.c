#include <stdio.h>
#include <stdlib.h>

int main(int args, char *argv[]){

  while(1){
    int **matriz;
    int filas;
    int columnas;

    printf("Numero de filas: ");
    scanf("%d", &filas);
    printf("Numero de columnas: ");
    scanf("%d", &columnas);
    printf("\n");

    /******* Crear Matriz ***********/
    // pedir memoria para matriz, (tener n filas cada una de tamano int* [arreglo] )
    matriz = (int**) malloc(filas * sizeof(int*));

    // pedir memoria para cada arreglo, (tener n columnas [numero de elementos del arreglo] cada una de tamano int
    for (int i=0; i<filas; i++){
      matriz[i] = (int*) malloc(columnas * sizeof(int) );
    }

    // Llenar matriz con 1's [ llenado default ]
    for( int j=0; j<filas; j++ ){
      for ( int i=0; i<columnas; i++ ){
        matriz[j][i] = 1;
      }
    }

    // llenarMatriz con la config de Luis, pero poniendo 0's en vez de X
    for( int j=0; j<filas; j++ ){
      for(int i=0; i<columnas; i++ ){

        // Fila Par
        if ( j%2 == 0){

          // Estoy dentro de una fila Par

          if ( i%2 != 0 ){
            // Estoy en una fila Par y un elemento ImPar
            matriz[j][i]= 0;
          }

        }

        // Fila imPar
        else {
          // Estoy dentro de una fila Impar

          if ( i%2 == 0) {
            // Estoy en una fila Impar y un elemento Par
            matriz[j][i]= 0;
          }
        }

      }
    }

    // imprimirMatriz
    for( int j=0; j<filas; j++ ){
      printf("[\t");
      for ( int i=0; i<columnas; i++ ){
        printf("%d\t", matriz[j][i]);
      }
      printf("]\n");
    }

    printf("\n\n");
  }

}
