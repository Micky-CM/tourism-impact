# Tourism Impact

Este proyecto ayuda a entender el impacto que tiene el turismo en la economía de los países. Para este fin, tiene por función realizar una gráfica de barras que muestra el histórico de los ingresos por turismo del país que se ingrese por consola durante el periodo de 2010 a 2020.

Para correr el programa debes seguir las siguientes instrucciones en la terminal:

```sh
git clone
pip install matplotlib
python3 main.py
```
El programa te pedirá que introduzcas el nombre de un país y al presionar enter, generará una gráfica correspondiente en formato png y la almacenará en el directorio 'images'.


Nota: La base de datos utilizada, contiene datos desde el año 1999 a 2023, pero realiza los gráficos solamente del periodo de 2010 a 2020 por dos razones: 1) En muchos casos los datos de 2021 a 2023 están vacíos en varios países, y 2) El gráfico se hace menos legible cuando se visualizan muchas gestiones.