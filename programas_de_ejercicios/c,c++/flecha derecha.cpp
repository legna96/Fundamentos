/*UACM SAN LORENZO TEZONCO
LUIS ALBERTO MOLINA VASQUEZ 
ESTE PROGRAMA DIBUJA UNA FLECHA CON ASTERISCOS HACIA LA IZQUIERDA
16 DE ABRIL DE 2019*/
#include <stdio.h>

main ( )

{
	int mitad,cuerpo,i,j,numero;
	
	
	printf ("\n Dame un numero: ");
	scanf("%d",&numero);
	
	while (numero < 2)
		{
		printf ("\n Con este numero nose puede dibujar una flecha intenta con otro numero");
		}
	
	int columnas = (2 * numero) ;
	int filas = (2 * numero)-1 ;
	mitad = numero - 1;
		for (j=0; j < filas; j++)
			{	
				printf("\t");
				for (i=0; i < columnas; i++)
					{
						//parte de recha es la punta
						if (i > mitad )
							{
								if (j <= mitad && i <= (columnas - numero + j ) )
									{
										printf("m");
									}
								else if (j > mitad && i <= (columnas + (2 * mitad) - (j + numero)))
									{
										printf ("M");	
									}
								else 
									{
										printf (" ");
									}
							}
						// partes izquierda el tronco
						else 
							{
								printf("I");
							}
					}
				printf("\n");
			}
}
