# Programa ADS.

La funcionalidad de este programa es la recopilación y el guardado de información de artículos mediante llaves similares a la siguiente:

* docs(1234564789asdfghjlkjqwerrtey)

Para esta tarea se utiliza la [API](https://ui.adsabs.harvard.edu/help/api/api-docs.html#overview) del [astrophysics data system](https://ui.adsabs.harvard.edu).

## Requerimientos.

Para este programa se utilizó Python como lenguaje de programación, por lo tanto requiere las siguientes cosas:

* python3.10
* módulos: requests, mariadb y python-dotenv

## Funcionamiento Básico.

El funcionamiento básico del programa es el siguiente:

* Contamos con nuestra interfaz principal, que en la que va a realizar todo el trabajo.

![Imagen1](https://github.com/RaulEstram/ImagenesREADME/blob/main/ADS%20README/Imagen1.png)

* Ingresamos nuestra llave en el cuadro de texto.

![Imagen2](https://github.com/RaulEstram/ImagenesREADME/blob/main/ADS%20README/Imagen2.png)

* Posteriormente damos click en el botón de **buscar** para obtener los resultados de la búsqueda con la llave.

![Imagen3](https://github.com/RaulEstram/ImagenesREADME/blob/main/ADS%20README/Imagen3.png)

* Posteriormente podemos guardar la información en una base de datos usando el botón **Guardar**, el cual nos pedirá el **nombre del autor** de los artículos, para posteriormente aceptar o cancelar la acción.

![Imagen4](https://github.com/RaulEstram/ImagenesREADME/blob/main/ADS%20README/Imagen4.png)

* Una vez que se guardó la información podemos verificar que se guardara adecuadamente en nuestra base de datos.

![Imagen5](https://github.com/RaulEstram/ImagenesREADME/blob/main/ADS%20README/Imagen5.png)

## Funcionalidades Extra

también tenemos funcionalidades extras en esta interfaz las cuales son:

* Previsualizar los queries que se usaran para guardar la información en la base de datos.

* Guardar la información proporcionada en un archivo de texto.


## Base de datos.

la base de datos que se está utilizando para este ejemplo es una base de datos muy chica, la cual se puede crear con el siguiente Código SQL:

```sql
DROP TABLE if EXISTS `DatosADS`;

CREATE TABLE `DatosADS` ( 
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT, 
  `autores` VARCHAR(200) NULL DEFAULT NULL , 
  `title` VARCHAR(300) NOT NULL , 
  `pub` VARCHAR(200) NOT NULL , 
  `bibcode` VARCHAR(50) NOT NULL UNIQUE, 
  `doi` VARCHAR(50) NOT NULL UNIQUE, 
  `fpage` VARCHAR(10) NULL DEFAULT NULL , 
  `lpage` VARCHAR(10) NULL DEFAULT NULL , 
  `volumen` VARCHAR(50) NULL DEFAULT NULL , 
  `year` VARCHAR(4) NULL DEFAULT NULL , 
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;
```

