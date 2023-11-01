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

### Download Android Studio command line tools
If you want to connect with an emulated device, it is necessary to do it with the command line tools. They can be downloaded by accessing Android Studio. In the top menu you must go to the Tools > SDK Manager option. In the window that opens, you must select the SDK Tools tab. In the list of tools, you must select Android SDK Command-line Tools and click Apply. Then click OK. Once downloaded, you must add to the environment variables the path to the folder used by the tool `emulator`. Check the following section to see how to add environment variables, in point 9 the path to add is specified.


## Add environment variables
To execute the module 
commands, you need to have certain paths added to the system PATH so that everything works correctly. To do this, follow these steps:
1. In the Windows search bar, type Environment Variables and select the Edit System Environment Variables option.
2. In the window that opens, select Environment Variables.
3. In the new window, you must create a new system variable. As a name, write ANDROID_HOME and as a value the absolute path to the folder `C:\Users\user\AppData\Local\Android\Sdk` (replace user with the computer username).
4. Then, select the Path variable and click Edit.
5. In the new window, click New and add the same path used in the previous step by adding the `platform-tools` folder at the end. For example, `C:\Users\user\AppData\Local\Android\Sdk\platform-tools` (replace user with the computer username).
6. Finally, click OK in all windows and restart the computer.
7. To verify that everything has been done correctly, open a command prompt and type adb. If everything is fine, a 
list of available commands should appear.
8. In case of installing the command line tools, the path to the folder `C:\Users\user\AppData\Local\Android\Sdk\emulator` (replace user with the computer username) must be added to the path.
9. After completing these steps, you can proceed to execute the module commands.


## Android device configuration
### These steps are only necessary if you want to connect with a physical Android device. If you want to connect with an emulated device, you must follow the Create an emulated device section.
To connect the device correctly, it is necessary to configure the Android device to accept the connection, either by USB or by WiFi. To do this, follow these steps:
1. Activate developer options: On the device, go to Settings > About phone > Build number. Tap Build number 7 times. A message will appear saying that you are now a developer.
2. Activate USB debugging: On the device, go to Settings > System > Developer options and turn on USB debugging.
3. 
Activate wireless debugging: On the device, go to Settings > System > Developer options and turn on Wireless debugging.
4. If you want to use the wireless connection (WIFI) you must pair the device so that it can connect. To do this, you must use the Link device command once.
5. If you want to use the USB connection, you must connect the device to the computer using the USB cable. Then, you must run the Connect device command.
6. If everything was configured correctly, the Connect Android command should return True.


