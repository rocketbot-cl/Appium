# Instructivo de configuración previa para poder utilizar el módulo Appium

## Instalaciones previas
Para poder utilizar el módulo, es necesario tener instalado npm y nodejs. Para ello, se puede seguir el siguiente [link](https://nodejs.org/es/download/).
npm es el gestor de paquetes de nodejs, y es necesario para poder instalar Appium. Es recomendable instalar en la ubicación por defecto para evitar errores en la ejecución.

### Descarga de Android Debug Bridge (adb)
Descargar adb desde la página oficial de Android. Para ello, se puede seguir el siguiente [link](https://developer.android.com/studio/releases/platform-tools?hl=es-419).
Una vez descargado, debemos descomprimir la carpeta platform-tools en la ubicación deseada.

### Instalación y configuración de Appium y uiautomator2
Una vez instalado npm, se puede proceder a instalar Appium y el driver utilizado. Para realizar esto, se puede ejecutar el comando Configurar Appium del módulo. Sin embargo, si se desea realizar la instalación manualmente, se puede seguir el siguiente [link](http://appium.io/docs/en/2.1/quickstart/install/) para instalar Appium y el siguiente [link](http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) para instalar el driver.


### Agregar variables de entorno
Al ejecutar los comandos de conexión con el dispositivo, se requiere tener ciertas rutas agregadas al PATH del sistema para que todo funcione correctamente. Para ello, siga los siguientes pasos:
1. En la barra de búsqueda de Windows escriba Variables de Entorno y seleccione la opción Editar las variables de entorno del sistema.
2. En la ventana que se abre, seleccione Variables de entorno.
3. En la nueva ventana, debe crear una nueva variable del sistema. Como nombre, escriba ANDROID_HOME y como valor la ruta absoluta hacia la carpeta platform-tools que descomprimió anteriormente.
4. Luego, seleccione la variable Path y haga clic en Editar.
5. En la nueva ventana, haga clic en Nuevo y agregue la misma ruta utilizada en el paso anterior.
6. Por último, haga clic en Aceptar en todas las ventanas y reinicie la computadora.
7. Para verificar que todo se haya realizado correctamente, abra una consola de comandos y escriba adb. Si todo está bien, debería aparecer una lista de comandos disponibles.
8. Si todo está bien, puede proceder a ejecutar el comando Conectar dispositivo del módulo.






