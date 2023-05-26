# DETECCION AUTOMATICA DE ACTOS DE CORRUPCION EN CONTRATOS

## Proyecto de Grado - Detección de Corrupción en Contratos mediante Analítica de Datos
¡Bienvenido al repositorio del proyecto de grado! En este proyecto, nos enfocamos en abordar el problema de la corrupción en los contratos a través del uso de analítica de datos avanzada.

La corrupción en los contratos es una preocupación significativa en numerosos sectores y puede tener consecuencias negativas en términos de desigualdad, pérdida de recursos y falta de transparencia. Para combatir este problema, hemos desarrollado una solución basada en la aplicación de modelos de inteligencia artificial y técnicas de análisis de datos.

Nuestra solución se basa en la detección de patrones y anomalías en el proceso de contratación mediante el uso de analítica de datos. Al recopilar y analizar los datos relevantes, nuestra plataforma de analítica puede identificar automáticamente comportamientos sospechosos o patrones inusuales en los contratos. Por ejemplo, el sistema puede alertar sobre contratos otorgados repetidamente a un solo proveedor o precios extremadamente por encima del promedio.

En este repositorio, encontrará toda la documentación necesaria para comprender y utilizar nuestra solución. Además, proporcionamos instrucciones detalladas sobre cómo implementar y configurar la plataforma de analítica de datos en su entorno. También incluimos ejemplos de datos de muestra y scripts para facilitar el proceso de prueba y demostración.

Esperamos que este proyecto contribuya a una mayor transparencia y rendición de cuentas en el ámbito de los contratos, y que nuestra solución pueda ser utilizada en diversos sectores para prevenir y detectar la corrupción. ¡Gracias por su interés en nuestro proyecto de grado y bienvenido a bordo!

Equipo de proyecto

