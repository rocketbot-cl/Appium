import re
import os
import time
import psutil
import base64
import subprocess
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium_selenium.webdriver.common.action_chains import ActionChains
from appium_selenium.webdriver.common.actions import interaction
from appium_selenium.webdriver.common.actions.action_builder import ActionBuilder
from appium_selenium.webdriver.common.actions.pointer_input import PointerInput

data_types = {
    "id": AppiumBy.ID,
    "xpath": AppiumBy.XPATH,
    "class": AppiumBy.CLASS_NAME
}

class AppiumObject:
    def __init__(self, device_ip, connection_type, allow_shell, unlock_type, unlock_key, is_emulator, emulator_name):
        """
        This function initializes the AppiumObject class.

        Args:
            device_ip (str): The IP of the device.
            connection_type (str): The connection type. Can be 'USB' or 'WIFI'.
            allow_shell (bool): If True, it allows the use of shell commands.
            unlock_type (str): The unlock type. Can be 'PIN', 'PASSWORD', 'PATTERN' or 'NONE'.
            unlock_key (str): The unlock key. The PIN, PASSWORD or PATTERN.
            is_emulator (bool): If True, it indicates that the device is an emulator.
            emulator_name (str): The name of the emulator.
        """
        self.device_ip = device_ip
        self.connection_type = connection_type
        self.allow_shell = allow_shell
        self.unlock_type = unlock_type
        self.unlock_key = unlock_key
        self.is_emulator = is_emulator
        self.emulator_name = emulator_name
        self.android_driver = None
        
        if is_emulator:
            self.connect_emulator()
        else:
            self.connect_device()


    def connect_device(self):
        """
        This function is used to connect to an Android device for automation. It first kills any existing server. 

        If the 'allow_shell' attribute is True, it starts the Appium server with the '--allow-insecure=adb_shell' option, otherwise it starts the Appium server normally.

        It then starts the adb server and attempts to connect to the device. The connection type can be either 'wifi' or 'usb'. 

        If the connection type is 'wifi', it attempts to connect to the device using its IP address. If the connection type is 'usb', it lists the connected adb devices.

        If the output of the connection command contains 'unauthorized', it raises an exception with instructions to authorize USB debugging on the device.

        If the output of the connection command contains 'connected' or 'device', it sets up the desired capabilities for Appium and creates a new webdriver instance.

        If a subprocess.CalledProcessError is raised during this process, it checks the SDK installation and raises an exception with instructions specific to the connection type.
        """
        self.kill_server()

        if self.allow_shell:
            print("Allowing insecure adb shell")
            appium_command = "appium --allow-insecure=adb_shell"
        else:
            appium_command = "appium"

        try:
            subprocess.Popen(appium_command, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

            subprocess.run("adb start-server")

            if self.connection_type == "wifi":
                output = subprocess.check_output(f"adb connect {self.device_ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            elif self.connection_type == "usb":
                output = subprocess.check_output("adb devices", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

            if "unauthorized" in output:
                raise Exception("Error connecting to device. It's necessary to accept the USB debugging authorization in the device. Disconnect your phone from the computer, go to the developer options in the device and first disable USB debugging, then revoke all USB debugging authorizations, enable USB debugging and finally connect your device again. When the authorization dialog appears in your device, check the 'Always allow from this computer' option and click 'OK'. Finally, execute the command again.")

            elif "connected" or "device" in output:
                caps = {}
                caps["platformName"] = "Android"
                caps["appium:automationName"] = "uiautomator2"
                caps["appium:deviceName"] = "Android Device"
                caps["appium:ensureWebviewsHavePages"] = True
                caps["appium:nativeWebScreenshot"] = True
                caps["appium:newCommandTimeout"] = 3600
                caps["appium:connectHardwareKeyboard"] = True
                caps["appium:unlockType"] = self.unlock_type
                caps["appium:unlockKey"] = self.unlock_key

                self.android_driver = webdriver.Remote("http://127.0.0.1:4723", caps)


        except subprocess.CalledProcessError as e:
            check_sdk()
            if self.connection_type == "wifi":
                raise Exception("Error connecting to device. First check if the device is connected to the same WIFI as the computer. Then check if the IP is correct. Finally, double check if the port entered in the command is the same as the one in the 'Wireless debugging' window and not from 'Pair device' window.")
            elif self.connection_type == "usb":
                raise Exception("Error connecting to device. First check if the device is connected to the computer. Then check if the USB debugging is activated in the device. If the error persists, go to the developer options in the device and revoke all USB debugging authorizations. Finally, execute the command again and accept the USB debugging authorization in the device.")
            

    def connect_emulator(self):
        """
        This function is used to connect to an Android emulator for automation. It first kills any existing server. 

        If the 'allow_shell' attribute is True, it starts the Appium server with the '--allow-insecure=adb_shell' option, otherwise it starts the Appium server normally.

        It then starts the adb server and attempts to start the emulator with the name specified in the 'emulator_name' attribute.

        It waits for the emulator to start and then sets up the desired capabilities for Appium and creates a new webdriver instance.

        If the webdriver creation fails, it waits for 30 seconds and tries again.

        If a subprocess.CalledProcessError is raised during this process, it checks the SDK installation and raises an exception with instructions to install the emulator from the SDK Manager in Android Studio.
        """
        try:
            self.kill_server()

            if self.allow_shell:
                print("Allowing insecure adb shell")
                appium_command = "appium --allow-insecure=adb_shell"
            else:
                appium_command = "appium"

            subprocess.Popen(appium_command, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

            subprocess.run("adb start-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            subprocess.Popen(f"emulator @{self.emulator_name}", shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)

            time.sleep(5)
            print("Waiting for emulator to start...")
            subprocess.run("adb wait-for-device")
            print("Emulator started successfully")

            caps = {}
            caps["platformName"] = "Android"
            caps["appium:automationName"] = "uiautomator2"
            caps["appium:deviceName"] = "Android Emulator"
            caps["appium:ensureWebviewsHavePages"] = True
            caps["appium:nativeWebScreenshot"] = True
            caps["appium:newCommandTimeout"] = 3600
            caps["appium:connectHardwareKeyboard"] = True
            caps["appium:unlockType"] = self.unlock_type
            caps["appium:unlockKey"] = self.unlock_key

            try:
                self.android_driver = webdriver.Remote("http://127.0.0.1:4723", caps)
            except Exception as e:
                print("Error connecting to emulator. Trying again...")
                time.sleep(30)
                self.android_driver = webdriver.Remote("http://127.0.0.1:4723", caps)

        except subprocess.CalledProcessError as e:
            check_sdk()
            raise Exception("Error connecting to emulator. Make sure to install the emulator from the SDK Manager in Android Studio.")


    @classmethod
    def kill_server(self):
        """
        This class method is used to kill the adb server, any running emulators, and any running Appium instances.

        It first attempts to kill any running emulators using the 'adb emu kill' command.

        It then kills the adb server using the 'adb kill-server' command.

        Finally, it iterates over all running processes and kills any process named 'adb.exe' or 'node.exe' that is running an Appium instance.
        """
        subprocess.run("adb emu kill", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.run("adb kill-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        for process in psutil.process_iter():
            if process.name() == "adb.exe":
                process.kill()
            if process.name() == "node.exe" and "appium" in str(process.cmdline()):
                process.kill()


    def simple_swipe(self, direction):
        """
        This function performs a simple swipe action on the Android device in the specified direction. 

        It first gets the window size of the device. 

        It then creates an ActionChains object and sets its w3c_actions attribute to an ActionBuilder object with a PointerInput of type POINTER_TOUCH.

        Depending on the direction specified, it moves the pointer to the appropriate location, presses down, moves to the destination location, and then releases.

        The directions can be "right", "left", "up", or "down". For "right" and "left", the swipe is horizontal and for "up" and "down", the swipe is vertical.

        Finally, it performs the actions.
        """
        size = self.android_driver.get_window_size()
        

        actions = ActionChains(self.android_driver)
        actions.w3c_actions = ActionBuilder(self.android_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

        if direction == "right":
            actions.w3c_actions.pointer_action.move_to_location((size["width"] - 1), (size["height"] / 2))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(1, (size["height"] / 2))

        elif direction == "left":
            actions.w3c_actions.pointer_action.move_to_location(1, (size["height"] / 2))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location((size["width"] - 1), (size["height"] / 2))

        elif direction == "up":
            actions.w3c_actions.pointer_action.move_to_location((size["width"] / 2), 1)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location((size["width"] / 2), (size["height"] - 1))

        elif direction == "down":
            actions.w3c_actions.pointer_action.move_to_location((size["width"] / 2), (size["height"] - 1))
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location((size["width"] / 2), 1)

        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def simple_tap(self, x, y):
        """
        This function performs a simple tap action on the Android device at the specified x and y coordinates.

        It first creates an ActionChains object and sets its w3c_actions attribute to an ActionBuilder object with a PointerInput of type POINTER_TOUCH.

        It then moves the pointer to the specified location, presses down, and then releases.

        Finally, it performs the actions.
        """
        actions = ActionChains(self.android_driver)
        actions.w3c_actions = ActionBuilder(self.android_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def tap_object(self, selector, data_type):
        """
        This function performs a tap action on a specific object on the Android device.

        It first finds the element on the screen using the provided selector and data type. The data type could be id, class name, xpath, etc.

        Once the element is found, it performs a click action on the element, effectively simulating a tap.
        """
        element = self.android_driver.find_element(by=data_types[data_type], value=selector)
        element.click()

    def send_keys(self, selector, data_type, text):
        """
        This function sends the specified text to a specific object on the Android device.

        It first finds the element on the screen using the provided selector and data type. The data type could be id, class name, xpath, etc.

        Once the element is found, it sends the provided text to the element.
        """
        element = self.android_driver.find_element(by=data_types[data_type], value=selector)
        element.send_keys(text)

    
    def get_text(self, selector, data_type):
        """
        This function retrieves the text from a specific object on the Android device.

        It first finds the element on the screen using the provided selector and data type. The data type could be id, class name, xpath, etc.

        Once the element is found, it retrieves and returns the text of the element.
        """
        element = self.android_driver.find_element(by=data_types[data_type], value=selector)

        return element.text

    def get_text_coord(self, coords):
        """
        This function retrieves the text from a specific coordinate on the Android device.

        It first splits the provided coordinates into x and y values.

        It then iterates over all elements on the screen. For each element, it retrieves the text and the bounds.

        If the element has no text, it continues to the next element.

        It then checks if the provided coordinates are within the bounds of the element. If they are, it returns the text of the element.

        If it has iterated over all elements and none of them contain the provided coordinates, it returns None.
        """
        x,y = coords.split(",")

        for element in self.android_driver.find_elements(by=AppiumBy.XPATH, value="//*"):
            text = element.get_attribute("text")

            if not text:
                continue
            bounds = element.get_attribute("bounds")
            bounds = bounds.replace("[", "").replace("]", ",").split(",")[:-1]

            if int(bounds[0]) <= int(x) <= int(bounds[2]) and int(bounds[1]) <= int(y) <= int(bounds[3]):
                return text

            if element == self.android_driver.find_elements(by=AppiumBy.XPATH, value="//*")[-1]:
                return None
            
    def get_screenshot(self, path):
        """
        This function takes a screenshot of the current screen on the Android device and saves it to the specified path.

        It first gets the screenshot as a base64 string using the 'get_screenshot_as_base64' method of the webdriver.

        It then decodes the base64 string to get the binary data of the screenshot.

        Finally, it opens the file at the specified path in write binary mode and writes the binary data to the file.
        """
        screenshotBase64 = self.android_driver.get_screenshot_as_base64()
        screenshotDecoded = base64.b64decode(screenshotBase64)

        with open(path, "wb") as f:
            f.write(screenshotDecoded)

    def lock(self):
        """
        This function locks the Android device.

        It first checks if the device is already locked using the 'is_locked' method of the webdriver. If it is, it raises an exception.

        If the device is not already locked, it locks the device using the 'lock' method of the webdriver.
        """
        if self.android_driver.is_locked():
            raise Exception("Device is already locked")

        self.android_driver.lock()

    def unlock(self):
        """
        This function unlocks the Android device.

        It first checks if the device is already unlocked using the 'is_locked' method of the webdriver. If it is, it raises an exception.

        If the device is not already unlocked, it unlocks the device using the 'unlock' method of the webdriver.
        """
        if not self.android_driver.is_locked():
            raise Exception("Device is already unlocked")

        self.android_driver.unlock()

    def coords_zoom(self, action, speed, coords, pixels):
        """
        This function performs a zoom in or zoom out action on the Android device at the specified coordinates with the specified speed and pixel distance.

        It first gets the window size of the device and calculates the center coordinates if none are provided.

        It then checks if the provided coordinates and pixel distance are within the bounds of the screen. If they are not, it raises an exception.

        It then creates two TouchAction objects and calculates the distance to move for each step of the zoom action.

        If the action is "zoom_in", it starts at the provided coordinates and moves the two TouchActions away from each other.

        If the action is "zoom_out", it starts the two TouchActions at a distance of 'pixels' away from the provided coordinates and moves them towards each other.

        Finally, it adds the two TouchActions to a MultiAction and performs the MultiAction.
        """
        screen_size = self.android_driver.get_window_size()
        width = screen_size["width"]
        height = screen_size["height"]
        print(width, height)

        xx = eval(coords.split(",")[0]) if coords else width // 2
        yy = eval(coords.split(",")[1]) if coords else height // 2

        if xx > width or yy > height or xx < 0 or yy < 0:
            raise Exception("Coordinates are out of bounds")

        if pixels > width or pixels > height or pixels < 0 or width < (xx + pixels) or height < (yy + pixels):
            raise Exception("Pixels are out of bounds")

        action1 = TouchAction(self.android_driver)
        action2 = TouchAction(self.android_driver)

        move_distance = pixels // speed
        
        if action == "zoom_in":
            action1.long_press(x=xx, y=yy)
            action2.long_press(x=xx, y=yy)

            for _ in range(speed):
                action1.move_to(x=xx, y=yy - move_distance)
                action2.move_to(x=xx, y=yy + move_distance)
                move_distance += pixels // speed

        if action == "zoom_out":
            action1.long_press(x=xx, y=yy + pixels)
            action2.long_press(x=xx, y=yy - pixels)

            for _ in range(speed):
                action1.move_to(x=xx, y=yy - move_distance + pixels)
                action2.move_to(x=xx, y=yy + move_distance - pixels)
                move_distance += pixels // speed

        m_action = MultiAction(self.android_driver)
        m_action.add(action1, action2)
        m_action.perform()

    def object_zoom(self, action, speed, selector, data_type, pixels):
        """
        This function performs a zoom in or zoom out action on a specific object on the Android device with the specified speed and pixel distance.

        It first checks if the pixel distance is greater than 0 and if a selector is provided. If not, it raises an exception.

        It then finds the element on the screen using the provided selector and data type and gets its bounds.

        It calculates the center coordinates of the element.

        It then creates two TouchAction objects and calculates the distance to move for each step of the zoom action.

        If the action is "zoom_in", it starts at the center of the element and moves the two TouchActions away from each other.

        If the action is "zoom_out", it starts the two TouchActions at a distance of 'pixels' away from the center of the element and moves them towards each other.

        Finally, it adds the two TouchActions to a MultiAction and performs the MultiAction.
        """
        if pixels < 0:
            raise Exception("Pixels must be greater than 0")

        if not selector:
            raise Exception("Please specify a selector")

        element = self.android_driver.find_element(by=data_types[data_type], value=selector)

        bounds = element.get_attribute("bounds")

        xx = (int(bounds.split("][")[0].replace("[", "").split(",")[0]) + int(bounds.split("][")[1].replace("]", "").split(",")[0])) // 2
        yy = (int(bounds.split("][")[0].replace("[", "").split(",")[1]) + int(bounds.split("][")[1].replace("]", "").split(",")[1])) // 2


        action1 = TouchAction(self.android_driver)
        action2 = TouchAction(self.android_driver)

        move_distance = pixels // speed

        if action == "zoom_in":
            action1.long_press(element)
            action2.long_press(element)

            for _ in range(speed):
                action1.move_to(x=xx, y=yy - move_distance)
                action2.move_to(x=xx, y=yy + move_distance)
                move_distance += pixels // speed
        
        if action == "zoom_out":
            action1.long_press(element)
            action2.long_press(element)


            for _ in range(speed):
                action1.move_to(x=xx, y=yy - move_distance + pixels)
                action2.move_to(x=xx, y=yy + move_distance - pixels)
                move_distance += pixels // speed

        m_action = MultiAction(self.android_driver)
        m_action.add(action1, action2)
        m_action.perform()

def check_appium():
    """
    This function checks if Appium is installed in the system by running the command 'appium -v'.
    If Appium is installed, it prints the installed version.
    If Appium is not installed, it tries to install it using the command 'npm i --location=global appium@2.1.3'.
    If the installation is successful, it prints 'Appium installed successfully'.
    In case of any error during the check or installation process, it raises the respective error.

    Raises:
        subprocess.CalledProcessError: If 'appium -v' command fails, indicating Appium is not installed.
        subprocess.CalledProcessError: If 'npm i --location=global appium@2.1.3' command fails, indicating npm is not installed.
    """
    try:
        # Check if appium is installed
        command = "appium -v"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        print("Appium version: ", output.strip())

    except subprocess.CalledProcessError:
        try:
            print("Appium is not installed. Installing...")

            command = "npm i --location=global appium@2.1.3"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            print("Appium installed successfully")
        
        except subprocess.CalledProcessError:
            raise Exception("You must install npm from https://nodejs.org/en/download/. Make sure to add to PATH the npm folder during the installation.")

def check_uiautomator():
    """
    This function checks if the uiautomator2 driver is installed in the system by running the command 'appium driver list'.
    It then searches the output for the string 'uiautomator2' followed by 'not installed'.
    If the uiautomator2 driver is not installed, it tries to install it using the command 'appium driver install uiautomator2@2.29.7'.
    If the installation is successful, it prints 'uiautomator2 driver installed successfully'.
    In case of any error during the check or installation process, it prints 'Error installing uiautomator2 driver' and raises the respective error.

    Raises:
        subprocess.CalledProcessError: If any error occurs during the check or installation process.
    """
    try:
        # Check if uiautomator2 driver is installed
        list_command = "appium driver list"
        output = subprocess.check_output(list_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True).strip()
        print(output)
        matches = re.search(r"uiautomator2.*?(not installed)", output, re.IGNORECASE)

        if matches:
            print("Installing uiautomator2 driver...")
            command = "appium driver install uiautomator2@2.29.7"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            print("uiautomator2 driver installed successfully")

    except subprocess.CalledProcessError:
        print("Error installing uiautomator2 driver")
        raise e

def check_sdk():
    """
    This function checks if adb (Android Debug Bridge) and emulator is installed in the system by running the command 'adb version' and 'emulator -version'.
    If adb and emulator is installed and in path, it prints the installed version.
    If adb or emulator is not installed, it raises an exception with a message instructing the user to install the SDK Tools from Android Studio, 
    which includes adb and emulator. The message includes a link to download Android Studio and instructions to add the platform-tools and emulator from the 
    SDK folder to the PATH after installation.

    Raises:
        subprocess.CalledProcessError: If 'adb version' or 'emulator -version' command fails, indicating that SDK Tools is not installed or the platform-tools/emulator is not in user PATH.
    """
    try:
        # Check if adb is installed and in path
        command = "adb version"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        print("adb version: ", output.strip())

        
        # Check if emulator is installed and in path
        command = "emulator -version"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        print("emulator version: ", output.strip())

    except subprocess.CalledProcessError:
        raise Exception("You must install the SDK Tools from Android Studio in order to use Appium. Download Android Studio here: https://developer.android.com/. For more information for how to install the SDK Tools visit https://developer.android.com/about/versions/14/setup-sdk#install-sdk. After the installation, you must add the platform-tools and the emulator folders from the SDK folder to the user PATH. For example C:\\Users\\<user>\\AppData\\Local\\Android\\Sdk\\platform-tools and C:\\Users\\<user>\\AppData\\Local\\Android\\Sdk\\emulator. Finally, restart Rocketbot.")

def check_java():
    """
    This function checks if Java is installed in the system by running the command 'java -version'.
    If Java is installed, it prints the installed version.
    If Java is not installed, it raises an exception with a message instructing the user to install Java.

    Raises:
        subprocess.CalledProcessError: If 'java -version' command fails, indicating Java is not installed.
    """
    try:
        # Check if Java is installed
        command = "java -version"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        print("Java version: ", output.strip())

    except subprocess.CalledProcessError:
        raise Exception("You must install Java in order to use Appium. Download Java here: https://www.java.com/en/download/. After the installation restart your computer.")

def check_path():
    """
    This function checks if the environment variable ANDROID_HOME are set in the system.
    ANDROID_HOME should point to the Android SDK folder.
    If this environment variable is not set, it raises an exception with a message instructing the user to set 
    the ANDROID_HOME environment variable to the Android SDK folder and then reload Rocketbot. The message includes a link 
    for more information on how to set these environment variables.

    Raises:
        Exception: If ANDROID_HOME environment variable is not set.
    """
    android_home = os.environ.get("ANDROID_HOME")
    android_sdk_root = os.environ.get("ANDROID_SDK_ROOT")

    if not android_home and not android_sdk_root:
        raise Exception("You must set the ANDROID_HOME environment variable to the Android SDK folder. For example C:\\Users\\<user>\\AppData\\Local\\Android\\Sdk and then Reload Rocketbot. For more information visit https://developer.android.com/studio/command-line/variables.")

def pair_device(ip, code):
    """
    This function pairs the device with the computer using the IP and code.
    It runs the command 'adb pair <ip> <code>' and checks the output for the string 'successfully'.
    If the pairing is successful, it prints 'Device paired successfully'.
    In case of any error during the pairing process, it prints 'Error pairing device. Please check the IP and code' and raises the respective error.

    Args:
        ip (str): The IP of the device.
        code (str): The code of the device.
    Returns:
        result (bool): True if the pairing is successful, False otherwise.
    """
    try:
        subprocess.run("adb kill-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        subprocess.run("adb start-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        output = subprocess.check_output(f"adb pair {ip} {code}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        if "successfully" in output.lower():
            return True
        else:
            return False

    except subprocess.CalledProcessError:
        check_sdk()
        raise Exception("Error pairing device. First check if the device is connected to the same WIFI as the computer. Then check if the IP and code are correct. Make sure to activate the wireless debugging in the device. Finally, double check if the port entered in the command is the same as the one in the 'Pair device' window and not from 'Wireless debugging' window.")
    
def list_emulators():
    """
    This function lists all the Android Virtual Devices (AVDs) available in the system by running the command 'emulator -list-avds'.
    It then splits the output by newline characters to get a list of emulator names. It filters out any empty strings from the list and returns it.

    If the 'emulator -list-avds' command fails, it checks the SDK installation and raises an exception with a message instructing the user to install the emulator from the SDK Manager in Android Studio.

    Raises:
        subprocess.CalledProcessError: If 'emulator -list-avds' command fails, indicating the emulator is not installed.
        Exception: If there is an error listing the emulators.
    """
    try:
        output = subprocess.check_output("emulator -list-avds", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        emulators = output.split("\n")
        emulators = list(filter(None, emulators))
        return emulators
    
    except subprocess.CalledProcessError:
        check_sdk()
        raise Exception("Error listing emulators. Make sure to install the emulator from the SDK Manager in Android Studio.")