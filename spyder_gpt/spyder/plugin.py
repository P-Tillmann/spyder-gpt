# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2023, Peter Tillmann
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
GPT in Spyder Plugin.
"""

# Third-party imports
from qtpy.QtGui import QIcon

# Spyder imports
from spyder.api.plugins import Plugins, SpyderDockablePlugin
from spyder.api.translations import get_translation

# Local imports
from spyder_gpt.spyder.confpage import GPTinSpyderConfigPage
from spyder_gpt.spyder.widgets import GPTinSpyderWidget

_ = get_translation("spyder_gpt.spyder")


class GPTinSpyder(SpyderDockablePlugin):
    """
    GPT in Spyder plugin.
    """

    NAME = "spyder_gpt"
    REQUIRES = []
    OPTIONAL = []
    WIDGET_CLASS = GPTinSpyderWidget
    CONF_SECTION = NAME
    CONF_WIDGET_CLASS = GPTinSpyderConfigPage

    # --- Signals

    # --- SpyderDockablePlugin API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("GPT in Spyder")

    def get_description(self):
        return _("A simple GPT interface in Spyder")

    def get_icon(self):
        return QIcon()

    def on_initialize(self):
        widget = self.get_widget()
        

    def check_compatibility(self):
        valid = True
        message = ""  # Note: Remember to use _("") to localize the string
        return valid, message

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------
