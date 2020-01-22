package main

import "fmt"

/**
* Hilo principal main
**/
func main() {
	// Declaraciones estaticas
	var nombre string
	var edad int
	var estatura float64
	var banderaFalse bool

	nombre = "Angel"
	edad = 22
	estatura = 1.70
	banderaFalse = false

	// Declaraciones implicitas (Duck Type)
	apat := "Rebollo"
	amat := "López"
	banderaTrue := true

	fmt.Println("=================================")
	fmt.Println("=====   Mi Perfil \"printf\"  =====")
	fmt.Println("=================================")
	fmt.Printf("\t+ Nombre: %s :)\n", nombre)
	fmt.Printf("\t+ Paterno: %s\n", apat)
	fmt.Printf("\t+ Materno: %s\n", amat)
	fmt.Printf("\t+ Edad: %d\n", edad)
	fmt.Printf("\t+ Estatura: %.2f xD\n", estatura)

	print("\n\n")

	fmt.Println("==================================")
	fmt.Println("=====   Mi Perfil \"println\"  =====")
	fmt.Println("==================================")
	// Interpolacion con "+" se puede pero me da errores con flotantes
	fmt.Println("\t+ Nombre: " + nombre + " :)")
	fmt.Println("\t+ Paterno: ", apat)
	fmt.Println("\t+ Materno: ", amat)
	fmt.Println("\t+ Edad: ", edad)
	// Interpolacion con "," es preferible usar esta interpolacion por el momento
	fmt.Println("\t+ Estatura: ", estatura, "xD")

	print("\n\n")

	fmt.Println("=============================")
	fmt.Println("=====   Mis Banderitas  =====")
	fmt.Println("=============================")
	fmt.Println("Bandera Falsa: ", banderaFalse)
	fmt.Println("Bandera Verdadera: ", banderaTrue)

	// Cambio de Banderas
	print("\n\n")
	banderaFalse, banderaTrue = true, false

	fmt.Println("=============================")
	fmt.Println("=====   Mis Banderitas  =====")
	fmt.Println("=============================")
	fmt.Println("Bandera Falsa: ", banderaFalse)
	fmt.Println("Bandera Verdadera: ", banderaTrue)

	// Banderas nuevas con declaracion implicita de forma multiple
	print("\n\n")
	verdadero, falso := true, false

	fmt.Println("=============================")
	fmt.Println("=====   Mis Banderitas  =====")
	fmt.Println("=============================")
	fmt.Println("Verdadero: ", verdadero)
	fmt.Println("Falso: ", falso)

	// declaracion implicita de forma multiple variables nuevas y existentes
	print("\n\n")
	banderaFalse, saludo, edad := false, "Hola soy Goku!", 23

	fmt.Println("=============================")
	fmt.Println("=====   Alternados :)   =====")
	fmt.Println("=============================")
	fmt.Println("Bandera Falsa: ", banderaFalse)
	fmt.Println("Saludo: ", saludo)
	fmt.Println("Edad: ", edad)

	for 1 > 0 {
	}
}
