# Appium
  
Módulo para automatizar dispositivos móviles  

*Read this in other languages: [English](Manual_Appium.md), [Português](Manual_Appium.pr.md), [Español](Manual_Appium.es.md)*

![banner](imgs/Banner_Appium.png o jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

# Instructivo de configuración previa para poder utilizar el módulo Appium

## Instalaciones previas
Para poder utilizar el módulo, es necesario tener instalado npm y nodejs. Para ello, se puede seguir el siguiente [link](https://nodejs.org/es/download/).
npm es el gestor de paquetes de nodejs, y es necesario para poder instalar Appium. Es recomendable instalar en la ubicación por defecto para evitar errores en la ejecución.

### Instalación y configuración de Appium y uiautomator2
Una vez instalado npm, se puede proceder a instalar Appium y el driver utilizado. Para realizar esto, se puede ejecutar el comando Configurar Appium del módulo. Sin embargo, si se desea realizar la instalación manualmente, se puede seguir el siguiente [link](http://appium.io/docs/en/2.1/quickstart/install/) para instalar Appium y el siguiente [link](http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) para instalar el driver.

### Descarga e instalación de Android Studio
El módulo utiliza herramientas 
del kit de Software de Android Studio, por lo que es necesario instalarlo. Para ello, se puede descargar desde el siguiente [link](https://developer.android.com/studio). Una vez descargado, se debe ejecutar el instalador y seguir los pasos que se indican. Es recomendable instalar en la ubicación por defecto para evitar errores en la ejecución.


## Agregar variables de entorno
Para ejecutar los comandos del módulo, se requiere tener ciertas rutas agregadas al PATH del sistema para que todo funcione correctamente. Para ello, siga los siguientes pasos:
1. En la barra de búsqueda de Windows escriba Variables de Entorno y seleccione la opción Editar las variables de entorno del sistema.
2. En la ventana que se abre, seleccione Variables de entorno.
3. En la nueva ventana, debe crear una nueva variable del sistema. Como nombre, escriba ANDROID_HOME y como valor la ruta absoluta hacia la carpeta `C:\Users\user\AppData\Local\Android\Sdk` (reemplazar user por el nombre de usuario de la 
computadora).
4. Luego, seleccione la variable Path y haga clic en Editar.
5. En la nueva ventana, haga clic en Nuevo y agregue la misma ruta utilizada en el paso anterior agregando la carpeta `platform-tools` al final. Por ejemplo, `C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (reemplazar user por el nombre de usuario de la computadora).
6. Por último, haga clic en Aceptar en todas las ventanas y reinicie la computadora.
7. Para verificar que todo se haya realizado correctamente, abra una consola de comandos y escriba adb. Si todo está bien, debería aparecer una lista de comandos disponibles.
8. Al finalizar estos pasos, se puede proceder a ejecutar los comandos del módulo.


## Configuración de dispositivo Android
Para conectar el dispositivo de forma correcta, se requiere configurar el dispositivo Android para que acepte la conexión, ya sea por USB o por WiFi. Para ello, siga los siguientes pasos:
1. Activar opciones de desarrollador: En el dispositivo, ve a Ajustes o 
Configuración > Información del teléfono > Número de compilación. Toca 7 veces Número de compilación. Aparecerá un mensaje que dice que ahora eres un desarrollador.
2. Activar depuración USB: En el dispositivo, ve a Ajustes o Configuración > Sistema > Opciones para desarrolladores y activa Depuración por USB.
3. Activar depuración inalámbrica: En el dispositivo, ve a Ajustes o Configuración > Sistema > Opciones para desarrolladores y activa Depuración inalámbrica.
4. Si se desea utilizar la conexión inalámbrica (WIFI) se debe emparejar el dispositivo para que se pueda conectar. Para esto se debe utilizar una única vez el comando Vincular dispositivo.
5. Si se desea utilizar la conexión por USB, se debe conectar el dispositivo a la computadora mediante el cable USB. Luego, se debe ejecutar el comando Conectar dispositivo.
6. Si todo fue configurado correctamente, el comando Conectar Android debería devolver True.


## Appium inspector
La herramienta Appium cuenta con un inspector para 
poder visualizar los elementos de la pantalla del dispositivo. Para descargarlo, se puede seguir el siguiente [link](https://github.com/appium/appium-inspector/releases)

### Utilizar Appium inspector
Al descomprimir la herramienta, se puede ejecutar Appium Inspector.exe, lo que levantará la ventana de la herramienta. Para conectar el dispositivo Android que fue conectado mediante el módulo en Rocketbot, debes ir a la pestaña `Attach to Session...` luego en el botón de recargar al lado del input para ingresar el ID. Si todo fue configurado correctamente, debería aparecer en el input un string donde se indica el ID de la conexión, el dispositivo, su ip y puerto, y el driver uiautomator2. Luego, se debe hacer clic en el botón Attach to Session. Esto abrirá una nueva ventana del inspector mostrando la información del dispositivo.

## Descripción de los comandos

### Configurar Appium
  
Este comando comprueba si se tiene instalado Appium, el driver uiautomator2. Si alguna de las dependencias no está instalada, se instalará automáticamente.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Asignar resultado de la configuración a una variable|result|

### Vincular dispositivo
  
Este comando permite vincular un dispositivo Android con la máquina donde se desea conectar. Este paso es necesario realizarlo una única vez por dispositivo si se desea conectar mediante WIFI.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dirección ip y puerto del dispositivo|Dirección IP y puerto del dispositivo Android que se desea conectar|ip:port|
|Código de vinculación WIFI|Código de vinculación WIFI del dispositivo Android que se desea vincular|876543|
|Asignar resultado a variable|Asignar resultado de la conexión a una variable|result|

### Conectar Android
  
Este comando permite conectar un dispositivo Android y configurar el servidor utilizando Android Debug Bridge (ADB). Se deben tener activadas las opciones de desarrollador en el dispositivo, y la depuración inalámbrica o USB según corresponda.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dirección ip y puerto del dispositivo|Dirección IP y puerto del dispositivo Android que se desea conectar|ip:port|
|Tipo de conexión|Tipo de conexión a utilizar|USB|
|Asignar resultado a variable|Asignar resultado de la conexión a una variable|result|

### Swipe simple
  
Este comando permite realizar un swipe simple en la pantalla del dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dirección del swipe|Dirección que tendrá el swipe en la pantalla del dispositivo.|Right|

### Tap en coordenadas
  
Este comando permite realizar un tap en una coordenada específica de la pantalla.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Coordenada X|Coordenada X donde se realizará el tap|100|
|Coordenada Y|Coordenada Y donde se realizará el tap|100|

### Enviar teclas
  
Este comando permite enviar teclas a un selector específico del dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de dato|Tipo de dato del selector en el cual se enviarán las teclas.|id|
|Selector|Selector en el cual se enviarán las teclas.|com.whatsapp:id/entry|
|Teclas|Teclas que se enviarán al selector.|Hola mundo!|

### Obtener texto
  
Este comando permite obtener el texto de un selector específico del dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de dato|Tipo de dato del selector en el cual se enviarán las teclas.|id|
|Selector|Selector en el cual se enviarán las teclas.|com.whatsapp:id/entry|
|Asignar resultado a variable|Nombre de la variable en la cual se asignará el resultado.|variable|

### Desconectar Android
  
Este comando permite desconectar el dispositivo Android que está siendo automatizado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |