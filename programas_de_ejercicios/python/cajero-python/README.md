# Cajero Python

Aplicacion de escritorio que simula un cajero realizado con la interfaz grafica TKinter y SQLite3 como base de datos embebida

El cajero incluye las operaciones basicas de retirar, depositar y consular saldo, una vez se haya ingresado mediante su nip

## Bibliotecas de Python requeridas

```
TKinter: ya incluida en python 3
sqlite3: ya incluida en python 3
pyinstaller: pip install pyinstaller
```

## Ejecutar programa

```
cd cajero-python
python main.py
```

## Generar ejecutable

```
cd cajero-python
pyinstaller --icon=presentacion/images/onepiece.ico main.spec
./dist/cajero/cajero.exe
```
### Login Test

nip activado para pruebas: 1111

## Preview

![ventana principal](https://i.ibb.co/JK7Wsyn/principal.png )
![ventana cuenta](https://i.ibb.co/GdX1vBJ/cuenta.png)
