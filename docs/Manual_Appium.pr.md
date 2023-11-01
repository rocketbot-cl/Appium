# Appium
  
Módulo para automatizar dispositivos móveis  

*Read this in other languages: [English](Manual_Appium.md), [Português](Manual_Appium.pr.md), [Español](Manual_Appium.es.md)*
  
![banner](imgs/Banner_Appium.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



# Instruções de pré-configuração para usar o módulo Appium


## Instalações anteriores
Para poder usar o módulo, é necessário ter npm e nodejs instalados. Para isso, você pode seguir o seguinte [link](https://nodejs.org/en/download/).
npm é o gerenciador de pacotes nodejs, e é necessário para poder instalar o Appium. É recomendável instalar no local padrão para evitar erros na execução.


### Instalação e configuração do Appium e uiautomator2
Depois de instalado o npm, você pode prosseguir para instalar o Appium e o driver usado. Para fazer isso, você pode executar o comando Configure Appium do módulo. No entanto, se você quiser realizar a instalação manualmente, pode seguir o seguinte [link](http://appium.io/docs/en/2.1/quickstart/install/) para instalar o Appium e o seguinte [link](http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) para instalar o driver.


### Download e instalação do Android Studio
O módulo usa ferramentas do kit de software do Android Studio, portanto, é 
necessário instalá-lo. Para fazer isso, você pode baixá-lo no seguinte [link](https://developer.android.com/studio). Depois de baixado, você deve executar o instalador e seguir as etapas indicadas. É recomendável instalar no local padrão para evitar erros na execução.

### Baixe as ferramentas de linha de comando do Android Studio
Se você deseja se conectar com um dispositivo emulado, é necessário fazê-lo com as ferramentas de linha de comando. Eles podem ser baixados acessando o Android Studio. No menu superior, você deve ir para a opção Tools > SDK Manager. Na janela que se abre, você deve selecionar a guia SDK Tools. Na lista de ferramentas, você deve selecionar Android SDK Command-line Tools e clicar em Apply. Em seguida, clique em OK. Depois de baixado, você deve adicionar às variáveis ​​de ambiente o caminho para a pasta usada pela ferramenta `emulator`. Verifique a seguinte seção para ver como adicionar variáveis ​​de ambiente, no ponto 9 é especificado o caminho a ser 
adicionado.


## Adicionar variáveis ​​de ambiente
Para executar os comandos do módulo, você precisa ter determinados caminhos adicionados ao PATH do sistema para que tudo funcione corretamente. Para fazer isso, siga estas etapas:
1. Na barra de pesquisa do Windows, digite Variáveis ​​de ambiente e selecione a opção Editar variáveis ​​de ambiente do sistema.
2. Na janela que se abre, selecione Variáveis ​​de ambiente.
3. Na nova janela, você deve criar uma nova variável do sistema. Como nome, escreva ANDROID_HOME e como valor o caminho absoluto para a pasta `C:\Users\user\AppData\Local\Android\Sdk` (substitua o usuário pelo nome de usuário do computador).
4. Em seguida, selecione a variável Path e clique em Editar.
5. Na nova janela, clique em Novo e adicione o mesmo caminho usado na etapa anterior, adicionando a pasta `platform-tools` no final. Por exemplo, `C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (substitua o usuário pelo nome de usuário do computador).
6. Por fim, 
clique em OK em todas as janelas e reinicie o computador.
7. Para verificar se tudo foi feito corretamente, abra um prompt de comando e digite adb. Se tudo estiver bem, uma lista de comandos disponíveis deve aparecer.
8. Em caso de instalar as ferramentas de linha de comando, o caminho para a pasta `C:\Users\user\AppData\Local\Android\Sdk\emulator` (substitua o usuário pelo nome de usuário do computador) deve ser adicionado ao caminho.
9. Depois de concluir estas etapas, você pode prosseguir para executar os comandos do módulo.


## Configuração do dispositivo Android
### Essas etapas são necessárias apenas se você quiser se conectar a um dispositivo Android físico. Se você quiser se conectar a um dispositivo emulado, deverá seguir a seção Criar um dispositivo emulado.
Para conectar o dispositivo corretamente, é necessário configurar o dispositivo Android para aceitar a conexão, seja por USB ou por WiFi. Para fazer isso, siga estas etapas:
1. Ative as opções do desenvolvedor: No 
dispositivo, vá para Configurações > Sobre o telefone > Número da compilação. Toque no número da compilação 7 vezes. Uma mensagem aparecerá dizendo que você agora é um desenvolvedor.
2. Ative a depuração USB: No dispositivo, vá para Configurações > Sistema > Opções do desenvolvedor e ative a depuração USB.
3. Ative a depuração sem fio: No dispositivo, vá para Configurações > Sistema > Opções do desenvolvedor e ative a depuração sem fio.
4. Se você deseja usar a conexão sem fio (WIFI), deve parear o dispositivo para que ele possa se conectar. Para fazer isso, você deve usar o comando Link device uma vez.
5. Se você deseja usar a conexão USB, deve conectar o dispositivo ao computador usando o cabo USB. Em seguida, você deve executar o comando Connect device.
6. Se tudo foi configurado corretamente, o comando Connect Android deve retornar True.


## Inspetor Appium
A ferramenta Appium possui um inspetor para poder visualizar os elementos da tela do dispositivo. Para baixá-lo, você pode 
seguir o seguinte [link](https://github.com/appium/appium-inspector/releases)


### Use o inspetor Appium
Ao descompactar a ferramenta, você pode executar o Appium Inspector.exe, que abrirá a janela da ferramenta. Para conectar o dispositivo Android que foi conectado usando o módulo no Rocketbot, você deve ir para a guia `Attach to Session ...` e depois no botão de recarregar ao lado da entrada para inserir o ID. Se tudo foi configurado corretamente, uma string deve aparecer na entrada onde o ID da conexão, o dispositivo, seu ip e porta e o driver uiautomator2 são indicados. Em seguida, você deve clicar no botão Attach to Session. Isso abrirá uma nova janela do inspetor mostrando as informações do dispositivo.

### Criar um dispositivo emulado
Para poder criar um dispositivo emulado, você deve abrir o Android Studio e criar um novo projeto. Na janela que se abre, do lado direito você terá o Device Manager (Se não estiver aberto, na barra lateral direita você pode abri-lo). Você deve 
clicar em Create Device. Em seguida, você deve selecionar o dispositivo que deseja emular e clicar em Avançar. Na próxima janela, você deve selecionar a versão do Android que deseja emular e clicar em Avançar. Na última janela, você deve verificar a configuração do dispositivo e clicar em Concluir. Feito isso, você deve executar o comando Connect emulated device para poder usá-lo.



## Descrição do comando

### Configurar Appium
  
Este comando verifica se o Appium e o driver uiautomator2 estão instalados. Se alguma das dependências não estiver instalada, ela será instalada automaticamente.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a variável|Atribuir resultado da configuração a uma variável|result|

### Emparelhar dispositivo
  
Este comando permite emparelhar um dispositivo Android com a máquina que você deseja conectar. Esta etapa é necessária para realizar apenas uma vez por dispositivo se você deseja se conectar via WIFI.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|IP e porta do dispositivo|IP e porta do dispositivo Android que você deseja conectar|ip:port|
|Código de emparelhamento WIFI|Código de emparelhamento WIFI do dispositivo Android que você deseja emparelhar|876543|
|Atribuir resultado a variável|Atribuir resultado da conexão a uma variável|result|

### Conectar Android
  
Este comando permite conectar um dispositivo Android e configurar o servidor utilizando Android Debug Bridge (ADB). As opções do desenvolvedor devem estar ativadas no dispositivo e a depuração sem fio ou USB conforme apropriado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|IP e porta do dispositivo|IP e porta do dispositivo Android que você deseja conectar|ip:port|
|Tipo de conexão|Tipo de conexão a ser usada|USB|
|Tipo de desbloqueio|Tipo de desbloqueio a ser usado|PIN|
|Código de desbloqueio|Código de desbloqueio do dispositivo Android que você deseja conectar|1234|
|Permitir shell|Permite executar comandos usando o terminal no dispositivo Android. É um recurso inseguro. Para mais informações, consulte https//appium.io/docs/en/2.0/guides/security/|True|
|Atribuir resultado a variável|Atribuir resultado da conexão a uma variável|result|

### Listar dispositivos emulados
  
Este comando permite listar os dispositivos emulados disponíveis.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado a variável|Atribuir resultado da operação a uma variável|result|

### Conectar Dispositivo Emulado
  
Este comando permite conectar um dispositivo emulado e configurar o servidor.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do emulador|Nome do emulador que você deseja conectar|Pixel_7_Pro_API_34|
|Permitir shell|Permite executar comandos usando o terminal no dispositivo Android. É um recurso inseguro. Para mais informações, consulte https//appium.io/docs/en/2.0/guides/security/|True|
|Tipo de desbloqueio|Tipo de desbloqueio a ser usado|PIN|
|Código de desbloqueio|Código de desbloqueio do dispositivo Android que você deseja conectar|1234|
|Atribuir resultado a variável|Atribuir resultado da conexão a uma variável|result|

### Bloquear dispositivo
  
Este comando permite bloquear um dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### Desbloquear Dispositivo
  
Este comando permite desbloquear um dispositivo Android. Disponível apenas se o tipo e o código de desbloqueio tiverem sido definidos no comando de conexão.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### Obter informações do aplicativo atual
  
Este comando permite obter o nome do pacote e o nome da atividade do aplicativo que está sendo executado atualmente no dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado à variável|Nome da variável na qual o resultado será atribuído.|variável|

### Iniciar aplicação
  
Este comando permite iniciar um aplicativo no dispositivo Android. Para obter o nome do pacote e o nome da atividade, você pode usar o comando Obter informações do aplicativo atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do pacote|Nome do pacote do aplicativo que você deseja iniciar.|com.android.Settings|
|Nome da atividade|Nome da atividade do aplicativo que você deseja iniciar.|.Settings|
|Atribuir resultado à variável|Nome da variável na qual o resultado será atribuído.|variável|

### Swipe simples
  
Esse comando permite que você faça um simples swipe na tela do dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Direção do swipe|Direção que o swipe terá na tela do dispositivo.|Right|

### Toque nas coordenadas
  
Este comando permite tocar em uma coordenada específica na tela.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Coordenada X|Coordenada X onde o toque será realizado|100|
|Coordenada Y|Coordenada Y onde o toque será realizado|100|

### Toque no elemento
  
Este comando permite tocar em um elemento específico na tela.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de dado|Tipo de dado do seletor no qual o toque será realizado.|id|
|Seletor|Seletor no qual o toque será realizado.|com.whatsapp:id/entry|
|Atribuir resultado à variável|Nome da variável na qual o resultado será atribuído.|variável|

### Enviar teclas
  
Esse comando permite enviar teclas para um seletor específico no dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de dado|Tipo de dado do seletor no qual as teclas serão enviadas.|id|
|Seletor|Seletor no qual as teclas serão enviadas.|com.whatsapp:id/entry|
|Teclas|Teclas a serem enviadas para o seletor.|Olá mundo!|

### Extrair texto
  
Este comando permite obter o texto de um seletor específico do dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de dado|Tipo de dado do seletor no qual as teclas serão enviadas.|id|
|Seletor|Seletor no qual as teclas serão enviadas.|com.whatsapp:id/entry|
|Atribuir resultado à variável|Nome da variável na qual o resultado será atribuído.|variável|

### Extrair texto por coordenadas
  
Este comando permite obter o texto de um elemento localizado em uma posição específica do dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Coordenadas x,y|Coordenadas x,y do elemento para obter o texto.|450,2000|
|Atribuir resultado à variável|Nome da variável na qual o resultado será atribuído.|variável|

### Zoom em coordenadas
  
Este comando permite dar zoom in ou zoom out nas coordenadas especificadas no dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de zoom|Tipo de zoom a realizar.|Zoom in|
|Coordenadas x,y|Coordenadas x,y onde o zoom será realizado.|450,2000|
|Pixels a deslocar|Pixels a deslocar no zoom.|500|
|Velocidade de zoom|Velocidade de zoom a realizar.|Normal|

### Zoom em objeto
  
Este comando permite dar zoom in ou zoom out em um objeto no dispositivo Android.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de zoom|Tipo de zoom a realizar.|Zoom in|
|Tipo de dado|Tipo de dado do seletor no qual o zoom será realizado.|id|
|Seletor|Seletor no qual realizará o zoom|com.whatsapp:id/entry|
|Pixels a deslocar|Pixels a deslocar no zoom.|500|
|Velocidade de zoom|Velocidade de zoom a realizar.|Normal|

### Captura de tela
  
Este comando permite capturar a tela do dispositivo Android e armazenar a imagem no caminho especificado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho da imagem|Caminho no qual a imagem será armazenada.|C:/Users/User/Desktop/imagen.png|

### Executar comando no dispositivo
  
Este comando permite executar um comando no terminal do dispositivo Android. Para executar este comando corretamente, a caixa de seleção Permitir shell no comando de conexão deve estar marcada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Comando|Comando a ser executado no terminal do dispositivo.|pm list packages|
|Atribuir resultado à variável|Nome da variável na qual o resultado será atribuído.|variável|

### Desconectar dispositivo
  
Este comando permite desconectar o dispositivo Android ou emulado que está sendo automatizado.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
