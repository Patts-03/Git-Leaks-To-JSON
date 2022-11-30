# Generación de archivo json de leaks

Creamos una ETL que extraiga los leaks de los commits de un repositorio Git a elección del usuario.

Una vez decidido el repositorio , a la vez que extraemos los leaks de los commits que coinciden con alguna de las palabras clave definidas en el programa, vamos creando un archivo tipo .json. 

Este estará estructurado en torno a las palabras clave elegidas, que serán las claves para los distintos leaks que contengan dicha palabra.
