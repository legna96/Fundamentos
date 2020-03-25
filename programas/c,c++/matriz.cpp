#include <stdio.h>

int main(){

  int filas, columnas;

  printf("dame las filas: ");
  scanf("%d", &filas);

  printf("\n");

  printf("dame las columnas: ");
  scanf("%d", &columnas);

  int matriz[columnas][filas];
  int i,j;

  for (j = 0; j < filas; j++)
  {
    for (i = 0; i < columnas; i++)
    {
      printf("Dame el numero para la posicion [ %d, %d ] de la caja: ", j, i);
      scanf("%d", &matriz[i][j] );
      printf("\n");
    }
  }

  for ( j = 0; j < filas; j++)
  {
    printf("[\t");
    for ( i = 0; i < columnas; i++)
    {
      printf("%d\t", matriz[i][j]);
    }
    printf("]\n");
  }


}
