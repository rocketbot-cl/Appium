# Appium
  
Module to automate mobile devices  

*Read this in other languages: [English](Manual_Appium.md), [Português](Manual_Appium.pr.md), [Español](Manual_Appium.es.md)*
  
![banner](imgs/Banner_Appium.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

# Pre-configuration instructions for using the Appium module


## Previous installations
To be able to use the module, it is necessary to have npm and nodejs installed. For this, you can follow the following [link](https://nodejs.org/en/download/).
npm is the nodejs package manager, and it is necessary to be able to install Appium. It is recommended to install in the default location to avoid errors in execution.


### Appium and uiautomator2 installation and configuration
Once npm is installed, you can proceed to install Appium and the driver used. To do this, you can run the Configure Appium command of the module. However, if you want to perform the installation manually, you can follow the following [link](http://appium.io/docs/en/2.1/quickstart/install/) to install Appium and the following [link](http://appium.io/docs/en/2.1/quickstart/uiauto2-driver/) to install the driver.


### Download and installation of Android Studio
The module uses tools from the Android Studio Software 
kit, so it is necessary to install it. To do this, you can download it from the following [link](https://developer.android.com/studio). Once downloaded, you must run the installer and follow the steps indicated. It is recommended to install in the default location to avoid errors in execution.


## Add environment variables
To execute the module commands, you need to have certain paths added to the system PATH so that everything works correctly. To do this, follow these steps:
1. In the Windows search bar, type Environment Variables and select the Edit System Environment Variables option.
2. In the window that opens, select Environment Variables.
3. In the new window, you must create a new system variable. As a name, write ANDROID_HOME and as a value the absolute path to the folder `C:\Users\user\AppData\Local\Android\Sdk` (replace user with the computer username).
4. Then, select the Path variable and click Edit.
5. In the new window, click New and add the same path used in the 
previous step by adding the `platform-tools` folder at the end. For example, `C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (replace user with the computer username).
6. Finally, click OK in all windows and restart the computer.
7. To verify that everything has been done correctly, open a command prompt and type adb. If everything is fine, a list of available commands should appear.
8. After completing these steps, you can proceed to execute the module commands.


## Android device configuration
To connect the device correctly, it is necessary to configure the Android device to accept the connection, either by USB or by WiFi. To do this, follow these steps:
1. Activate developer options: On the device, go to Settings > About phone > Build number. Tap Build number 7 times. A message will appear saying that you are now a developer.
2. Activate USB debugging: On the device, go to Settings > System > Developer options and turn on USB debugging.
3. Activate wireless debugging: On 
the device, go to Settings > System > Developer options and turn on Wireless debugging.
4. If you want to use the wireless connection (WIFI) you must pair the device so that it can connect. To do this, you must use the Link device command once.
5. If you want to use the USB connection, you must connect the device to the computer using the USB cable. Then, you must run the Connect device command.
6. If everything was configured correctly, the Connect Android command should return True.


## Appium inspector
The Appium tool has an inspector to be able to visualize the elements of the device screen. To download it, you can follow the following [link](https://github.com/appium/appium-inspector/releases)


### Use Appium inspector
When unzipping the tool, you can run Appium Inspector.exe, which will open the tool window. To connect the Android device that was connected using the module in Rocketbot, you must go to the `Attach to Session ...` tab then in the reload button next to the input 
to enter the ID. If everything was configured correctly, a string should appear in the input where the ID of the connection, the device, its ip and port, and the uiautomator2 driver are indicated. Then, you must click on the Attach to Session button. This will open a new window of the inspector showing the device information.


## Description of the commands

### Configure Appium
  
This command checks if Appium and the uiautomator2 driver is installed. If any of the dependencies is not installed, it will be installed automatically.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Assign result of the configuration to a variable|result|

### Pair device
  
This command allows you to pair an Android device with the machine you want to connect to. This step is necessary to perform only once per device if you want to connect via WIFI.
|Parameters|Description|example|
| --- | --- | --- |
|IP address and port of the device|IP address and port of the Android device you want to connect|ip:port|
|WIFI pairing code|WIFI pairing code of the Android device you want to pair|876543|
|Assign result to variable|Assign result of connection to a variable|result|

### Connect Android
  
This command allows you to connect an Android device and configure the server using Android Debug Bridge (ADB). Developer options must be enabled on the device, and wireless or USB debugging as appropriate.
|Parameters|Description|example|
| --- | --- | --- |
|IP address and port of the device|IP address and port of the Android device you want to connect|ip:port|
|Connection type|Type of connection to use|USB|
|Assign result to variable|Assign result of connection to a variable|result|

### Simple Swipe
  
This command allows you to perform a simple swipe on the Android device screen.
|Parameters|Description|example|
| --- | --- | --- |
|Swipe direction|Direction that the swipe will have on the device screen.|Right|

### Tap on coordinates
  
This command allows you to tap on a specific coordinate on the screen.
|Parameters|Description|example|
| --- | --- | --- |
|Coordinate X|X coordinate where the tap will be performed|100|
|Coordinate Y|Y coordinate where the tap will be performed|100|

### Send keys
  
This command allows you to send keys to a specific selector of the Android device.
|Parameters|Description|example|
| --- | --- | --- |
|Data type|Data type of the selector in which the keys will be sent.|id|
|Selector|Selector in which the keys will be sent.|com.whatsapp:id/entry|
|Keys|Keys to be sent to the selector.|Hello world!|

### Get text
  
This command allows you to get the text of a specific selector of the Android device.
|Parameters|Description|example|
| --- | --- | --- |
|Data type|Data type of the selector in which the keys will be sent.|id|
|Selector|Selector in which the keys will be sent.|com.whatsapp:id/entry|
|Assign result to variable|Name of the variable in which the result will be assigned.|variable|

### Disconnect Android
  
This command allows you to disconnect the Android device being automated.
|Parameters|Description|example|
| --- | --- | --- |
