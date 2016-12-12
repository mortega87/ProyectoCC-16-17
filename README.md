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

Se ha realizado provisionamiento con dos de las plataformas de software libre más utilizadas, en este caso **Ansible y Chef**.

En primer lugar, vamos a comentar como se ha realizado el provisionamiento para la máquina que va a ejecutar el proyecto con **Ansible**, el cuál está programado en Python y utiliza ficheros de tipo YAML.

En la siguiente imagen vemos el fichero de instalación de los paquetes necesarios para provisionar la máquina que va a ejecutar el proyecto. Por tanto, una vez ejecutado el fichero de Ansible, llamado playbook, dispondremos de todas las herramientas necesarias para dicha ejecución.

![alt tag](https://rawgit.com/mortega87/Images/master/ansible.png)

Para la ejecución del playbook usamos el siguiente comando:

<pre>ansible-playbook /etc/ansible/playbooks/playbook.yml</pre>


Para realizar el provisionamiento con una herramienta distinta he decidido utilizar **Chef**. Está escrita en Ruby y es otra de las más utilizadas para provisionamiento y sencillo de usar. En este caso, he utilizado chef-solo, por tanto, es necesario tener instalado dicho paquete en le cliente y así poder ejecutar el fichero.

Necesitamos varios ficheros para provisionar una máquina.

En primer lugar el fichero default.rb, donde hacemos la descripción de los paquetes o receta que vamos a necesitar en el provisionamiento.

![alt tag](https://rawgit.com/mortega87/Images/master/chef_default.png)

El siguiente fichero es node.json, donde tenemos que indicar el nombre del recipiente que vamos a utilizar.

![alt tag](https://rawgit.com/mortega87/Images/master/chef_node.png)

Por último tenemos el fichero solo.rb en el cual vamos a indicar los directorios que componen el provisionamiento. Podemos indicarlo de la siguiente forma.

![alt tag](https://rawgit.com/mortega87/Images/master/chef_solo.png)

Una vez con estos ficheros completados, ejecutamos en la máquina que vamos a provisionar:

<pre>sudo chef-solo -c chef/solo.rb</pre>

Tener en cuenta que la máquina debe de contar con el paquete chef-solo instalado.

### Orquestación.

Para la orquestación de máquinas virtuales se ha utilizado la herramienta de software libre Vagrant. Está desarrollada en Ruby y se complementa perfectamente con sofware de virtualización como VirtualBox y con software de aprovisionamiento como Ansible.

En primer lugar, instalamos VirtualBox y Vagrant:

<pre>sudo apt-get install virtualbox dkms</pre>

<pre>sudo apt-get -y install vagrant</pre>

Iniciamos el servicio Vagrant.

<pre>vagrant init</pre>

Esto nos creará en nuestro directorio y el fichero Vagrantfile, asi que, a continuación, vamos a comentar el contenido del fichero para nuestra orquestación.

<pre>
  #Fichero Vagrant para crear y provisionar tres máquinas virtuales Ubuntu 14.04.

  Vagrant.configure(2) do |config|

    #Definimos la configuración de las tres máquinas virtuales.

    config.vm.define "vm1" do |vm1|
      vm1.vm.box = "ubuntu/trusty64"
    end

    config.vm.define "vm2" do |vm2|
      vm2.vm.box = "ubuntu/trusty64"
    end

    config.vm.define "vm3" do |vm3|
      vm3.vm.box = "ubuntu/trusty64"
    end

    #Especificamos cual será el fichero de ansible que va a provisionar las tres máquinas virtuales.

    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
    end

  end
</pre>

Creamos tres máquinas virtuales Ubuntu 14.04 y el aprovisionamiento se realizará con playbook.yml, utilizado anteroirmente y situado en el mismo directorio del Vagrantfile.

Ejecutamos el comando siguiente para levantar, crear y aprovisionar las máquinas virtuales.

<pre>vagrant up</pre>


Vemos que se crean y aprovisionan correctamente:

![alt tag](https://rawgit.com/mortega87/Images/master/vagrant1.png)

![alt tag](https://rawgit.com/mortega87/Images/master/vagrant3.png)

Para conectar con ellas ejecutamos:

<pre>vagrant ssh vm1</pre>

Donde vm1 es el nombre que hemos especificado de la máquina en Vagrantfile, pudiendo ser sustituido por cualquiera de las demás.


Más información en la web del proyecto.
