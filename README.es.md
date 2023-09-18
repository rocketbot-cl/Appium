# Appium
  
Módulo para automatizar dispositivos móviles  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Configurar Appium  
Este comando comprueba si se tiene instalado Appium, el driver uiautomator2. Si alguna de las dependencias no está instalada, se instalará automáticamente.

2. Vincular dispositivo  
Este comando permite vincular un dispositivo Android con la máquina donde se desea conectar. Este paso es necesario realizarlo una única vez por dispositivo si se desea conectar mediante WIFI.

3. Conectar Android  
Este comando permite conectar un dispositivo Android y configurar el servidor utilizando Android Debug Bridge (ADB). Se deben tener activadas las opciones de desarrollador en el dispositivo, y la depuración inalámbrica o USB según corresponda.

4. Swipe simple  
Este comando permite realizar un swipe simple en la pantalla del dispositivo Android.

5. Tap en coordenadas  
Este comando permite realizar un tap en una coordenada específica de la pantalla.

6. Enviar teclas  
Este comando permite enviar teclas a un selector específico del dispositivo Android.

7. Obtener texto  
Este comando permite obtener el texto de un selector específico del dispositivo Android.

8. Desconectar Android  
Este comando permite desconectar el dispositivo Android que está siendo automatizado.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**Appium-Python-Client**](https://pypi.org/project/Appium-Python-Client/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)