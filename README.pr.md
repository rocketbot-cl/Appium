# Appium
  
Módulo para automatizar dispositivos móveis  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Configurar Appium  
Este comando verifica se o Appium e o driver uiautomator2 estão instalados. Se alguma das dependências não estiver instalada, ela será instalada automaticamente.

2. Emparelhar dispositivo  
Este comando permite emparelhar um dispositivo Android com a máquina que você deseja conectar. Esta etapa é necessária para realizar apenas uma vez por dispositivo se você deseja se conectar via WIFI.

3. Conectar Android  
Este comando permite conectar um dispositivo Android e configurar o servidor utilizando Android Debug Bridge (ADB). As opções do desenvolvedor devem estar ativadas no dispositivo e a depuração sem fio ou USB conforme apropriado.

4. Swipe simples  
Esse comando permite que você faça um simples swipe na tela do dispositivo Android.

5. Toque nas coordenadas  
Este comando permite tocar em uma coordenada específica na tela.

6. Enviar teclas  
Esse comando permite enviar teclas para um seletor específico no dispositivo Android.

7. Obter texto  
Este comando permite obter o texto de um seletor específico do dispositivo Android.

8. Desconectar Android  
Este comando permite desconectar o dispositivo Android que está sendo automatizado.  




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