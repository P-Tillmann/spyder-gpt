# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2023, Peter Tillmann
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
GPT in Spyder Preferences Page.
"""
from spyder.api.preferences import PluginConfigPage
from spyder.api.translations import get_translation

_ = get_translation("spyder_gpt.spyder")


class GPTinSpyderConfigPage(PluginConfigPage):

    # --- PluginConfigPage API
    # ------------------------------------------------------------------------
    def setup_page(self):
        pass
