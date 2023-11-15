# Pre-configuration instructions for using the Appium module


## Previous installations
To be able to use the module, it is necessary to install dependencies such as npm, nodejs, java and Android Studio, certain environment variables must also be configured in the system. To be able to configure everything correctly, you can run the Configure Appium command of the module to automatically detect what needs to be installed or configured. You can also follow the steps below.


### Manual installation of Appium and uiautomator2
To be able to install and configure Appium and uiautomator2, it is necessary to install npm and nodejs. To do this, you can follow the following [link](https://nodejs.org/en/download/). Once npm is installed, you can follow the following [link](http://appium.io/docs/en/2.1/quickstart/install/) to download and install Appium and the following [link](http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) to download and install the driver.

### Download and installation of Android Studio and SDK Tools
The module uses tools from the Android Studio Software kit (SDK Tools), so it is necessary to install it. To do this, you can download it from the following [link](https://developer.android.com/studio). Once downloaded, you must run the installer and follow the steps indicated. It is recommended to install in the default location to avoid errors in execution. To download the SDK Tools you must access Android Studio. In the top menu you must go to the Tools > SDK Manager option. In the window that opens, you must select the SDK Tools tab. In the list of tools, you must select `Android SDK Build-Tools`, `Android Emulator`, `Android SDK Platform-Tools` and click Apply. Once everything is downloaded, the paths to the folders used by the `emulator` and `platform-tools` tools must be added to the system path. An example of a path is `C:\Users\user\AppData\Local\Android\Sdk\emulator` (replace user with the computer username). Check the following section to see how to add environment variables.

### Download and installation of Java
To install Java you can follow the following [link](https://www.java.com/en/download/). Once downloaded, you must run the installer and follow the steps indicated. After installation, restart the machine. It is recommended to install in the default location to avoid errors in execution. To verify that everything has been done correctly, after restarting you can open a command prompt and type java -version. If everything is fine, the installed Java version should appear.


## Add environment variables
To run the module commands, you need to have certain paths added to the system PATH so that everything works correctly. To do this, follow these steps:
1. In the Windows search bar, type Environment Variables and select the Edit system environment variables option.
2. In the window that opens, select Environment variables.
3. In the new window, you must create a new system variable. As name, write ANDROID_HOME and as value the absolute path to the folder where the Android SDK Tools are installed. By default it is: `C:\Users\user\AppData\Local\Android\Sdk` (replace user with the computer username).
4. Then, in the Environment variables window select the Path user variable and click Edit.
5. In the new window, click New and add the same path used in the previous step adding the `platform-tools` folder at the end. For example, `C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (replace user with the computer username). You must also do the same but with the `emulator` folder. For example `C:\Users\user\AppData\Local\Android\Sdk\emulator` (replace user with the computer username).
6. Finally, click OK in all windows and restart the computer.
7. To verify that everything has been done correctly, open a command prompt and type adb. If everything is fine, a list of available commands should appear.
8. After completing these steps, you can proceed to run the module commands. As a recommendation, you can run the Configure Appium command to check that nothing is left pending.


## Android device configuration
### These steps are only necessary if you want to connect with a physical Android device. If you want to connect with an emulated device, you must follow the Create an emulated device section.
To connect the device correctly, it is necessary to configure the Android device to accept the connection, either by USB or by WiFi. To do this, follow these steps:
1. Activate developer options: On the device, go to Settings > About phone > Build number. Tap Build number 7 times. A message will appear saying that you are now a developer.
2. Activate USB debugging: On the device, go to Settings > System > Developer options and turn on USB debugging.
3. Activate wireless debugging: On the device, go to Settings > System > Developer options and turn on Wireless debugging.
4. If you want to use the wireless connection (WIFI) you must pair the device so that it can connect. To do this, you must use the Link device command once.
5. If you want to use the USB connection, you must connect the device to the computer using the USB cable. Then, you must run the Connect device command.
6. If everything was configured correctly, the Connect Android command should return True.


## Appium inspector
The Appium tool has an inspector to be able to visualize the elements of the device screen. To download it, you can follow the following [link](https://github.com/appium/appium-inspector/releases)


### Use Appium inspector
When unzipping the tool, you can run Appium Inspector.exe, which will open the tool window. To connect the Android device that was connected using the module in Rocketbot, you must go to the `Attach to Session ...` tab then in the reload button next to the input to enter the ID. If everything was configured correctly, a string should appear in the input where the ID of the connection, the device, its ip and port, and the uiautomator2 driver are indicated. Then, you must click on the Attach to Session button. This will open a new window of the inspector showing the device information.

### Create an emulated device
To be able to create an emulated device, you must open Android Studio and create a new project. In the window that opens, on the right side you will have the Device Manager (If it is not open, from the right side bar you can open it). You must click on Create Device. Then, you must select the device you want to emulate and click Next. In the next window, you must select the Android version you want to emulate and click Next. In the last window, you must verify the device configuration and click Finish. Once done, you must run the Connect emulated device command to be able to use it.

---

# Instructivo de configuración previa para poder utilizar el módulo Appium

## Instalaciones previas
Para poder utilizar el módulo, se requieren instalar dependencias como npm, nodejs, java y Android Studio, también se deben configurar ciertas variables de entorno en el sistema. Para poder configurar todo correctamente, se puede ejecutar el comando Configurar Appium del módulo para detectar automáticamente qué se debe instalar o configurar. Tambien se pueden seguir los pasos a continuación.

### Instalación manual de Appium y uiautomator2
Para poder instalar y configurar Appium y uiautomator2 se requiere instalar npm y nodejs. Para ello, se puede seguir el siguiente [link](https://nodejs.org/en/download/). Una vez instalado npm, se puede seguir el siguiente [link](http://appium.io/docs/en/2.1/quickstart/install/) para descargar e instalar Appium y el siguiente [link](http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) para descargar e instalar el driver.

### Descarga e instalación de Android Studio y SDK Tools
El módulo utiliza herramientas del kit de Software de Android Studio (SDK Tools), por lo que es necesario instalarlo. Para ello, se puede descargar desde el siguiente [link](https://developer.android.com/studio). Una vez descargado, se debe ejecutar el instalador y seguir los pasos que se indican. Es recomendable instalar en la ubicación por defecto para evitar errores en la ejecución. Para descargar las SDK Tools se debe acceder a Android Studio. En el menú superior se debe ir a la opción Tools > SDK Manager. En la ventana que se abre, se debe seleccionar la pestaña SDK Tools. En la lista de herramientas, se debe seleccionar `Android SDK Build-Tools`, `Android Emulator`, `Android SDK Platform-Tools` y hacer clic en Apply. Una vez todo descargado, se deben agregar al path del sistema las rutas hacia las carpetas usadas por las herramientas `emulator` y `platform-tools`. Un ejemplo de ruta es `C:\Users\user\AppData\Local\Android\Sdk\emulator` (reemplazar user por el nombre de usuario de la computadora). Verifique la sección correspondiente para ver cómo agregar variables de entorno.

### Descarga e instalación de Java
Para instalar Java se puede seguir el siguiente [link](https://www.java.com/es/download/). Una vez descargado, se debe ejecutar el instalador y seguir los pasos que se indican. Despues de la instalación reinicia la máquina. Es recomendable instalar en la ubicación por defecto para evitar errores en la ejecución. Para verificar que todo se haya realizado correctamente, luego de reiniciar se puede abrir una consola de comandos y escribir java -version. Si todo está bien, debería aparecer la versión de Java instalada.


## Agregar variables de entorno
Para ejecutar los comandos del módulo, se requiere tener ciertas rutas agregadas al PATH del sistema para que todo funcione correctamente. Para ello, siga los siguientes pasos:
1. En la barra de búsqueda de Windows escriba Variables de Entorno y seleccione la opción Editar las variables de entorno del sistema.
2. En la ventana que se abre, seleccione Variables de entorno.
3. En la nueva ventana, debe crear una nueva variable del sistema. Como nombre, escriba ANDROID_HOME y como valor la ruta absoluta hacia la carpeta donde se tengan instaladas las SDK Tools de Android. Por defecto es: `C:\Users\user\AppData\Local\Android\Sdk` (reemplazar user por el nombre de usuario de la computadora).
4. Luego, en la ventana de Variables de entorno seleccione la variable de usuario Path y haga clic en Editar.
5. En la nueva ventana, haga clic en Nuevo y agregue la misma ruta utilizada en el paso anterior agregando la carpeta `platform-tools` al final. Por ejemplo, `C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (reemplazar user por el nombre de usuario de la computadora). También deberá hacer lo mismo pero con la carpeta `emulator`. Por ejemplo `C:\Users\user\AppData\Local\Android\Sdk\emulator` (reemplazar user por el nombre de usuario de la computadora).
6. Por último, haga clic en Aceptar en todas las ventanas y reinicie la computadora.
7. Para verificar que todo se haya realizado correctamente, abra una consola de comandos y escriba adb. Si todo está bien, debería aparecer una lista de comandos disponibles.
8. Al finalizar estos pasos, se puede proceder a ejecutar los comandos del módulo. Como recomendación se puede ejecutar el comando Configurar Appium para revisar que no haya quedado nada pendiente.


## Configuración de dispositivo Android
### Estos pasos sólo son necesarios en caso de querer conectar con un dispositivo Android físico. En caso de querer conectar con un dispositivo emulado, se debe seguir el apartado Crear un dispositivo emulado.
Para conectar el dispositivo de forma correcta, se requiere configurar el dispositivo Android para que acepte la conexión, ya sea por USB o por WiFi. Para ello, siga los siguientes pasos:
1. Activar opciones de desarrollador: En el dispositivo, ve a Ajustes o Configuración > Información del teléfono > Número de compilación. Toca 7 veces Número de compilación. Aparecerá un mensaje que dice que ahora eres un desarrollador.
2. Activar depuración USB: En el dispositivo, ve a Ajustes o Configuración > Sistema > Opciones para desarrolladores y activa Depuración por USB.
3. Activar depuración inalámbrica: En el dispositivo, ve a Ajustes o Configuración > Sistema > Opciones para desarrolladores y activa Depuración inalámbrica.
4. Si se desea utilizar la conexión inalámbrica (WIFI) se debe emparejar el dispositivo para que se pueda conectar. Para esto se debe utilizar una única vez el comando Vincular dispositivo.
5. Si se desea utilizar la conexión por USB, se debe conectar el dispositivo a la computadora mediante el cable USB. Luego, se debe ejecutar el comando Conectar dispositivo.
6. Si todo fue configurado correctamente, el comando Conectar Android debería devolver True.


## Appium inspector
La herramienta Appium cuenta con un inspector para poder visualizar los elementos de la pantalla del dispositivo. Para descargarlo, se puede seguir el siguiente [link](https://github.com/appium/appium-inspector/releases)

### Utilizar Appium inspector
Al descomprimir la herramienta, se puede ejecutar Appium Inspector.exe, lo que levantará la ventana de la herramienta. Para conectar el dispositivo Android que fue conectado mediante el módulo en Rocketbot, debes ir a la pestaña `Attach to Session...` luego en el botón de recargar al lado del input para ingresar el ID. Si todo fue configurado correctamente, debería aparecer en el input un string donde se indica el ID de la conexión, el dispositivo, su ip y puerto, y el driver uiautomator2. Luego, se debe hacer clic en el botón Attach to Session. Esto abrirá una nueva ventana del inspector mostrando la información del dispositivo.

## Crear un dispositivo emulado
Para poder crear un dispositivo emulado, se debe abrir Android Studio y crear un nuevo proyecto. En la ventana que se abre, del lado derecho tendrán el Device Manager (Si no está abierto, desde la barra lateral derecha podrán abrirlo). Se debe hacer clic en Create Device. Luego, se debe seleccionar el dispositivo que se desea emular y hacer clic en Next. En la siguiente ventana, se debe seleccionar la versión de Android que se desea emular y hacer clic en Next. En la última ventana, se debe verificar la configuración del dispositivo y hacer clic en Finish. Una vez realizado, se debe ejecutar el comando Conectar dispositivo emulado para poder utilizarlo.

---

# Instruções de pré-configuração para usar o módulo Appium


## Instalações anteriores
Para poder usar o módulo, é necessário instalar dependências como npm, nodejs, java e Android Studio, também é necessário configurar certas variáveis ​​de ambiente no sistema. Para poder configurar tudo corretamente, você pode executar o comando Configure Appium do módulo para detectar automaticamente o que precisa ser instalado ou configurado. Você também pode seguir as etapas abaixo.


### Instalação manual do Appium e uiautomator2
Para poder instalar e configurar o Appium e o uiautomator2, é necessário instalar o npm e o nodejs. Para fazer isso, você pode seguir o seguinte [link](https://nodejs.org/en/download/). Depois de instalado o npm, você pode seguir o seguinte [link](http://appium.io/docs/en/2.1/quickstart/install/) para baixar e instalar o Appium e o seguinte [link](http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) para baixar e instalar o driver.


### Download e instalação do Android Studio e SDK Tools
O módulo usa ferramentas do kit de software do Android Studio (SDK Tools), portanto, é necessário instalá-lo. Para fazer isso, você pode baixá-lo no seguinte [link](https://developer.android.com/studio). Depois de baixado, você deve executar o instalador e seguir as etapas indicadas. É recomendável instalar no local padrão para evitar erros na execução. Para baixar as SDK Tools, você deve acessar o Android Studio. No menu superior, você deve ir para a opção Tools > SDK Manager. Na janela que se abre, você deve selecionar a guia SDK Tools. Na lista de ferramentas, você deve selecionar `Android SDK Build-Tools`, `Android Emulator`, `Android SDK Platform-Tools` e clicar em Apply. Depois de tudo baixado, você deve adicionar ao path do sistema os caminhos para as pastas usadas pelas ferramentas `emulator` e `platform-tools`. Um exemplo de caminho é `C:\Users\user\AppData\Local\Android\Sdk\emulator` (substitua o usuário pelo nome de usuário do computador). Verifique a seção correspondente para ver como adicionar variáveis ​​de ambiente.


### Download e instalação do Java
Para instalar o Java, você pode seguir o seguinte [link](https://www.java.com/en/download/). Depois de baixado, você deve executar o instalador e seguir as etapas indicadas. Após a instalação, reinicie a máquina. É recomendável instalar no local padrão para evitar erros na execução. Para verificar se tudo foi feito corretamente, após a reinicialização, você pode abrir um prompt de comando e digitar java -version. Se tudo estiver bem, a versão do Java instalada deve aparecer.


## Adicionar variáveis ​​de ambiente
Para executar os comandos do módulo, você precisa ter certos caminhos adicionados ao PATH do sistema para que tudo funcione corretamente. Para fazer isso, siga estas etapas:
1. Na barra de pesquisa do Windows, digite Variáveis ​​de ambiente e selecione a opção Editar variáveis ​​de ambiente do sistema.
2. Na janela que se abre, selecione Variáveis ​​de ambiente.
3. Na nova janela, você deve criar uma nova variável do sistema. Como nome, escreva ANDROID_HOME e como valor o caminho absoluto para a pasta onde as Android SDK Tools estão instaladas. Por padrão, é: `C:\Users\user\AppData\Local\Android\Sdk` (substitua o usuário pelo nome de usuário do computador).
4. Em seguida, na janela Variáveis ​​de ambiente, selecione a variável do usuário Path e clique em Editar.
5. Na nova janela, clique em Novo e adicione o mesmo caminho usado na etapa anterior adicionando a pasta `platform-tools` no final. Por exemplo, `C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (substitua o usuário pelo nome de usuário do computador). Você também deve fazer o mesmo, mas com a pasta `emulator`. Por exemplo `C:\Users\user\AppData\Local\Android\Sdk\emulator` (substitua o usuário pelo nome de usuário do computador).
6. Por fim, clique em OK em todas as janelas e reinicie o computador.
7. Para verificar se tudo foi feito corretamente, abra um prompt de comando e digite adb. Se tudo estiver bem, uma lista de comandos disponíveis deve aparecer.
8. Após concluir estas etapas, você pode prosseguir para executar os comandos do módulo. Como recomendação, você pode executar o comando Configure Appium para verificar se nada ficou pendente.


## Configuração do dispositivo Android
### Essas etapas são necessárias apenas se você quiser se conectar a um dispositivo Android físico. Se você quiser se conectar a um dispositivo emulado, deverá seguir a seção Criar um dispositivo emulado.
Para conectar o dispositivo corretamente, é necessário configurar o dispositivo Android para aceitar a conexão, seja por USB ou por WiFi. Para fazer isso, siga estas etapas:
1. Ative as opções do desenvolvedor: No dispositivo, vá para Configurações > Sobre o telefone > Número da compilação. Toque no número da compilação 7 vezes. Uma mensagem aparecerá dizendo que você agora é um desenvolvedor.
2. Ative a depuração USB: No dispositivo, vá para Configurações > Sistema > Opções do desenvolvedor e ative a depuração USB.
3. Ative a depuração sem fio: No dispositivo, vá para Configurações > Sistema > Opções do desenvolvedor e ative a depuração sem fio.
4. Se você deseja usar a conexão sem fio (WIFI), deve parear o dispositivo para que ele possa se conectar. Para fazer isso, você deve usar o comando Link device uma vez.
5. Se você deseja usar a conexão USB, deve conectar o dispositivo ao computador usando o cabo USB. Em seguida, você deve executar o comando Connect device.
6. Se tudo foi configurado corretamente, o comando Connect Android deve retornar True.


## Inspetor Appium
A ferramenta Appium possui um inspetor para poder visualizar os elementos da tela do dispositivo. Para baixá-lo, você pode seguir o seguinte [link](https://github.com/appium/appium-inspector/releases)


### Use o inspetor Appium
Ao descompactar a ferramenta, você pode executar o Appium Inspector.exe, que abrirá a janela da ferramenta. Para conectar o dispositivo Android que foi conectado usando o módulo no Rocketbot, você deve ir para a guia `Attach to Session ...` e depois no botão de recarregar ao lado da entrada para inserir o ID. Se tudo foi configurado corretamente, uma string deve aparecer na entrada onde o ID da conexão, o dispositivo, seu ip e porta e o driver uiautomator2 são indicados. Em seguida, você deve clicar no botão Attach to Session. Isso abrirá uma nova janela do inspetor mostrando as informações do dispositivo.

### Criar um dispositivo emulado
Para poder criar um dispositivo emulado, você deve abrir o Android Studio e criar um novo projeto. Na janela que se abre, do lado direito você terá o Device Manager (Se não estiver aberto, na barra lateral direita você pode abri-lo). Você deve clicar em Create Device. Em seguida, você deve selecionar o dispositivo que deseja emular e clicar em Avançar. Na próxima janela, você deve selecionar a versão do Android que deseja emular e clicar em Avançar. Na última janela, você deve verificar a configuração do dispositivo e clicar em Concluir. Feito isso, você deve executar o comando Connect emulated device para poder usá-lo.


---