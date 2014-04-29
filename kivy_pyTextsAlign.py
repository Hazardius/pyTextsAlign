#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner


from pta_alignment import alignment, atype
from pta_files import open_file

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    alignment = None
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    align_type = ObjectProperty(None)
    file_1_input = ObjectProperty(None)
    file_1_lang = ObjectProperty(None)
    file_2_input = ObjectProperty(None)
    file_2_lang = ObjectProperty(None)
    al_text = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_save(self):
        if (alignment != None):
            content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
            self._popup = Popup(title="Save alignment", content=content, size_hint=(0.9, 0.9))
            self._popup.open()

    def show_ch1(self):
        content = LoadDialog(load=self.choose_file_1, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose file 1", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def choose_file_1(self, path, filename):
        file_1_path = os.path.join(path, filename[0])
        self.file_1_input.text = file_1_path

        self.dismiss_popup()

    def show_ch2(self):
        content = LoadDialog(load=self.choose_file_2, cancel=self.dismiss_popup)
        self._popup = Popup(title="Choose file 2", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def choose_file_2(self, path, filename):
        file_2_path = os.path.join(path, filename[0])
        self.file_2_input.text = file_2_path

        self.dismiss_popup()

    def _check_atype_(self):
        selected = self.align_type.text
        if selected == 'Naive':
            return atype.NAIVE
        elif selected == 'Simple':
            return atype.SIMPLE
        elif selected == 'Hunalign':
            return atype.HUNALIGN

    def align(self):
        if ((self.file_1_input.text != '') and (self.file_2_input != '')):
            self.alignment = alignment(self._check_atype_(), (self.file_1_input.text, self.file_1_lang.text),\
                (self.file_2_input.text, self.file_2_lang.text))
            # self.show_alignment()
            self.al_text.text = self.alignment.get_core()

    def save(self, path, filename):
        # self.alignment.save(os.path.join(path, filename), 'w')
        with codecs.open(os.path.join(path, filename), 'w', 'utf-8') as stream:
            stream.write(self.al_text.text)

        self.dismiss_popup()

class PyTextsAlignApp(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    PyTextsAlignApp().run()
