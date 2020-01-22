#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int *arreglo;
int numEvaluaciones;

void llenarArreglo(){
  printf("Dime a cuantas personas vas a evaluar: ");
  scanf("%d", &numEvaluaciones );
  printf("\n");
  arreglo =  (int *) malloc(numEvaluaciones*sizeof(int));
  for(int i=0; i<numEvaluaciones; i++){
    printf("Evaluacion %d: ", i + 1);
    scanf("%d", &arreglo[i]);
  }

}

void impArreglo(int *arreglo, int numElementos) {
  printf("[\t");
  for(int i=0; i<numElementos; i++){
    printf("%d\t", arreglo[i]);
  }
  printf("]\n");
}

int maximoArreglo( int *arreglo, int numElementos ){
  int maximo = 0;

  for(int i=0; i<numElementos; i++ ){
    if (maximo < arreglo[i]){
      maximo = arreglo[i];
    }
  }
  return maximo;
}

float calcPromedio(){
  int suma = 0;
  for(int i=0; i< numEvaluaciones; i++){
    suma += arreglo[i];
  }
  return (float) suma / numEvaluaciones;
}

float calcMedia(){

  int media = ( numEvaluaciones - 1 ) / 2;
  int suma = 0;

  for(int i=0; i< numEvaluaciones; i++){

    if ( numEvaluaciones%2 != 0 && i == media ){
      return arreglo[i];
    }

    if ( numEvaluaciones%2 == 0 && (i == media || i == media + 1) ){
      suma += arreglo[i];
    }

  }

  return (float) suma / 2;

}

int calcModa(){
  int cont6 = 0;
  int cont7 = 0;
  int cont8 = 0;
  int cont9 = 0;
  int cont10 = 0;

  int *arregloVeces = (int *) malloc(5*sizeof(int));
  int contModas = 0;

  for( int i=0; i<numEvaluaciones; i++){

    if( arreglo[i] == 6 ){
      cont6++;
    }

    if( arreglo[i] == 7 ){
      cont7++;
    }

    if( arreglo[i] == 8 ){
      cont8++;
    }

    if( arreglo[i] == 9 ){
      cont9++;
    }

    if( arreglo[i] == 10 ){
      cont10++;
    }
  }

  arregloVeces[0] = cont6;
  arregloVeces[1] = cont7;
  arregloVeces[2] = cont8;
  arregloVeces[3] = cont9;
  arregloVeces[4] = cont10;

  impArreglo( arregloVeces, 5 );

  int maximo = maximoArreglo( arregloVeces, 5 );

  for (int j=0; j<5; j++){
    if( maximo == arregloVeces[j]){
      contModas++;
    }
  }

  if (contModas > 1 ){
    return -1;
  }

  else if ( maximo == cont6) {
    return 6;
  }

  else if ( maximo == cont7) {
    return 7;
  }

  else if ( maximo == cont8) {
    return 8;
  }

  else if ( maximo == cont9) {
    return 9;
  }

  else if ( maximo == cont10) {
    return 10;
  }
}

int main( int arg, char* argv[] ){

  llenarArreglo();
  float promedio = calcPromedio();
  float media = calcMedia();
  int moda = calcModa();

  impArreglo(arreglo, numEvaluaciones);
  printf("Promedio: %.2f\n", promedio);
  printf("Media: %.2f\n", media);

  if (moda == -1 ){
    printf("Hay almenos dos modas");
  }
  else {
    printf("Moda: %d\n", moda);
  }

  free(arreglo);
}
