"""
Scan components for bec_testing_plugin.

The scan components module allows you to define custom components that can be used in your scans.
These components can be used to encapsulate reusable logic, interact with devices, or perform specific actions during the scan lifecycle.
"""

from bec_server.scan_server.scans.scan_components import ScanComponents


class BecTestingPluginScanComponents(ScanComponents):
    """Scan components for bec_testing_plugin."""
