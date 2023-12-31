



# Appium
  
Módulo para automatizar dispositivos móveis  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Configurar Appium  
Este comando verifica se você instalou as dependências necessárias para executar o Appium. Ele tentará instalar alguns, mas não todos. Para aqueles em que o Rocketbot não puder, ele gerará um erro indicando as etapas a seguir para instalá-los manualmente. É recomendável executar este comando apenas para validar se você possui as dependências necessárias e não incluí-lo na versão do bot que é implantada em produção.

2. Emparelhar dispositivo  
Este comando permite emparelhar um dispositivo Android com a máquina que você deseja conectar. Esta etapa é necessária para realizar apenas uma vez por dispositivo se você deseja se conectar via WIFI.

3. Conectar Android  
Este comando permite conectar um dispositivo Android e configurar o servidor utilizando Android Debug Bridge (ADB). As opções do desenvolvedor devem estar ativadas no dispositivo e a depuração sem fio ou USB conforme apropriado.

4. Listar dispositivos emulados  
Este comando permite listar os dispositivos emulados disponíveis.

5. Conectar Dispositivo Emulado  
Este comando permite conectar um dispositivo emulado e configurar o servidor. Se esta for a primeira vez que você executa o emulador, pode levar alguns minutos para iniciar.

6. Bloquear dispositivo  
Este comando permite bloquear um dispositivo Android.

7. Desbloquear Dispositivo  
Este comando permite desbloquear um dispositivo Android. Disponível apenas se o tipo e o código de desbloqueio tiverem sido definidos no comando de conexão.

8. Obter informações do aplicativo atual  
Este comando permite obter o nome do pacote e o nome da atividade do aplicativo que está sendo executado atualmente no dispositivo Android.

9. Iniciar aplicação  
Este comando permite iniciar um aplicativo no dispositivo Android. Para obter o nome do pacote e o nome da atividade, você pode usar o comando Obter informações do aplicativo atual

10. Swipe simples  
Esse comando permite que você faça um simples swipe na tela do dispositivo Android.

11. Toque nas coordenadas  
Este comando permite tocar em uma coordenada específica na tela.

12. Toque no elemento  
Este comando permite tocar em um elemento específico na tela.

13. Enviar teclas  
Esse comando permite enviar teclas para um seletor específico no dispositivo Android.

14. Extrair texto  
Este comando permite obter o texto de um seletor específico do dispositivo Android.

15. Extrair texto por coordenadas  
Este comando permite obter o texto de um elemento localizado em uma posição específica do dispositivo Android.

16. Zoom em coordenadas  
Este comando permite dar zoom in ou zoom out nas coordenadas especificadas no dispositivo Android.

17. Zoom em objeto  
Este comando permite dar zoom in ou zoom out em um objeto no dispositivo Android.

18. Captura de tela  
Este comando permite capturar a tela do dispositivo Android e armazenar a imagem no caminho especificado.

19. Executar comando no dispositivo  
Este comando permite executar um comando no terminal do dispositivo Android. Para executar este comando corretamente, a caixa de seleção Permitir shell no comando de conexão deve estar marcada.

20. Aguardar por objeto  
Este comando permite aguardar por um objeto no dispositivo Android. O comando será executado até que o objeto seja encontrado ou até que o tempo máximo de espera seja atingido.

21. Desconectar dispositivo  
Este comando permite desconectar o dispositivo Android ou emulado que está sendo automatizado.  




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