Portal web: [Accede al portal](https://reporte-procesos.azurewebsites.net/)

Reporte de PowerBI directo: [Reporte de Power BI](https://app.powerbi.com/view?r=eyJrIjoiZGU2MWYwMzAtYWZiOC00OGZlLTk1MDItNTNhMTE0NGVhMTljIiwidCI6IjVmZmIyOTg2LTQ2MDctNDQwZS1iYjBmLWQyYjlmZmU2NjZlOSIsImMiOjR9)

Datos oficiales utilizados: [Datos abiertos CSV](https://www.datos.gov.co/resource/tb27-zmix.csv) | [Información del dataset](https://www.datos.gov.co/Gastos-Gubernamentales/Contratos-Secop-II/tb27-zmix)

Aplicacion de ETL desarrollada para Azure Function [Codigo de la aplicación](https://github.com/jboca-andes/proyecto-grado/tree/main/andes-proyecto-grado)

Aplicacion para la captura de votos de la ciudadania, desarrollada en Python y Flask [Codigo de la aplicación](https://github.com/jboca-andes/proyecto-grado/tree/main/reporte-contratos)

Artefactos [Carpeta de artefactos](https://github.com/jboca-andes/proyecto-grado/tree/main/Artefactos)

### Tabla de requerimientos

| Aspecto   | Requerimiento                                                                                                                                                | Prueba Prevista                                                                                                               | Criterio o Metrica de evaluacion y rangos deseados                                                                   | Resultado | Prueba                                                                                                                                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Negocio   |                                                                                                                                                              |                                                                                                                               |                                                                                                                      |           |                                                                                                                                                                                                                                                          |
| R1        | Visualizar las inversiones en infraestructura en un tablero de control                                                                                       | Se visualizan las inversiones tanto en dinero como en cantidades                                                              | Cumple                                                                                                               | Cumple    | [Ver reporte](https://app.powerbi.com/view?r=eyJrIjoiZGU2MWYwMzAtYWZiOC00OGZlLTk1MDItNTNhMTE0NGVhMTljIiwidCI6IjVmZmIyOTg2LTQ2MDctNDQwZS1iYjBmLWQyYjlmZmU2NjZlOSIsImMiOjR9)                                                                                                                                                                                                                                                     |
| R2        | Identificar posibles contratos "sospechosos" o atipicos                                                                                                      | Se marcan aquellos contratos considerados como "sospechosos"                                                                  | Criterios robustos para distribución empírica de los datos, dato fuera del 95% en la distribución empírica acumulada | No Cumple | Aunque se llegan a resultados muy exactos, se marca menos del uno porciento de los datos según el error en predicción vs el precio real. Los datos de predicción de precios no se pudo llegar a lo deseado (con un 0.89 de R2 en el modelo implementado), con el fin de solventar esto, se implemento una estrategia de votos sobre contratos que la comunidad considere sospechosos, esto permitiría en el futuro complementar este tipo de modelos ![Imagen](https://github.com/jboca-andes/proyecto-grado/blob/main/Imagenes/SistemaVotos.png?raw=true) |
| R3        | Habilitar a los ciudadanos en la visualizacion y consumo de estos datos                                                                                      | Se puede ingresar desde cualquier lugar a visualizar el tablero de control utilizando un computador y una conexión a internet | Cumple                                                                                                               | Cumple    | [Ver reporte](https://app.powerbi.com/view?r=eyJrIjoiZGU2MWYwMzAtYWZiOC00OGZlLTk1MDItNTNhMTE0NGVhMTljIiwidCI6IjVmZmIyOTg2LTQ2MDctNDQwZS1iYjBmLWQyYjlmZmU2NjZlOSIsImMiOjR9)                                                                                                                                                                                                                                                     |
| R4        | Facilitar la identificación de contratos a los que amerite realizar seguimiento detallado                                                                    | Se identifican en el tablero mediante otro color aquellos "sospechosos"                                                       | Se evidencia visualmente porque esos contratos son atípicos                                                          | Cumple    | ![Imagen](https://raw.githubusercontent.com/jboca-andes/proyecto-grado/c59ab78fb53ec42958645f439586c4b279a66b1c/Imagenes/Evidencia%20contratos%20extra%C3%B1os.png)                                                                                                                                                                                                                                                     |
| Desempeño |                                                                                                                                                              |                                                                                                                               |                                                                                                                      |           |                                                                                                                                                                                                                                                          |
| R5        | Desplegar el tablero de control en cualquier navegador basado en Chromium                                                                                    | Se despliega en Chrome, Edge, Firefox y Brave                                                                                 | Cumple                                                                                                               | Cumple    | [Ver evidencia](https://github.com/jboca-andes/proyecto-grado/blob/main/Navegadores.md)                                                                                                                                                                                                                                                    |
| R6        | Realizar la prediccion en menos de 20 segundos en el API                                                                                                     | Se usa Postman y se toman tiempos de prediccion                                                                               | Tiempo < 20 segundos                                                                                                 | Cumple    | ![Imagen](https://raw.githubusercontent.com/jboca-andes/proyecto-grado/main/Imagenes/Postman.webp)                                                                                                                                                                                                                                                     |
| R7        | Desplegar el tablero de control en menos de 30 segundos en los dispositivos de los usuarios                                                                  | Se realizan mediciones desde un computador utilizando herramientas de desarrollo del navegador                                | Tiempo < 30 segundos                                                                                                 | Cumple    | [Ver análisis de rendimiento](https://www.webpagetest.org/result/230526_BiDc4K_9DZ/1/details/#waterfall_view_step1)                                                                                                                                                                                                                                                     |
| R8        | Actualizar la informacion en menos de 2 horas desde la publicacion de los datos actualizados                                                                 | Se ejecuta todo el proceso de ETL / ELT para calcular los tiempos                                                             | Tiempo < 2 horas                                                                                                     | Cumple    | ![Imagen](https://github.com/jboca-andes/proyecto-grado/blob/main/Imagenes/EjecucionETL.png?raw=true)                                                                                                                                                                                                                                                     |
| Funcional |                                                                                                                                                              |                                                                                                                               |                                                                                                                      |           |                                                                                                                                                                                                                                                          |
| R9        | Interfaz para dispositivos tipo laptop o de escritorio para el consumo de dicha informacion                                                                  | Se prueba desde dispositivos Windows y MAC                                                                                    | Cumple                                                                                                               | Cumple    | [Ver evidencia](https://github.com/jboca-andes/proyecto-grado/blob/main/Navegadores.md)                                                                                                                                                                                                                                                           |
| R10       | Se debe exponer un servicio REST que realice las predicciones dadas las entradas del Objeto del contrato, Entidad contratante, monto y duración del contrato | Se realizan pruebas desde Postman                                                                                             | Cumple                                                                                                               | Cumple    | ![Imagen](https://github.com/jboca-andes/proyecto-grado/blob/main/Imagenes/PruebaAPI2.png?raw=true)                                                                                                                                                                                                                                                     |
### Mockups

| Inicial                                 | 
|:-----------------------------------------:|
| ![Inicial](https://github.com/jboca-andes/proyecto-grado/blob/main/Imagenes/Mockup%20animado.gif?raw=true) |
| Desplegado|
|![Desplegado](https://github.com/jboca-andes/proyecto-grado/blob/main/Imagenes/Desplegado.gif?raw=true)|

### Arquitectura del proyecto
![Arquitectura](https://github.com/jboca-andes/proyecto-grado/blob/main/Imagenes/Arquitectura%20desplegada.png?raw=true)

### Video de presentación
[![Mira el video](https://uniandes.edu.co/sites/default/files/logo-uniandes.png)](https://youtu.be/f2Z05TI9y4Y)


#### Aviso de licenciamiento

La Licencia Creative Commons Zero Universal 1.0 (CC0) es una licencia de derechos de autor que proporciona una forma simple y efectiva para que los creadores renuncien a sus derechos de autor y coloquen sus obras en el dominio público. CC0 es una licencia irrevocable y no exclusiva, lo que significa que una vez que una obra está bajo CC0, cualquiera puede utilizarla de cualquier manera sin restricciones.

A continuación, se detallan algunos aspectos clave de la Licencia Creative Commons Zero Universal 1.0:

Renuncia de derechos: El titular de los derechos de autor renuncia a todos sus derechos sobre la obra en la medida permitida por la ley. Esto significa que la obra puede ser utilizada, copiada, modificada, distribuida y utilizada con fines comerciales sin necesidad de obtener permiso o atribución al autor original.

Dominio público: Al colocar una obra bajo la licencia CC0, el autor la coloca en el dominio público, lo que significa que la obra no está sujeta a derechos de autor y se puede utilizar libremente por cualquier persona.

Licencia global: CC0 es una licencia universal, lo que significa que se aplica en todo el mundo y no está limitada a una jurisdicción específica.

Irrevocable: Una vez que una obra se coloca bajo CC0, no se puede retirar. La renuncia de derechos es permanente e irrevocable.

Sin garantías: La licencia CC0 se proporciona "tal cual", sin garantías de ningún tipo. El titular de los derechos de autor no ofrece ninguna garantía en cuanto a la exactitud, la calidad o la idoneidad de la obra para un propósito específico.

Reconocimiento voluntario: Aunque no se requiere atribución, CC0 alienta a aquellos que utilicen una obra a proporcionar reconocimiento al autor original de manera voluntaria.
