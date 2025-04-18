Procesador de Transacciones Financieras

Introducción
Este proyecto implementa una aplicación de línea de comandos que procesa archivos CSV con transacciones financieras (créditos y débitos) y genera un reporte con información relevante como el balance final, la transacción de mayor monto y el conteo de transacciones por tipo.
El programa fue desarrollado como parte del reto de Interbank Academy 25, con el objetivo de demostrar habilidades de procesamiento de datos y generación de reportes.

Instrucciones de Ejecución

Requisitos
----------
Python 3.6 o superior


Pasos para ejecutar la aplicación
---------------------------------
Clona el repositorio:

bashgit clone https://github.com/AlexMatheo/InterbankRetoTecnico.git
cd InterbankRetoTecnico

Ejecuta el programa:

bashpython src/main.py [ruta_al_archivo_csv]
Si no se especifica una ruta para el archivo CSV, el programa utilizará el archivo predeterminado ubicado en data/transactions.csv.


Enfoque y Solución
------------------
He implementado una solución orientada a objetos utilizando Python, creando una clase TransactionProcessor que encapsula toda la lógica de procesamiento:

Carga de datos: Lectura del archivo CSV utilizando el módulo csv de Python.
Procesamiento: Análisis de cada transacción para actualizar el balance, contadores y encontrar la de mayor monto.
Generación de reportes: Creación de un reporte formateado para mostrar en la terminal.

Para el manejo de valores monetarios, utilicé el tipo Decimal en lugar de float para evitar problemas de precisión en operaciones financieras.


Estructura del Proyecto
-----------------------

proyecto/
│
├── src/
│   ├── main.py                 # Punto de entrada de la aplicación
│   └── transaction_processor.py # Clase principal de procesamiento
│
├── data/
│   └── transactions.csv        # Archivo de ejemplo con transacciones
│
└── README.md                   # Este archivo

main.py: Maneja la interfaz de línea de comandos y utiliza la clase TransactionProcessor.
transaction_processor.py: Contiene la lógica principal para cargar, procesar y generar reportes de transacciones.
transactions.csv: Archivo de ejemplo que contiene transacciones financieras.


Mejoras Futuras
---------------
Algunas posibles mejoras para el proyecto:

Soporte para diferentes formatos de archivo (JSON, Excel, etc.)
Interfaz gráfica para visualizar los datos
Generación de reportes más detallados con gráficos
Exportación de reportes a PDF o HTML