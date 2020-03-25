#include <stdio.h>

int main(){

  int numero, i, j, filas, columnas, posNumero;

  printf("Dame un numero: ");
  scanf("%d", &numero );

  printf("\n");

  filas = ( 2 * numero ) - 1;
  columnas = 2 * numero;
  posNumero = numero - 1;

  for (j=0; j<filas; j++){
    printf("\t\t");

    for(i=0; i<columnas; i++){

      // Punta
        if (i < numero ){
          // Parte de arriba
          if( j <= posNumero && i >= (posNumero - j) )
            printf("*");

          // Parte de abajo
          else if( j > posNumero && i >= (j - posNumero) )
            printf("*");

          else {
            printf(" ");
          }
        }

        // Cola
        else {

          int inicio = posNumero / 2;
          int fin = posNumero + inicio;

          if ( posNumero%2 != 0 ){
            inicio += 1;
          }

          if( j >= inicio && j <= fin )
            printf("*");
          else
            printf(" ");
        }


    }

    printf("\t%d\n", j);

  }


}
