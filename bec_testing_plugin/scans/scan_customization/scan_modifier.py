"""
Scan modifier plugin for bec_testing_plugin.

The scan modifier allows you to modify the scan lifecycle and run custom actions before or after the scan hook or replace the scan hook entirely.
Note that the scan_modifier module must be registered as a plugin in the pyproject.toml file for it to be recognized by the BEC framework and that
there can only be one scan_modifier plugin registered at a time. If you need to run multiple scan modifiers, you can create a single scan
modifier plugin that runs multiple actions in sequence with conditional logic to determine which actions to run based on the scan context.
"""

from typing import Any

from bec_server.scan_server.scans.scan_modifier import ScanModifier


class BecTestingPluginScanModifier(ScanModifier):
    """
    Scan modifier for bec_testing_plugin.

    By inheriting from the ScanModifier base class, you get access to currently running scan (self.scan), the devices (self.dev), the scan info (self.scan_info),
    the scan components (self.components) and the scan actions (self.actions).
    """

    # @staticmethod
    # def scan_signature_overrides(
    #     scan_name: str, arguments: dict[str, Any | None], defaults: dict[str, Any]
    # ) -> tuple[dict, dict]:
    #     if "relative" in arguments:
    #         arguments.pop("relative", None)
    #         defaults["relative"] = False
    #     if scan_name == "custom_testing_scan":
    #         arguments.pop("settling_time", None)
    #         defaults.pop("settling_time", None)
    #     return arguments, defaults
