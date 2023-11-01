# Appium
  
Módulo para automatizar dispositivos móviles  

*Read this in other languages: [English](Manual_Appium.md), [Português](Manual_Appium.pr.md), [Español](Manual_Appium.es.md)*
  
![banner](imgs/Banner_Appium.jpg)
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

### Descargar herramientas de línea de comandos de Android Studio
En caso de querer conectarse con un dispositivo emulado, es necesario hacerlo con las herramientas de línea de comandos. Se pueden descargar accediendo a Android Studio. En el menú superior se debe ir a la opción Tools > SDK Manager. En la ventana que se abre, se debe seleccionar la pestaña SDK Tools. En la lista de herramientas, se debe seleccionar Android SDK Command-line Tools y hacer clic en Apply. Luego hacer clic en OK. Una vez descargadas, se debe agregar a las variables de entorno la ruta hacia la carpeta que utiliza la herramienta `emulator`. Revise el siguiente apartado 
para ver cómo agregar variables de entorno, en el punto 8 se especifica la ruta a agregar.


## Agregar variables de entorno
Para ejecutar los comandos del módulo, se requiere tener ciertas rutas agregadas al PATH del sistema para que todo funcione correctamente. Para ello, siga los siguientes pasos:
1. En la barra de búsqueda de Windows escriba Variables de Entorno y seleccione la opción Editar las variables de entorno del sistema.
2. En la ventana que se abre, seleccione Variables de entorno.
3. En la nueva ventana, debe crear una nueva variable del sistema. Como nombre, escriba ANDROID_HOME y como valor la ruta absoluta hacia la carpeta `C:\Users\user\AppData\Local\Android\Sdk` (reemplazar user por el nombre de usuario de la computadora).
4. Luego, seleccione la variable Path y haga clic en Editar.
5. En la nueva ventana, haga clic en Nuevo y agregue la misma ruta utilizada en el paso anterior agregando la carpeta `platform-tools` al final. Por ejemplo, 
`C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (reemplazar user por el nombre de usuario de la computadora).
6. Por último, haga clic en Aceptar en todas las ventanas y reinicie la computadora.
7. Para verificar que todo se haya realizado correctamente, abra una consola de comandos y escriba adb. Si todo está bien, debería aparecer una lista de comandos disponibles.
8. En caso de instalar las herramientas de línea de comandos, se debe agregar al path la ruta hacia la carpeta `C:\Users\user\AppData\Local\Android\Sdk\emulator` (reemplazar user por el nombre de usuario de la computadora).
9. Al finalizar estos pasos, se puede proceder a ejecutar los comandos del módulo.


## Configuración de dispositivo Android
### Estos pasos sólo son necesarios en caso de querer conectar con un dispositivo Android físico. En caso de querer conectar con un dispositivo emulado, se debe seguir el apartado Crear un dispositivo emulado.
Para conectar el dispositivo de forma correcta, se requiere 
configurar el dispositivo Android para que acepte la conexión, ya sea por USB o por WiFi. Para ello, siga los siguientes pasos:
1. Activar opciones de desarrollador: En el dispositivo, ve a Ajustes o Configuración > Información del teléfono > Número de compilación. Toca 7 veces Número de compilación. Aparecerá un mensaje que dice que ahora eres un desarrollador.
2. Activar depuración USB: En el dispositivo, ve a Ajustes o Configuración > Sistema > Opciones para desarrolladores y activa Depuración por USB.
3. Activar depuración inalámbrica: En el dispositivo, ve a Ajustes o Configuración > Sistema > Opciones para desarrolladores y activa Depuración inalámbrica.
4. Si se desea utilizar la conexión inalámbrica (WIFI) se debe emparejar el dispositivo para que se pueda conectar. Para esto se debe utilizar una única vez el comando Vincular dispositivo.
5. Si se desea utilizar la conexión por USB, se debe conectar el dispositivo a la computadora mediante el cable USB. Luego, se debe ejecutar 
el comando Conectar dispositivo.
6. Si todo fue configurado correctamente, el comando Conectar Android debería devolver True.


## Appium inspector
La herramienta Appium cuenta con un inspector para poder visualizar los elementos de la pantalla del dispositivo. Para descargarlo, se puede seguir el siguiente [link](https://github.com/appium/appium-inspector/releases)

### Utilizar Appium inspector
Al descomprimir la herramienta, se puede ejecutar Appium Inspector.exe, lo que levantará la ventana de la herramienta. Para conectar el dispositivo Android que fue conectado mediante el módulo en Rocketbot, debes ir a la pestaña `Attach to Session...` luego en el botón de recargar al lado del input para ingresar el ID. Si todo fue configurado correctamente, debería aparecer en el input un string donde se indica el ID de la conexión, el dispositivo, su ip y puerto, y el driver uiautomator2. Luego, se debe hacer clic en el botón Attach to Session. Esto abrirá una nueva ventana del inspector 
mostrando la información del dispositivo.

## Crear un dispositivo emulado
Para poder crear un dispositivo emulado, se debe abrir Android Studio y crear un nuevo proyecto. En la ventana que se abre, del lado derecho tendrán el Device Manager (Si no está abierto, desde la barra lateral derecha podrán abrirlo). Se debe hacer clic en Create Device. Luego, se debe seleccionar el dispositivo que se desea emular y hacer clic en Next. En la siguiente ventana, se debe seleccionar la versión de Android que se desea emular y hacer clic en Next. En la última ventana, se debe verificar la configuración del dispositivo y hacer clic en Finish. Una vez realizado, se debe ejecutar el comando Conectar dispositivo emulado para poder utilizarlo.


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
|Tipo de desbloqueo|Tipo de desbloqueo a utilizar|PIN|
|Código de desbloqueo|Código de desbloqueo del dispositivo Android que se desea conectar|1234|
|Permitir shell|Permite ejecutar comandos utilizando la terminal en el dispositivo Android. Es una característica insegura. Para más información, consulte https//appium.io/docs/en/2.0/guides/security/|True|
|Asignar resultado a variable|Asignar resultado de la conexión a una variable|result|

### Listar Dispositivos Emulados
  
Este comando permite listar los dispositivos emulados disponibles.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Asignar resultado de la operación a una variable|result|

### Conectar Dispositivo Emulado
  
Este comando permite conectar un dispositivo emulado y configurar el servidor.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del emulador|Nombre del emulador que se desea conectar|Pixel_7_Pro_API_34|
|Permitir shell|Permite ejecutar comandos utilizando la terminal en el dispositivo Android. Es una característica insegura. Para más información, consulte https//appium.io/docs/en/2.0/guides/security/|True|
|Tipo de desbloqueo|Tipo de desbloqueo a utilizar|PIN|
|Código de desbloqueo|Código de desbloqueo del dispositivo Android que se desea conectar|1234|
|Asignar resultado a variable|Asignar resultado de la conexión a una variable|result|

### Bloquear dispositivo
  
Este comando permite bloquear un dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Desbloquear Dispositivo
  
Este comando permite desbloquear un dispositivo Android. Sólo disponible si se ha establecido el tipo y código de desbloqueo en el comando de conexión.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Obtener información de aplicación actual
  
Este comando permite obtener el nombre del paquete y el nombre de la actividad de la aplicación que se está ejecutando actualmente en el dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Asignar resultado a variable|Nombre de la variable en la cual se asignará el resultado.|variable|

### Iniciar aplicación
  
Este comando permite iniciar una aplicación en el dispositivo Android. Para obtener el nombre del paquete y el nombre de la actividad, puede utilizar el comando Obtener información de aplicación actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del paquete|Nombre del paquete de la aplicación que se desea iniciar.|com.android.Settings|
|Nombre de la actividad|Nombre de la actividad de la aplicación que se desea iniciar.|.Settings|
|Asignar resultado a variable|Nombre de la variable en la cual se asignará el resultado.|variable|

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

### Tap en elemento
  
Este comando permite realizar un tap en un elemento específico de la pantalla.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de dato|Tipo de dato del selector en el cual se realizará el tap.|id|
|Selector|Selector en el cual realizará el tap.|com.whatsapp:id/entry|
|Asignar resultado a variable|Nombre de la variable en la cual se asignará el resultado.|variable|

### Enviar teclas
  
Este comando permite enviar teclas a un selector específico del dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de dato|Tipo de dato del selector en el cual se enviarán las teclas.|id|
|Selector|Selector en el cual se enviarán las teclas.|com.whatsapp:id/entry|
|Teclas|Teclas que se enviarán al selector.|Hola mundo!|

### Extraer texto
  
Este comando permite obtener el texto de un selector específico del dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de dato|Tipo de dato del selector en el cual se enviarán las teclas.|id|
|Selector|Selector en el cual se enviarán las teclas.|com.whatsapp:id/entry|
|Asignar resultado a variable|Nombre de la variable en la cual se asignará el resultado.|variable|

### Extraer texto por coordenadas
  
Este comando permite obtener el texto de un elemento ubicado en una posición específica del dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Coordenadas x,y|Coordenadas x,y del elemento a obtener el texto.|450,2000|
|Asignar resultado a variable|Nombre de la variable en la cual se asignará el resultado.|variable|

### Zoom en coordenadas
  
Este comando permite realizar un zoom in o zoom out sobre las coordenadas especificadas en el dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de zoom|Tipo de zoom a realizar.|Zoom in|
|Coordenadas x,y|Coordenadas x,y donde se realizará el zoom.|450,2000|
|Píxeles a desplazar|Píxeles a desplazar en el zoom.|500|
|Velocidad de zoom|Velocidad de zoom a realizar.|Normal|

### Zoom en objeto
  
Este comando permite realizar un zoom in o zoom out sobre un objeto en el dispositivo Android.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de zoom|Tipo de zoom a realizar.|Zoom in|
|Tipo de dato|Tipo de dato del selector en el cual se realizará el zoom.|id|
|Selector|Selector en el cual realizará el zoom|com.whatsapp:id/entry|
|Píxeles a desplazar|Píxeles a desplazar en el zoom.|500|
|Velocidad de zoom|Velocidad de zoom a realizar.|Normal|

### Captura de pantalla
  
Este comando permite capturar la pantalla del dispositivo Android y almacenar la imagen en la ruta especificada.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la imagen|Ruta en la cual se almacenará la imagen.|C:/Users/User/Desktop/imagen.png|

### Ejecutar comando en dispositivo
  
Este comando permite ejecutar un comando en el terminal del dispositivo Android. Para ejecutar este comando correctamente debe estar marcado el checkbox de Permitir shell en el comando de conexión.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Comando|Comando que se ejecutará en el terminal del dispositivo.|pm list packages|
|Asignar resultado a variable|Nombre de la variable en la cual se asignará el resultado.|variable|

### Desconectar dispositivo
  
Este comando permite desconectar el dispositivo Android o emulado que está siendo automatizado.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
