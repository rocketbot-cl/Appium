



# Appium
  
Módulo para automatizar dispositivos móviles  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Configurar Appium  
Este comando comprueba si se tienen instaladas las dependencias necesarias para correr Appium. Intentará instalar algunas, pero no todas. Para aquellas en las que Rocketbot no pueda, generará un error indicando los pasos a seguir para instalarlas manualmente. Se recomienda ejecutar este comando solamente para validar que se tienen las dependencias necesarias, y no incluirlo en la versión del bot que se despliegue en producción.

2. Vincular dispositivo  
Este comando permite vincular un dispositivo Android con la máquina donde se desea conectar. Este paso es necesario realizarlo una única vez por dispositivo si se desea conectar mediante WIFI.

3. Conectar Android  
Este comando permite conectar un dispositivo Android y configurar el servidor utilizando Android Debug Bridge (ADB). Se deben tener activadas las opciones de desarrollador en el dispositivo, y la depuración inalámbrica o USB según corresponda.

4. Listar Dispositivos Emulados  
Este comando permite listar los dispositivos emulados disponibles.

5. Conectar Dispositivo Emulado  
Este comando permite conectar un dispositivo emulado y configurar el servidor. Si es la primera vez que se ejecuta el emulador, es posible que se demore unos minutos en iniciar.

6. Bloquear dispositivo  
Este comando permite bloquear un dispositivo Android.

7. Desbloquear Dispositivo  
Este comando permite desbloquear un dispositivo Android. Sólo disponible si se ha establecido el tipo y código de desbloqueo en el comando de conexión.

8. Obtener información de aplicación actual  
Este comando permite obtener el nombre del paquete y el nombre de la actividad de la aplicación que se está ejecutando actualmente en el dispositivo Android.

9. Iniciar aplicación  
Este comando permite iniciar una aplicación en el dispositivo Android. Para obtener el nombre del paquete y el nombre de la actividad, puede utilizar el comando Obtener información de aplicación actual

10. Swipe simple  
Este comando permite realizar un swipe simple en la pantalla del dispositivo Android.

11. Tap en coordenadas  
Este comando permite realizar un tap en una coordenada específica de la pantalla.

12. Tap en elemento  
Este comando permite realizar un tap en un elemento específico de la pantalla.

13. Enviar teclas  
Este comando permite enviar teclas a un selector específico del dispositivo Android.

14. Extraer texto  
Este comando permite obtener el texto de un selector específico del dispositivo Android.

15. Extraer texto por coordenadas  
Este comando permite obtener el texto de un elemento ubicado en una posición específica del dispositivo Android.

16. Zoom en coordenadas  
Este comando permite realizar un zoom in o zoom out sobre las coordenadas especificadas en el dispositivo Android.

17. Zoom en objeto  
Este comando permite realizar un zoom in o zoom out sobre un objeto en el dispositivo Android.

18. Captura de pantalla  
Este comando permite capturar la pantalla del dispositivo Android y almacenar la imagen en la ruta especificada.

19. Ejecutar comando en dispositivo  
Este comando permite ejecutar un comando en el terminal del dispositivo Android. Para ejecutar este comando correctamente debe estar marcado el checkbox de Permitir shell en el comando de conexión.

20. Esperar por objeto  
Este comando permite esperar por un objeto en el dispositivo Android. El comando se ejecutará hasta que el objeto sea encontrado o hasta que se cumpla el tiempo máximo de espera.

21. Desconectar dispositivo  
Este comando permite desconectar el dispositivo Android o emulado que está siendo automatizado.  




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