#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import warnings
from typing import TYPE_CHECKING, Any, cast

from appium_selenium.common.exceptions import UnknownMethodException

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.protocols.webdriver.can_remember_extension_presence import CanRememberExtensionPresence
from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class Common(CanExecuteCommands, CanExecuteScripts, CanRememberExtensionPresence):
    def end_test_coverage(self, intent: str, path: str) -> Any:
        """Ends the coverage collection and pull the coverage.ec file from the device.
        deprecated:: 2.9.0

        Android only.
        See https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/android/android-coverage.md

        Args:
            intent: description of operation to be performed
            path: path to coverage.ec file to be pulled from the device

        Returns:
            TODO
        """
        warnings.warn(
            'This API is deprecated and will be removed in future versions',
            DeprecationWarning,
        )
        return self.execute(
            Command.END_TEST_COVERAGE,
            {
                'intent': intent,
                'path': path,
            },
        )['value']

    def open_notifications(self) -> 'WebDriver':
        """Open notification shade in Android (API Level 18 and above)

        Returns:
            Union['WebDriver', 'Common']: Self instance
        """
        ext_name = 'mobile: openNotifications'
        try:
            self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            self.mark_extension_absence(ext_name).execute(Command.OPEN_NOTIFICATIONS, {})
        return cast('WebDriver', self)

    @property
    def current_package(self) -> str:
        """Retrieves the current package running on the device."""
        ext_name = 'mobile: getCurrentPackage'
        try:
            return self.assert_extension_exists(ext_name).execute_script(ext_name)
        except UnknownMethodException:
            # TODO: Remove the fallback
            return self.mark_extension_absence(ext_name).execute(Command.GET_CURRENT_PACKAGE)['value']

    def _add_commands(self) -> None:
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.GET_CURRENT_PACKAGE] = (
            'GET',
            '/session/$sessionId/appium/device/current_package',
        )
        commands[Command.END_TEST_COVERAGE] = (
            'POST',
            '/session/$sessionId/appium/app/end_test_coverage',
        )
        commands[Command.OPEN_NOTIFICATIONS] = (
            'POST',
            '/session/$sessionId/appium/device/open_notifications',
        )
