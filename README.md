# ProyectoCC-16-17
Repositorio para proyecto de la asignatura Cloud Computing.

## MusicSpace

### Descripción del problema

Somos muchas las personas amantes de la música que no disponemos de una plataforma que nos proporcione información y permita preescuchar albumes. Si a esto añadimos que las webs existentes están ancladas en los mismos estilos, surge la necesidad de realizar una web que abarque estilos más minoritarios de música. Por ello surge MusicSpace.

Mi intención con esta aplicación web es satisfacer la necesidad de todas aquellas personas que deseen poder acceder a una aplicación web con una interfaz atractiva, novedosa, multiplataforma y eficiente.

### Arquitectura de desarrollo

MusicSpace sigue una arquitectura microkernel, ya que todos los servicios se ejecutan desde la misma máquina. Por tanto, es el núcleo central el que se comunica con la base de datos y así, comunica la aplicación web con la base de datos, gestionando las peticiones e inserciones de datos a la misma.

Así, separa la mínima funcionalidad principal de la funcionalidad extendida y las partes del cliente, implementando el propio microkernel los servicios principales y manejando la comunicación y los recursos.

### Tecnología utilizada

La herramienta principal de desarrollo es Django, un framework de código abierto, escrito en Python y que se apoya en el modelo de diseño MVC (Modelo-Vista-Controlador). Este modelo MVC define una forma de desarrollar software en la que el código para definir y acceder a los datos (el modelo) está separado del pedido lógico de asignación de ruta (el controlador), que a su vez está separado de la interfaz del usuario (la vista).

Para la persistencia de datos se ha decidido utilizar la base de datos NoSQL y de código abierto MongoDB, la cual se integra perfectamente en Django. Al no necesitar relaciones para la base de datos se utilizará MongoDB, y hará que el tamaño de la base de datos sea muy ligero.

### Provisionamiento

Se ha realizado provisionamiento con dos de las plataformas de software libre más utilizadas, en este caso Ansible y Chef.

En primer lugar, vamos a comentar como se ha realizado el provisionamiento para la máquina que va a ejecutar el proyecto con Ansible, el cuál está programado en Python y utiliza ficheros de tipo YAML.

En la siguiente imagen vemos el fichero de instalación de los paquetes necesarios para provisionar la máquina que va a ejecutar el proyecto. Por tanto, una vez ejecutado el fichero de Ansible dispondremos de todas las herramientas necesarias para dicha ejecución.

![alt tag](https://rawgit.com/mortega87/Images/master/ansible.png)
