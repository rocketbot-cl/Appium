# Appium
  
Module to automate mobile devices  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Configure Appium  
This command checks if Appium and the uiautomator2 driver is installed. If any of the dependencies is not installed, it will be installed automatically.

2. Pair device  
This command allows you to pair an Android device with the machine you want to connect to. This step is necessary to perform only once per device if you want to connect via WIFI.

3. Connect Android  
This command allows you to connect an Android device and configure the server using Android Debug Bridge (ADB). Developer options must be enabled on the device, and wireless or USB debugging as appropriate.

4. List Emulated Devices  
This command allows you to list the available emulated devices.

5. Connect Emulated Device  
This command allows you to connect an emulated device and configure the server.

6. Lock device  
This command allows you to lock an Android device.

7. Unlock Device  
This command allows you to unlock an Android device. Only available if the unlock type and code have been set in the connection command.

8. Get Current Application Information  
This command allows you to get the package name and activity name of the application that is currently running on the Android device.

9. Start application  
This command allows you to start an application on the Android device. To get the package name and activity name, you can use the Get Current Application Information command

10. Simple Swipe  
This command allows you to perform a simple swipe on the Android device screen.

11. Tap on coordinates  
This command allows you to tap on a specific coordinate on the screen.

12. Tap on element  
This command allows you to tap on a specific element on the screen.

13. Send keys  
This command allows you to send keys to a specific selector of the Android device.

14. Get text  
This command allows you to get the text of a specific selector of the Android device.

15. Get text by coordinates  
This command allows you to get the text of an element located at a specific position of the Android device.

16. Zoom in coordinates  
This command allows you to zoom in or zoom out on the coordinates specified on the Android device.

17. Zoom in object  
This command allows you to zoom in or zoom out on an object on the Android device.

18. Screenshot  
This command allows you to capture the screen of the Android device and store the image in the specified path.

19. Run command on device  
This command allows you to run a command on the Android device terminal. To run this command correctly, the Allow shell checkbox in the connection command must be checked.

20. Disconnect device  
This command allows you to disconnect the Android or emulated device that is being automated  




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