## Appium inspector
The Appium tool has an inspector to be able to visualize the elements of the device screen. To download it, you can follow the following [link](https://github.com/appium/appium-inspector/releases)


### Use Appium inspector
When unzipping the tool, you can run Appium Inspector.exe, which will open the tool window. To connect the Android device that was connected using the module in Rocketbot, you must go to the `Attach to Session ...` tab then in the 
reload button next to the input to enter the ID. If everything was configured correctly, a string should appear in the input where the ID of the connection, the device, its ip and port, and the uiautomator2 driver are indicated. Then, you must click on the Attach to Session button. This will open a new window of the inspector showing the device information.

### Create an emulated device
To be able to create an emulated device, you must open Android Studio and create a new project. In the window that opens, on the right side you will have the Device Manager (If it is not open, from the right side bar you can open it). You must click on Create Device. Then, you must select the device you want to emulate and click Next. In the next window, you must select the Android version you want to emulate and click Next. In the last window, you must verify the device configuration and click Finish. Once done, you must run the Connect emulated device command to be able to use it.


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
|Unlock type|Type of unlock to use|PIN|
|Unlock code|Unlock code of the Android device you want to connect|1234|
|Allow shell|Allows you to run commands using the terminal on the Android device. It is an unsafe feature. For more information, see https//appium.io/docs/en/2.0/guides/security/|True|
|Assign result to variable|Assign result of connection to a variable|result|

### List Emulated Devices
  
This command allows you to list the available emulated devices.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Assign result of operation to a variable|result|

### Connect Emulated Device
  
This command allows you to connect an emulated device and configure the server.
|Parameters|Description|example|
| --- | --- | --- |
|Emulator name|Name of the emulator you want to connect|Pixel_7_Pro_API_34|
|Allow shell|Allows you to run commands using the terminal on the Android device. It is an unsafe feature. For more information, see https//appium.io/docs/en/2.0/guides/security/|True|
|Unlock type|Type of unlock to use|PIN|
|Unlock code|Unlock code of the Android device you want to connect|1234|
|Assign result to variable|Assign result of connection to a variable|result|

### Lock device
  
This command allows you to lock an Android device.
|Parameters|Description|example|
| --- | --- | --- |

### Unlock Device
  
This command allows you to unlock an Android device. Only available if the unlock type and code have been set in the connection command.
|Parameters|Description|example|
| --- | --- | --- |

### Get Current Application Information
  
This command allows you to get the package name and activity name of the application that is currently running on the Android device.
|Parameters|Description|example|
| --- | --- | --- |
|Assign result to variable|Name of the variable in which the result will be assigned.|variable|

### Start application
  
This command allows you to start an application on the Android device. To get the package name and activity name, you can use the Get Current Application Information command
|Parameters|Description|example|
| --- | --- | --- |
|Package name|Name of the package of the application you want to start.|com.android.Settings|
|Activity name|Name of the activity of the application you want to start.|.Settings|
|Assign result to variable|Name of the variable in which the result will be assigned.|variable|

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

### Tap on element
  
This command allows you to tap on a specific element on the screen.
|Parameters|Description|example|
| --- | --- | --- |
|Data type|Data type of the selector in which the tap will be performed.|id|
|Selector|Selector in which the tap will be performed.|com.whatsapp:id/entry|
|Assign result to variable|Name of the variable in which the result will be assigned.|variable|

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

### Get text by coordinates
  
This command allows you to get the text of an element located at a specific position of the Android device.
|Parameters|Description|example|
| --- | --- | --- |
|Coordinates x,y|Coordinates x,y of the element to get the text.|450,2000|
|Assign result to variable|Name of the variable in which the result will be assigned.|variable|

### Zoom in coordinates
  
This command allows you to zoom in or zoom out on the coordinates specified on the Android device.
|Parameters|Description|example|
| --- | --- | --- |
|Type of zoom|Type of zoom to perform.|Zoom in|
|Coordinates x,y|Coordinates x,y where the zoom will be performed.|450,2000|
|Pixels to move|Pixels to move in the zoom.|500|
|Zoom speed|Zoom speed to perform.|Normal|

### Zoom in object
  
This command allows you to zoom in or zoom out on an object on the Android device.
|Parameters|Description|example|
| --- | --- | --- |
|Type of zoom|Type of zoom to perform.|Zoom in|
|Data type|Data type of the selector in which the zoom will be performed.|id|
|Selector|Selector in which to perform the zoom|com.whatsapp:id/entry|
|Pixels to move|Pixels to move in the zoom.|500|
|Zoom speed|Zoom speed to perform.|Normal|

### Screenshot
  
This command allows you to capture the screen of the Android device and store the image in the specified path.
|Parameters|Description|example|
| --- | --- | --- |
|Image path|Path in which the image will be stored.|C:/Users/User/Desktop/imagen.png|

### Run command on device
  
This command allows you to run a command on the Android device terminal. To run this command correctly, the Allow shell checkbox in the connection command must be checked.
|Parameters|Description|example|
| --- | --- | --- |
|Command|Command to be executed in the device terminal.|pm list packages|
|Assign result to variable|Name of the variable in which the result will be assigned.|variable|

### Disconnect device
  
This command allows you to disconnect the Android or emulated device that is being automated
|Parameters|Description|example|
| --- | --- | --- |
