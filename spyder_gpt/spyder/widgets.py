# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2023, Peter Tillmann
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
GPT in Spyder Main Widget.
"""

import os
import openai
openai.organization = "org-WJrCSHEbMT7I03koyiM7aAk5"
openai.api_key = os.getenv("OPENAI_API_KEY")


# Third party imports
from qtpy.QtWidgets import QHBoxLayout, QLabel


# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation

from spyder.api.widgets.main_widget import PluginMainWidget


# Localization
_ = get_translation("spyder_gpt.spyder")

from qtpy.QtWidgets import QTextBrowser, QWidget, QVBoxLayout, QSizePolicy, QSpacerItem, QPushButton
from spyder.api.widgets.mixins import SpyderWidgetMixin

from spyder.api.widgets.status import BaseTimerStatus
from spyder.utils.icon_manager import ima

# Third party imports
import qtawesome as qta


from qtpy.QtWidgets import QPlainTextEdit, QWidget, QVBoxLayout, QTextEdit
from spyder.api.widgets.mixins import SpyderWidgetMixin

class GPTinSpyderActions:
    ExampleAction = "example_action"


class GPTinSpyderToolBarSections:
    ExampleSection = "example_section"


class GPTinSpyderOptionsMenuSections:
    ExampleSection = "example_section"


simple_css = """
.chatbot-container {
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-bottom: 10px;
    padding: 10px;
}

/* Chatbot message */
.chatbot-message {
    background-color: #34495e;
    color: white;
    border-radius: 5px;
    padding: 12px 15px;
    margin-bottom: 5px;
    font-size: 14px;
}

/* User message */
.user-message {
    background-color: #2980b9;
    color: white;
    border-radius: 5px;
    padding: 12px 15px;
    margin-bottom: 5px;
    text-align: right;
    font-size: 14px;
}
"""

class GPTinSpyderWidget(PluginMainWidget):

    # PluginMainWidget class constants

    # Signals

    def __init__(self, name=None, plugin=None, parent=None):
        super().__init__(name, plugin, parent)

       

        self.browser = QTextBrowser()
        self.browser.setPlaceholderText("Test Text Browser")

        # Create a vertical layout and add the output widget to it
        
        self.editor = QPlainTextEdit()

        # set the size policy for the editor widget
        editor_size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        editor_size_policy.setVerticalStretch(0)
        editor_size_policy.setVerticalPolicy(QSizePolicy.Fixed)
        editor_size_policy.setHorizontalStretch(1)
        self.editor.setSizePolicy(editor_size_policy)

        # set the height of the editor widget to 30% of the height of the plugin widget
        editor_height = int(self.height() * 0.3)
        print(f"Editor height: {editor_height}")
        
        self.editor.setFixedHeight(300)
        
        #self.editor.set
        
        spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.button = QPushButton("Sent")
        self.button.clicked.connect(self.display_text)

        layout = QVBoxLayout()
        
        layout.addWidget(self.browser)
        #layout.addItem(spacer)
        layout.addWidget(self.editor)
        layout.addWidget(self.button)

        # Create a vertical layout and add the input widget to it
        
        self.setLayout(layout)

    # --- PluginMainWidget API
    # ------------------------------------------------------------------------
    def get_title(self):
        return _("GPT in Spyder")

    def get_focus_widget(self):
        pass
    
    def display_text(self):
       # get the text from the editor widget
       prompt = self.editor.toPlainText()
       
       response = openai.ChatCompletion.create(
         model="gpt-3.5-turbo",
         messages=[{"role": "system", "content": "You are a helpful assistant for python programming integrated into the spyder IDE."},
                   {"role": "user", "content": prompt}],
         temperature=0.7,
         max_tokens=256,
         top_p=1.0,
         frequency_penalty=0.0,
         presence_penalty=0.0
       )
       
       response = response['choices'][0]['message']['content']
       
       html_content = f"""
       <div class="user-message" style="text-align:right;">{prompt}</div> 
       <div class="chatbot-message" style="text-align:left;">{response}</div> 
        """
        
       # set the HTML content of the browser widget to the text
       text_document = self.browser.document()
       text_document.setDefaultStyleSheet(simple_css)
       self.browser.setHtml(html_content)
       

    def setup(self):
        # Create an example action
        example_action = self.create_action(
            name=GPTinSpyderActions.ExampleAction,
            text="Example action",
            tip="Example hover hint",
            icon=self.create_icon("spyder"),
            triggered=lambda: print("Example action triggered!"),
        )

        # Add an example action to the plugin options menu
        menu = self.get_options_menu()
        self.add_item_to_menu(
            example_action,
            menu,
            GPTinSpyderOptionsMenuSections.ExampleSection,
        )

        # Add an example action to the plugin toolbar
        toolbar = self.get_main_toolbar()
        self.add_item_to_toolbar(
            example_action,
            toolbar,
            GPTinSpyderOptionsMenuSections.ExampleSection,
        )

    def update_actions(self):
        pass

    @on_conf_change
    def on_section_conf_change(self, section):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
