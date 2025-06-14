# Transformador a MiniZinc

Esta aplicación proporciona una interfaz gráfica para transformar datos de ciudades en código MiniZinc para resolver problemas de optimización.

## Descripción

La aplicación permite ingresar datos de ciudades (nombre y coordenadas) y genera automáticamente el código MiniZinc correspondiente para resolver problemas de optimización relacionados con estas ciudades.

## Requisitos

- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)
- MiniZinc (para ejecutar los modelos generados)

## Instalación

Clona este repositorio:

```bash
git clone [URL_DEL_REPOSITORIO]
```

## Uso

1. Ejecuta la aplicación:

```bash
python main.py
```

2. En la interfaz gráfica:

   - En el panel izquierdo, ingresa los datos en el siguiente formato:

     ```
     N
     M
     Ciudad1 X1 Y1
     Ciudad2 X2 Y2
     ...
     CiudadM XM YM
     ```

     Donde:

     - N: Tamaño de la cuadricula
     - M: Número de ciudades
     - Ciudad: Nombre de la ciudad
     - X, Y: Coordenadas de la ciudad

   - Haz clic en "Generar MiniZinc"
   - El código MiniZinc generado aparecerá en el panel derecho

## Formato de Entrada

Ejemplo de entrada válida:

```
12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2
```

# Autores

- [Isabella Rebellón Medina](https://github.com/Issabella09) - [Email](mailto:isabella.rebellon@correounivalle.edu.co)
- [Jose Luis Ramos Arango](https://github.com/RamSterB) - [Email](mailto:jose.luis.ramos@correounivalle.edu.co)
- [Juan Sebastian Marin Serna](https://github.com/JSebastianMarin) - [Email](mailto:juan.marin.serna@correounivalle.edu.co)
- [Juan Pablo Idarraga](https://github.com/JuanPidarraga) - [Email](mailto:idarraga.juan@correounivalle.edu.co)
