#include <stdio.h>

int main(int argc, char *argv[])
{
  int suma = 0;
  int elementos;

  printf("dame el numero de elementos: ");
  scanf("%d", &elementos);

  int arreglo[elementos];
  printf("\n");

  for(int i = 0; i < elementos; i++)
  {
    printf("dame el elemento %d del arreglo: ", i + 1);
    scanf("%d", &arreglo[i]);
    printf("\n");

    suma = suma + arreglo[i];

    printf("La suma vale: %d \n", suma);
  }

  printf("\n\n");
  printf("total = %d", suma);
  printf("\n\n");

  return 0;
}
