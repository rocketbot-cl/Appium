# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import re
import sys
import time
import traceback
import subprocess

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Appium' + os.sep + 'libs' + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy


from appium_selenium.webdriver.common.action_chains import ActionChains
from appium_selenium.webdriver.common.actions import interaction
from appium_selenium.webdriver.common.actions.action_builder import ActionBuilder
from appium_selenium.webdriver.common.actions.pointer_input import PointerInput


module = GetParams("module")
global android_driver, mod_consoles

try:
    if module == "config_appium":
        result = GetParams("result")


        try:
            # Check if appium is installed
            command = "appium -v"
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

            print("Appium version: ", output.strip())

        except subprocess.CalledProcessError as e:
            print("Appium is not installed. Installing...")

            command = "npm i --location=global appium@2.1.3"
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            print("Appium installed successfully")
        
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

        except:
            SetVar(result, False)
            print("Error installing uiautomator2 driver")
            raise e

        SetVar(result, True)

    if module == "pair_device":
        pair_ip = GetParams("pair_ip")
        pair_code = GetParams("pair_code")
        result = GetParams("result")

        try:
            subprocess.run("adb kill-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            subprocess.run("adb start-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            output = subprocess.check_output(f"adb pair {pair_ip} {pair_code}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

            if "successfully" in output.lower():
                SetVar(result, True)
            else:
                SetVar(result, False)
                raise Exception("Error pairing device. Please check the IP and code")

        except Exception as e:
            SetVar(result, False)
            raise e

    if module == "connect_android":
        device_ip = GetParams("device_ip")
        connection_type = GetParams("connection_type")
        allow_shell = GetParams("allow_shell")
        result = GetParams("result")
        mod_consoles = []

        try:
            subprocess.run("adb kill-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            user_folder = os.path.expanduser("~")
            appium_path = os.path.join(user_folder, "AppData", "Roaming", "npm", "appium.cmd")

            if allow_shell:
                print("Allowing insecure adb shell")
                appium_command = "appium --allow-insecure=adb_shell"
            else:
                appium_command = "appium"

            appium_console = subprocess.Popen(appium_command, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            mod_consoles.append(appium_console)

            subprocess.run("adb start-server")

            if connection_type == "wifi":
                output = subprocess.check_output(f"adb connect {device_ip}", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            elif connection_type == "usb":
                output = "connected"


            if "connected" or "" in output:
                caps = {}
                caps["platformName"] = "Android"
                caps["appium:automationName"] = "uiautomator2"
                caps["appium:deviceName"] = "Android Device"
                caps["appium:ensureWebviewsHavePages"] = True
                caps["appium:nativeWebScreenshot"] = True
                caps["appium:newCommandTimeout"] = 3600
                caps["appium:connectHardwareKeyboard"] = True

                android_driver = webdriver.Remote("http://127.0.0.1:4723", caps)

                SetVar(result, True)

            else:
                SetVar(result, False)
                traceback.print_exc()
                raise Exception("Error connecting to device")
        
        except Exception as e:
            SetVar(result, False)
            for console in mod_consoles:
                try:
                    console.terminate()
                    console.kill()
                except:
                    pass
            raise e

    if module == "list_emulators":
        result = GetParams("result")

        try:
            output = subprocess.check_output("emulator -list-avds", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            emulators = output.split("\n")
            emulators = list(filter(None, emulators))

            SetVar(result, emulators)

        except Exception as e:
            SetVar(result, False)
            raise e

    if module == "connect_emulator":
        emulator_name = GetParams("emulator_name")
        allow_shell = GetParams("allow_shell")
        result = GetParams("result")
        mod_consoles = []

        try:
            subprocess.run("adb kill-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            if allow_shell:
                print("Allowing insecure adb shell")
                appium_command = "appium --allow-insecure=adb_shell"
            else:
                appium_command = "appium"

            appium_console = subprocess.Popen(appium_command, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            mod_consoles.append(appium_console)

            subprocess.run("adb start-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            
            emulator_console = subprocess.Popen(f"emulator @{emulator_name}", shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            mod_consoles.append(emulator_console)

            wait_console = subprocess.Popen("adb wait-for-device", shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            mod_consoles.append(wait_console)

            caps = {}
            caps["platformName"] = "Android"
            caps["appium:automationName"] = "uiautomator2"
            caps["appium:deviceName"] = "Android Emulator"
            caps["appium:ensureWebviewsHavePages"] = True
            caps["appium:nativeWebScreenshot"] = True
            caps["appium:newCommandTimeout"] = 3600
            caps["appium:connectHardwareKeyboard"] = True

            android_driver = webdriver.Remote("http://127.0.0.1:4723", caps)

            SetVar(result, True)
        
        except Exception as e:
            SetVar(result, False)
            for console in mod_consoles:
                try:
                    console.terminate()
                    console.kill()
                except:
                    pass
            raise e

    if module == "simple_swipe":
        direction = GetParams("direction")

        size = android_driver.get_window_size()
        

        actions = ActionChains(android_driver)
        actions.w3c_actions = ActionBuilder(android_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

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


    if module == "simple_tap":
        x = GetParams("x")
        y = GetParams("y")

        actions = ActionChains(android_driver)
        actions.w3c_actions = ActionBuilder(android_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))

        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    if module == "tap_object":
        selector = GetParams("selector")
        data_type = GetParams("data_type")
        result = GetParams("result")

        try:
            if data_type == "id":
                element = android_driver.find_element(by=AppiumBy.ID, value=selector)
            elif data_type == "xpath":
                element = android_driver.find_element(by=AppiumBy.XPATH, value=selector)
            elif data_type == "class":
                element = android_driver.find_element(by=AppiumBy.CLASS_NAME, value=selector)
            else:
                raise Exception("Invalid data type")

            element.click()

            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            raise e

    # if module == "scroll_to_object":
    #     selector = GetParams("selector")
    #     data_type = GetParams("data_type")
    #     result = GetParams("result")

    #     try:
    #         if data_type == "id":
    #             element = android_driver.find_element(by=AppiumBy.ID, value=selector)
    #         elif data_type == "xpath":
    #             element = android_driver.find_element(by=AppiumBy.XPATH, value=selector)
    #         elif data_type == "class":
    #             element = android_driver.find_element(by=AppiumBy.CLASS_NAME, value=selector)
    #         else:
    #             raise Exception("Invalid data type")

    #         print(element.location)

    #         # action = webdriver.common.touch_action.TouchAction(android_driver)
    #         # action.scroll_from_element(element, 0, 10).perform()


            

    #         SetVar(result, True)

    #     except Exception as e:
    #         SetVar(result, False)
    #         raise e

    if module == "send_keys":
        data_type = GetParams("data_type")
        selector = GetParams("selector")
        text = GetParams("text")

        if data_type == "id":
            element = android_driver.find_element(by=AppiumBy.ID, value=selector)
            element.click()
        elif data_type == "xpath":
            element = android_driver.find_element(by=AppiumBy.XPATH, value=selector)
        elif data_type == "class":
            element = android_driver.find_element(by=AppiumBy.CLASS_NAME, value=selector)
        else:
            raise Exception("Invalid data type")
        
        element.send_keys(text)


    if module == "get_text":
        data_type = GetParams("data_type")
        selector = GetParams("selector")
        result = GetParams("result")

        if data_type == "id":
            element = android_driver.find_element(by=AppiumBy.ID, value=selector)
        elif data_type == "xpath":
            element = android_driver.find_element(by=AppiumBy.XPATH, value=selector)
        elif data_type == "class":
            element = android_driver.find_element(by=AppiumBy.CLASS_NAME, value=selector)
        else:
            raise Exception("Invalid data type")

        SetVar(result, element.get_attribute("text"))

    if module == "get_text_coord":
        coords = GetParams("coordinates")
        result = GetParams("result")

        x,y = coords.split(",")

        for element in android_driver.find_elements(by=AppiumBy.XPATH, value="//*"):
            text = element.get_attribute("text")

            if not text:
                continue
            bounds = element.get_attribute("bounds")
            bounds = bounds.replace("[", "").replace("]", ",").split(",")[:-1]

            if int(bounds[0]) <= int(x) <= int(bounds[2]) and int(bounds[1]) <= int(y) <= int(bounds[3]):
                SetVar(result, text)
                break

            if element == android_driver.find_elements(by=AppiumBy.XPATH, value="//*")[-1]:
                SetVar(result, False)
                raise Exception("No element with text was found")

    
    if module == "get_screenshot":
        path = GetParams("path")

        if not path:
            raise Exception("Please specify a path")
        if not path.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            path = path + ".png"

        screenshotBase64 = android_driver.get_screenshot_as_base64()
        screenshotDecoded = base64.b64decode(screenshotBase64)

        with open(path, "wb") as f:
            f.write(screenshotDecoded)

    if module == "run_command":
        command = GetParams("command")
        result = GetParams("result")

        try:
            output = android_driver.execute_script('mobile: shell', {'command': command})

            SetVar(result, output)
        except Exception as e:
            SetVar(result, False)
            raise e

    if module == "get_current_app_data":
        result = GetParams("result")
        current_app = {}

        try:
            current_app["package_name"] = android_driver.current_package
            current_app["activity_name"] = android_driver.current_activity

            SetVar(result, current_app)
        except Exception as e:
            SetVar(result, False)
            raise e


    if module == "start_app":
        package_name = GetParams("package_name")
        activity_name = GetParams("activity_name")
        result = GetParams("result")

        try:
            if not activity_name or not package_name:
                raise Exception("Please specify a package name and activity name")

            android_driver.start_activity(package_name, activity_name)

            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            raise e


    if module == "disconnect_android":
        subprocess.run("adb kill-server", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        try:
            android_driver.quit()
        except:
            pass
        for console in mod_consoles:
            try:
                console.terminate()
                console.kill()
            except:
                pass

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e