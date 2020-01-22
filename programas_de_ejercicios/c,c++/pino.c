#include <stdio.h>

int main( int args, char *argv[]){

  while(1){

    int numero = 0;

    while( numero < 2){
      printf("Dame un numero: ");
      scanf("%d", &numero);

      if( numero < 2 )
        printf("Con este numero no se puede crear una flecha, Prueba con un numero mayor:");

      printf("\n");
    }

    int filas = 2 * numero;
    int columnas = (2 * numero) - 1;
    int cont = 0;
    int posNumero = numero - 1;

    int i, j;

    for(j=0; j<filas; j++ ){
      printf("\t\t");
      for(i=0; i<columnas; i++ ){

        // Arbol
        if ( j < numero ){
          if( i >= (posNumero - cont) && i <= (posNumero + cont ) )
            printf("*");
          else
            printf(" ");
        }

        // Tronco
        else {

          int inicio = posNumero / 2;
          int fin = posNumero + inicio;

          if ( posNumero%2 != 0 ){
            inicio += 1;
          }

          if( i >= inicio && i <= fin )
            printf("*");
          else
            printf(" ");
        }

      }
      printf("\n");
      cont++;
    }
    printf("\n\n");

  }
}
