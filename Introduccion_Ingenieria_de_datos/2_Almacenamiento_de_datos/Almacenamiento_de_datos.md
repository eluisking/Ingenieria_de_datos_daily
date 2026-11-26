# Almacenamiento de Datos

Usualmente en el almacenamiento de Datos podemos guardarlos de tres maneras diferente.

1. **Datos Estructurados**: Estos en bases de datos SQL, en donde tienen un orden por tablas con su propia estructura para definir la organizacion.
2. **Datos Semi-Estructurados**: Estos son guardaos principalmete en Bases de Datos NoSQL, en formatos como Json, XML entre otros, brindan mas flexibilidad pero tabien son mas propensos al desorden y esto es una limitante cuando existe mucha data.
3. **Datos No Estructurados**: Estos son almacenados en lakes de datos como S3 o alamcenes de datos generales, la informacion que se suele  guardar aqui son video, imagenes o archivos similares.

## Bases de Datos SQL
 SQL: Structure, Query, Language.
 
 SQL es el lenguaje con el que nos vamos a comunicar a las bases de datos, ya sea para crear o modificar la estructura o datos de la misma DB o para consultar datos.

 ## Data Lake vs Data Warehouse.
 Data Lake:
 - Se almacenan los datos en bruto.
 - Datos sin procesar y tal vez desordenados.
  - Estos pueden ser extremadamente grandes en volumen.
  - Almacena cualquier tipo de datos (Etructurados, Semi Estructurados o no estructurados).
  - Dificiles de analizar.

 DaTa Warehouse:
 - Almacena datos especificos para un uso concreto.
- Estos acomparacion con los Data Lake son pequenos.
- Almacenan mayormente Datos Estructurados.
- Costosos de actualizar.
- Optimizados para el analisis.