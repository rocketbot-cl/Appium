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
'''
    Declare Rocketbot variables
'''
GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

import os
import sys
import traceback



base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'Appium' + os.sep + 'libs' + os.sep

if cur_path not in sys.path:
    sys.path.append(cur_path)

global mod_appium_session
from AppiumObject import AppiumObject, check_appium, check_uiautomator, check_sdk, check_java, check_path, pair_device, list_emulators # type: ignore
from appium_selenium.common.exceptions import InvalidSessionIdException # type: ignore
from appium_selenium.common.exceptions import WebDriverException # type: ignore

try:
    if not mod_appium_session: # type: ignore
        mod_appium_session = None
except NameError:
    mod_appium_session = None


module = GetParams("module")



'''
    Commands
'''
try:
    if module == "config_appium":
        result = GetParams("result")

        try:
            check_appium()
            check_uiautomator()
            check_sdk()
            check_java()
            check_path()

            SetVar(result, True)
        
        except Exception as e:
            SetVar(result, False)
            raise e


    if module == "pair_device":
        pair_ip = GetParams("pair_ip")
        pair_code = GetParams("pair_code")
        result = GetParams("result")

        try:
            paired = pair_device(pair_ip, pair_code)

            SetVar(result, paired)
        
        except Exception as e:
            SetVar(result, False)
            raise e


    if module == "connect_android":
        device_ip = GetParams("device_ip")
        connection_type = GetParams("connection_type")
        allow_shell = GetParams("allow_shell")
        unlock_type = GetParams("unlock_type")
        unlock_key = GetParams("unlock_key")
        result = GetParams("result")

        try:
            mod_appium_session = AppiumObject(device_ip, 
                                              connection_type, 
                                              allow_shell, 
                                              unlock_type, 
                                              unlock_key, 
                                              is_emulator=False, 
                                              emulator_name=None)

            SetVar(result, True)
        
        except Exception as e:
            SetVar(result, False)
            raise e

    if module == "list_emulators":
        result = GetParams("result")

        try:

            emulators = list_emulators()

            SetVar(result, emulators)

        except Exception as e:
            SetVar(result, False)
            raise e

    if module == "connect_emulator":
        emulator_name = GetParams("emulator_name")
        allow_shell = GetParams("allow_shell")
        unlock_type = GetParams("unlock_type")
        unlock_key = GetParams("unlock_key") if unlock_type else None
        result = GetParams("result")
        

        try:
            emulators = list_emulators()

            if emulator_name not in emulators:
                raise Exception("Emulator not found")

            mod_appium_session = AppiumObject(None, 
                                              None, 
                                              allow_shell,
                                              unlock_type, 
                                              unlock_key, 
                                              is_emulator=True, 
                                              emulator_name=emulator_name)

            SetVar(result, True)
        
        except Exception as e:
            SetVar(result, False)
            raise e

    if module == "simple_swipe":
        direction = GetParams("direction")

        try:
            mod_appium_session.simple_swipe(direction)
        except Exception as e:
            traceback.print_exc()
            raise e

    if module == "simple_tap":
        x = GetParams("x")
        y = GetParams("y")

        try:
            mod_appium_session.simple_tap(x, y)
        except Exception as e:
            traceback.print_exc()
            raise e

    if module == "tap_object":
        selector = GetParams("selector")
        data_type = GetParams("data_type")
        result = GetParams("result")

        try:
            mod_appium_session.tap_object(selector, data_type)

            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            traceback.print_exc()
            raise e

    if module == "send_keys":
        data_type = GetParams("data_type")
        selector = GetParams("selector")
        text = GetParams("text")

        try:
            mod_appium_session.send_keys(selector, data_type, text)
        except Exception as e:
            traceback.print_exc()
            raise e


    if module == "get_text":
        data_type = GetParams("data_type")
        selector = GetParams("selector")
        result = GetParams("result")

        try:
            text = mod_appium_session.get_text(selector, data_type)

            SetVar(result, text)
        except Exception as e:
            SetVar(result, False)
            raise e


    if module == "get_text_coord":
        coords = GetParams("coordinates")
        result = GetParams("result")

        try:
            text = mod_appium_session.get_text_coord(coords)

            if not text:
                raise Exception("No element with text was found in the coordinates.")

            SetVar(result, text)
        except Exception as e:
            SetVar(result, False)
            raise e

    
    if module == "get_screenshot":
        path = GetParams("path")

        if not path:
            raise Exception("Please specify a path")
        if not path.endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
            path = path + ".png"

        try:
            mod_appium_session.get_screenshot(path)
        except Exception as e:
            traceback.print_exc()
            raise e

    if module == "run_command":
        command = GetParams("command")
        result = GetParams("result")

        try:
            output = mod_appium_session.android_driver.execute_script('mobile: shell', {'command': command})

            SetVar(result, output)
        except Exception as e:
            SetVar(result, False)
            raise e

    if module == "get_current_app_data":
        result = GetParams("result")
        current_app = {}

        try:
            current_app["package_name"] = mod_appium_session.android_driver.current_package
            current_app["activity_name"] = mod_appium_session.android_driver.current_activity

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

            mod_appium_session.android_driver.start_activity(package_name, activity_name)

            SetVar(result, True)
        except Exception as e:
            SetVar(result, False)
            raise e


    if module == "disconnect_android":
        try:
            mod_appium_session.android_driver.quit()
            mod_appium_session.kill_server()
            mod_appium_session = None

        except AttributeError:
            AppiumObject.kill_server()
            mod_appium_session = None
            raise Exception("No device connected.")
        
        except (InvalidSessionIdException, WebDriverException):
            AppiumObject.kill_server()
            mod_appium_session = None
            raise Exception("The session unexpectedly closed.")
    


    if module == "lock_device":
        try:
            mod_appium_session.lock()
        except Exception as e:
            traceback.print_exc()
            raise e

    if module == "unlock_device":
        try:
            mod_appium_session.unlock()
        except Exception as e:
            traceback.print_exc()
            raise e

    if module == "coords_zoom":
        action = GetParams("action")
        speed = eval(GetParams("speed")) if GetParams("speed") else 1
        coords = GetParams("coordinates")
        pixels = int(GetParams("pixels"))

        try:
            mod_appium_session.coords_zoom(action, speed, coords, pixels)
        except Exception as e:
            traceback.print_exc()
            raise e

    if module == "object_zoom":
        action = GetParams("action")
        speed = eval(GetParams("speed")) if GetParams("speed") else 1
        data_type = GetParams("data_type")
        selector = GetParams("selector")
        pixels = int(GetParams("pixels"))

        try:
            mod_appium_session.object_zoom(action, speed, selector, data_type, pixels)
        except Exception as e:
            traceback.print_exc()
            raise e


except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e