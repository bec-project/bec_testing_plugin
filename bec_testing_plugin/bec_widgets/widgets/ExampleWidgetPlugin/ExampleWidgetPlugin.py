from bec_widgets.utils.bec_widget import BECWidget
from qtpy.QtWidgets import QWidget

from bec_testing_plugin.bec_widgets.widgets.ExampleWidgetPlugin.ExampleWidgetPlugin_ui import (
    Ui_Examplewidgetplugin,
)


class Examplewidgetplugin(BECWidget, QWidget, Ui_Examplewidgetplugin):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, **kwargs)
